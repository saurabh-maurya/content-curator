"""
FastAPI Backend for Instagram AI Avatar Automation
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Dict, List
import json
import os

import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

from constants import (
    AVAILABLE_MODELS,
    CONTENT_CREATION_CHECKLIST,
    CONTENT_TYPES,
    TRENDING_PROFILES,
)
from langgraph_workflow import run_content_creation

app = FastAPI(title="Instagram AI Avatar Automation API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For personal use, allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for checklist states (simple persistence)
checklist_storage: Dict[str, Dict] = {}


class ContentRequest(BaseModel):
    topic: str
    content_type: str
    api_key: str
    api_model: str


class ChecklistUpdate(BaseModel):
    task_id: str
    status: str  # "completed", "pending", "manual", "failed"


@app.get("/")
async def root():
    return {"message": "Instagram AI Avatar Automation API"}


@app.get("/api/config")
async def get_config():
    """Get available models, checklist items, and content types"""
    return {
        "models": AVAILABLE_MODELS,
        "checklist": CONTENT_CREATION_CHECKLIST,
        "content_types": CONTENT_TYPES,
        "trending_profiles": TRENDING_PROFILES,
    }


@app.post("/api/create-content")
async def create_content(request: ContentRequest):
    """Trigger content creation workflow"""
    try:
        # Validate content type
        if request.content_type not in CONTENT_TYPES:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid content type. Must be one of: {CONTENT_TYPES}",
            )
        
        # Validate API model
        if request.api_model not in AVAILABLE_MODELS:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid API model. Must be one of: {AVAILABLE_MODELS}",
            )
        
        # Run workflow
        result = run_content_creation(
            topic=request.topic,
            content_type=request.content_type,
            api_key=request.api_key,
            api_model=request.api_model,
        )
        
        # Store checklist status
        session_id = f"{request.topic}_{request.content_type}"
        checklist_storage[session_id] = result.get("checklist_status", {})
        
        return {
            "success": True,
            "result": {
                "script": result.get("script", ""),
                "carousel_content": result.get("carousel_content", ""),
                "caption": result.get("caption", ""),
                "hashtags": result.get("hashtags", ""),
                "alt_text": result.get("alt_text", ""),
                "avatar_dialogue": result.get("avatar_dialogue", ""),
                "checklist_status": result.get("checklist_status", {}),
            },
            "errors": result.get("errors", []),
            "session_id": session_id,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Content creation failed: {str(e)}")


@app.get("/api/checklist/{session_id}")
async def get_checklist(session_id: str):
    """Get checklist status for a session"""
    if session_id in checklist_storage:
        return {
            "success": True,
            "checklist_status": checklist_storage[session_id],
        }
    return {
        "success": True,
        "checklist_status": {},
    }


@app.post("/api/checklist/{session_id}")
async def update_checklist(session_id: str, update: ChecklistUpdate):
    """Update checklist item status"""
    if session_id not in checklist_storage:
        checklist_storage[session_id] = {}
    
    checklist_storage[session_id][update.task_id] = update.status
    
    return {
        "success": True,
        "checklist_status": checklist_storage[session_id],
    }


@app.get("/api/checklist")
async def get_all_checklists():
    """Get all checklist sessions (for debugging)"""
    return {
        "success": True,
        "sessions": checklist_storage,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

