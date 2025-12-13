"""
LangGraph Supervisor Workflow for Content Creation
Orchestrates the content creation process using LangGraph.
"""
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
import json
import os

import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

from constants import PROMPT_TEMPLATES, CONTENT_CREATION_CHECKLIST


class ContentState(TypedDict):
    """State for content creation workflow"""
    topic: str
    content_type: str
    api_key: str
    api_model: str
    script: str
    caption: str
    hashtags: str
    alt_text: str
    avatar_dialogue: str
    carousel_content: str
    checklist_status: dict
    errors: list
    current_step: str


def get_llm(api_key: str, api_model: str):
    """Get appropriate LLM based on model name"""
    if api_model.startswith("gpt"):
        return ChatOpenAI(
            model=api_model,
            api_key=api_key,
            temperature=0.7,
        )
    elif api_model.startswith("claude"):
        return ChatAnthropic(
            model=api_model,
            api_key=api_key,
            temperature=0.7,
        )
    elif api_model.startswith("gemini"):
        return ChatGoogleGenerativeAI(
            model=api_model,
            google_api_key=api_key,
            temperature=0.7,
        )
    else:
        # Default to OpenAI
        return ChatOpenAI(
            model="gpt-4o-mini",
            api_key=api_key,
            temperature=0.7,
        )


def generate_script(state: ContentState) -> ContentState:
    """Generate script for Reel or content for Carousel"""
    try:
        llm = get_llm(state["api_key"], state["api_model"])
        
        if state["content_type"] == "Reel":
            prompt = PROMPT_TEMPLATES["reel_script"].format(
                duration=25,
                topic=state["topic"]
            )
        elif state["content_type"] == "Carousel":
            prompt = PROMPT_TEMPLATES["carousel_content"].format(
                topic=state["topic"]
            )
        else:
            prompt = f"Generate content for {state['content_type']} about {state['topic']}"
        
        response = llm.invoke(prompt)
        script = response.content
        
        if state["content_type"] == "Carousel":
            state["carousel_content"] = script
        else:
            state["script"] = script
        
        state["checklist_status"]["generate_script"] = "completed"
        state["current_step"] = "script_generated"
    except Exception as e:
        state["errors"].append(f"Script generation error: {str(e)}")
        state["checklist_status"]["generate_script"] = "failed"
    
    return state


def generate_caption(state: ContentState) -> ContentState:
    """Generate Instagram caption"""
    try:
        llm = get_llm(state["api_key"], state["api_model"])
        prompt = PROMPT_TEMPLATES["caption"].format(topic=state["topic"])
        
        response = llm.invoke(prompt)
        caption = response.content
        
        # Try to parse JSON if returned, otherwise use as-is
        try:
            captions_list = json.loads(caption)
            state["caption"] = captions_list[0] if isinstance(captions_list, list) else caption
        except:
            state["caption"] = caption
        
        state["checklist_status"]["generate_caption"] = "completed"
        state["current_step"] = "caption_generated"
    except Exception as e:
        state["errors"].append(f"Caption generation error: {str(e)}")
        state["checklist_status"]["generate_caption"] = "failed"
    
    return state


def generate_hashtags(state: ContentState) -> ContentState:
    """Generate hashtags"""
    try:
        llm = get_llm(state["api_key"], state["api_model"])
        prompt = PROMPT_TEMPLATES["hashtags"].format(
            topic=state["topic"],
            audience="Instagram users"
        )
        
        response = llm.invoke(prompt)
        hashtags = response.content.strip()
        
        state["hashtags"] = hashtags
        state["checklist_status"]["generate_hashtags"] = "completed"
        state["current_step"] = "hashtags_generated"
    except Exception as e:
        state["errors"].append(f"Hashtags generation error: {str(e)}")
        state["checklist_status"]["generate_hashtags"] = "failed"
    
    return state


def generate_alt_text(state: ContentState) -> ContentState:
    """Generate alt text for accessibility"""
    try:
        llm = get_llm(state["api_key"], state["api_model"])
        prompt = PROMPT_TEMPLATES["alt_text"].format(
            content_type=state["content_type"],
            topic=state["topic"]
        )
        
        response = llm.invoke(prompt)
        alt_text = response.content.strip()
        
        state["alt_text"] = alt_text
        state["checklist_status"]["generate_alt_text"] = "completed"
        state["current_step"] = "alt_text_generated"
    except Exception as e:
        state["errors"].append(f"Alt text generation error: {str(e)}")
        state["checklist_status"]["generate_alt_text"] = "failed"
    
    return state


def generate_avatar_dialogue(state: ContentState) -> ContentState:
    """Generate avatar dialogue script"""
    try:
        llm = get_llm(state["api_key"], state["api_model"])
        prompt = PROMPT_TEMPLATES["avatar_dialogue"].format(topic=state["topic"])
        
        response = llm.invoke(prompt)
        dialogue = response.content
        
        state["avatar_dialogue"] = dialogue
        state["current_step"] = "avatar_dialogue_generated"
    except Exception as e:
        state["errors"].append(f"Avatar dialogue generation error: {str(e)}")
    
    return state


def create_workflow():
    """Create LangGraph workflow for content creation"""
    workflow = StateGraph(ContentState)
    
    # Add nodes
    workflow.add_node("generate_script", generate_script)
    workflow.add_node("generate_caption", generate_caption)
    workflow.add_node("generate_hashtags", generate_hashtags)
    workflow.add_node("generate_alt_text", generate_alt_text)
    workflow.add_node("generate_avatar_dialogue", generate_avatar_dialogue)
    
    # Set entry point
    workflow.set_entry_point("generate_script")
    
    # Add edges - sequential flow
    workflow.add_edge("generate_script", "generate_caption")
    workflow.add_edge("generate_caption", "generate_hashtags")
    workflow.add_edge("generate_hashtags", "generate_alt_text")
    workflow.add_edge("generate_alt_text", "generate_avatar_dialogue")
    workflow.add_edge("generate_avatar_dialogue", END)
    
    return workflow.compile()


def run_content_creation(topic: str, content_type: str, api_key: str, api_model: str):
    """Run the content creation workflow"""
    # Initialize state
    initial_state = {
        "topic": topic,
        "content_type": content_type,
        "api_key": api_key,
        "api_model": api_model,
        "script": "",
        "caption": "",
        "hashtags": "",
        "alt_text": "",
        "avatar_dialogue": "",
        "carousel_content": "",
        "checklist_status": {
            "generate_idea": "completed",  # Idea is the topic provided
            "generate_script": "pending",
            "generate_caption": "pending",
            "generate_hashtags": "pending",
            "generate_alt_text": "pending",
        },
        "errors": [],
        "current_step": "starting",
    }
    
    # Create and run workflow
    workflow = create_workflow()
    final_state = workflow.invoke(initial_state)
    
    return final_state

