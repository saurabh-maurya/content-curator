"""
Constants for Instagram AI Avatar Automation System
Loads from environment variables, then provides constants throughout the codebase.
"""
import os
from typing import List

# API Configuration
API_KEY = os.getenv("API_KEY", "")
API_MODEL = os.getenv("API_MODEL", "gpt-4o-mini")

# Available API Models
AVAILABLE_MODELS = [
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-4-turbo",
    "gpt-3.5-turbo",
    "claude-3-5-sonnet-20241022",
    "claude-3-opus-20240229",
    "gemini-1.5-flash",  # Recommended for free tier - fast and efficient
    "gemini-1.5-pro",    # More capable, may have stricter rate limits on free tier
    "gemini-pro",        # Legacy model (deprecated, use gemini-1.5-flash instead)
]

# Trending Instagram Profiles (same genre) - for content inspiration
# Add your niche profiles here or via environment variable
TRENDING_PROFILES_ENV = os.getenv("TRENDING_PROFILES", "")
TRENDING_PROFILES: List[str] = (
    [p.strip() for p in TRENDING_PROFILES_ENV.split(",") if p.strip()]
    if TRENDING_PROFILES_ENV
    else [
        # Default examples - replace with your niche
        "@garyvee",
        "@neilpatel",
        "@amyporterfield",
        "@socialmediaexaminer",
    ]
)

# Content Creation Checklist Items
CONTENT_CREATION_CHECKLIST = [
    {
        "id": "generate_idea",
        "name": "Generate Reel/Carousel idea",
        "description": "Create content idea using AI based on trending profiles",
        "automated": True,
    },
    {
        "id": "generate_script",
        "name": "Generate script/content",
        "description": "Create script for Reel or content for Carousel",
        "automated": True,
    },
    {
        "id": "generate_caption",
        "name": "Generate caption",
        "description": "Create catchy caption with emojis",
        "automated": True,
    },
    {
        "id": "generate_hashtags",
        "name": "Generate hashtags",
        "description": "Suggest 10-12 relevant hashtags",
        "automated": True,
    },
    {
        "id": "generate_alt_text",
        "name": "Generate alt text",
        "description": "Create accessibility alt text for image/video",
        "automated": True,
    },
    {
        "id": "create_voiceover",
        "name": "Create voiceover (TTS)",
        "description": "Generate voiceover using TTSMaker/ElevenLabs",
        "automated": False,  # External tool
    },
    {
        "id": "build_avatar_video",
        "name": "Build avatar video",
        "description": "Create AI avatar video using HeyGen/CapCut",
        "automated": False,  # External tool
    },
    {
        "id": "edit_video",
        "name": "Edit in CapCut",
        "description": "Add captions, emojis, transitions, trending audio",
        "automated": False,  # External tool
    },
    {
        "id": "upload_post",
        "name": "Upload + caption + alt text",
        "description": "Post to Instagram with generated content",
        "automated": False,  # Manual step
    },
    {
        "id": "engage_audience",
        "name": "Engage for 20 minutes",
        "description": "Reply to comments and engage with audience",
        "automated": False,  # Manual step
    },
    {
        "id": "track_metrics",
        "name": "Track saves/comments/shares",
        "description": "Monitor engagement metrics",
        "automated": False,  # Manual step
    },
]

# Content Types
CONTENT_TYPES = ["Reel", "Carousel", "Story", "Post"]

# Prompt Templates
PROMPT_TEMPLATES = {
    "reel_script": """Generate a {duration}-second Instagram Reel script on "{topic}" with:
- A 5-word hook
- 3 short key points
- 1-line CTA to save and share
Make it engaging and viral-worthy.""",
    
    "carousel_content": """Create 5 slides for an Instagram carousel titled "{topic}".
For each slide provide:
- Headline
- 1-sentence content
- Final slide with CTA
Format as JSON with slides array.""",
    
    "caption": """Write 3 short Instagram captions (<100 chars) for a post about "{topic}".
Each caption should include:
- A hook
- Emojis
- Call to action to comment
Format as JSON array.""",
    
    "hashtags": """Suggest 10-12 medium-difficulty hashtags for "{topic}" targeting {audience}.
Format as comma-separated list.""",
    
    "alt_text": """Write alt text (≤120 chars) describing {content_type} about "{topic}".
Include a main keyword and be descriptive for accessibility.""",
    
    "avatar_dialogue": """Write a natural conversational script for an AI avatar explaining "{topic}".
Include:
- Hand gestures cues
- Emotional tone markers
- Natural pauses
Make it engaging and conversational.""",
}

