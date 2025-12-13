# Instagram AI Avatar Automation - Developer Guide

This guide is for developers who want to set up, run, and modify the application.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A terminal/command prompt
- (Optional) Virtual environment tool (venv)

## Project Structure

```
content_curator/
├── backend/
│   ├── __init__.py
│   ├── main.py                 # FastAPI server and API endpoints
│   ├── langgraph_workflow.py   # LangGraph supervisor workflow
│   └── constants.py            # Configuration, prompts, checklist
├── frontend/
│   ├── index.html             # Main UI
│   └── app.js                 # Frontend JavaScript
├── data/                      # Data directory (for future use)
├── manual_tasks.md            # Manual tasks documentation
├── requirements.txt           # Python dependencies
├── run_backend.sh            # Backend startup script
├── README.md                 # Main documentation
├── USER_GUIDE.md             # End-user guide
└── DEVELOPER_GUIDE.md        # This file
```

## Development Setup

### 1. Clone/Navigate to Project

```bash
cd /path/to/content_curator
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory (optional - API key can be entered in UI):

```env
API_KEY=your_api_key_here
API_MODEL=gpt-4o-mini
TRENDING_PROFILES=@profile1,@profile2,@profile3
```

**Note**: The app works without `.env` - users can input API key directly in the UI.

## Running the Application

### Start Backend Server

**Option 1: Using the startup script**
```bash
./run_backend.sh
```

**Option 2: Using uvicorn directly**
```bash
# From project root
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# Or from backend directory
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Option 3: Using Python directly**
```bash
cd backend
python main.py
```

The server will start on `http://localhost:8000`

### Start Frontend

**Option 1: Direct file open**
- Simply open `frontend/index.html` in your browser
- Works for basic testing

**Option 2: Local HTTP server (Recommended for development)**
```bash
# Using Python
cd frontend
python -m http.server 8080
# Then open http://localhost:8080

# Using Node.js (if installed)
npx http-server frontend -p 8080

# Using PHP (if installed)
php -S localhost:8080 -t frontend
```

### Verify Setup

1. Backend should show: `Uvicorn running on http://0.0.0.0:8000`
2. Visit `http://localhost:8000` - should see API welcome message
3. Visit `http://localhost:8000/api/config` - should see JSON config
4. Open frontend - should load without errors

## Development Workflow

### Making Backend Changes

1. Backend auto-reloads with `--reload` flag (uvicorn)
2. Changes to Python files trigger automatic restart
3. Check terminal for errors

### Making Frontend Changes

1. Edit `frontend/index.html` or `frontend/app.js`
2. Refresh browser to see changes
3. Use browser DevTools (F12) for debugging

### Testing API Endpoints

**Using curl:**
```bash
# Get config
curl http://localhost:8000/api/config

# Create content
curl -X POST http://localhost:8000/api/create-content \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "test topic",
    "content_type": "Reel",
    "api_key": "your_key",
    "api_model": "gpt-4o-mini"
  }'
```

**Using browser:**
- Visit `http://localhost:8000/api/config` for GET requests
- Use browser DevTools Network tab to inspect requests

**Using Postman/Insomnia:**
- Import endpoints from FastAPI docs at `http://localhost:8000/docs`

## Code Architecture

### Backend (`backend/`)

**main.py**
- FastAPI application setup
- CORS middleware configuration
- API endpoints:
  - `GET /api/config` - Get available models, checklist, content types
  - `POST /api/create-content` - Trigger content creation workflow
  - `GET /api/checklist/{session_id}` - Get checklist status
  - `POST /api/checklist/{session_id}` - Update checklist item

**langgraph_workflow.py**
- LangGraph state machine definition
- Content generation nodes (script, caption, hashtags, alt text)
- LLM provider abstraction (OpenAI, Anthropic, Google)
- Workflow orchestration

**constants.py**
- Configuration constants
- Environment variable loading
- Prompt templates
- Checklist definitions
- Trending profiles list

### Frontend (`frontend/`)

**index.html**
- UI structure and styling
- Form inputs for API config and content creation
- Results display area
- Checklist display

**app.js**
- API communication
- UI state management
- Checklist interaction
- Error handling

## Customization Guide

### Adding New API Models

Edit `backend/constants.py`:
```python
AVAILABLE_MODELS = [
    "gpt-4o",
    "gpt-4o-mini",
    "your-new-model",  # Add here
]
```

Then update `langgraph_workflow.py` `get_llm()` function to handle the new model.

### Modifying Checklist Items

Edit `backend/constants.py`:
```python
CONTENT_CREATION_CHECKLIST = [
    {
        "id": "new_task",
        "name": "New Task Name",
        "description": "Task description",
        "automated": True,  # or False
    },
    # ... existing items
]
```

### Customizing Prompts

Edit `PROMPT_TEMPLATES` in `backend/constants.py`:
```python
PROMPT_TEMPLATES = {
    "reel_script": "Your custom prompt template here with {placeholders}",
    # ... other templates
}
```

### Adding New Content Types

1. Add to `CONTENT_TYPES` in `backend/constants.py`
2. Update frontend dropdown in `frontend/index.html`
3. Add handling in `langgraph_workflow.py` `generate_script()` function

### Changing UI Styling

Edit CSS in `frontend/index.html` within `<style>` tags.

## Debugging

### Backend Issues

**Check logs:**
- Terminal output shows all errors
- FastAPI auto-reload shows import errors

**Common issues:**
- Import errors: Check `sys.path` modifications in `main.py` and `langgraph_workflow.py`
- Port already in use: Change port in uvicorn command or kill process on port 8000
- API key errors: Check LLM provider credentials

**Debug mode:**
```bash
# Run with debug logging
uvicorn backend.main:app --reload --log-level debug
```

### Frontend Issues

**Browser DevTools:**
- Console tab: JavaScript errors
- Network tab: API request/response inspection
- Elements tab: HTML/CSS inspection

**Common issues:**
- CORS errors: Ensure backend is running and CORS middleware is enabled
- API connection: Check `API_BASE_URL` in `app.js` matches backend URL
- UI not updating: Check JavaScript console for errors

### LangGraph Workflow Issues

**Check state:**
- Add print statements in workflow nodes
- Inspect `final_state` returned from `run_content_creation()`

**Common issues:**
- LLM provider errors: Verify API key and model name
- State errors: Check `ContentState` TypedDict matches usage

## Testing

### Manual Testing

1. Start backend and frontend
2. Test each content type (Reel, Carousel, Story, Post)
3. Test checklist marking (complete, manual)
4. Test error scenarios (invalid API key, network errors)

### API Testing

Use FastAPI's built-in docs:
- Visit `http://localhost:8000/docs`
- Interactive API documentation
- Test endpoints directly from browser

## Deployment Considerations

### For Personal Use (Current Setup)
- Current setup is fine for local/personal use
- No authentication needed
- In-memory storage (resets on restart)

### For Production (Future)
- Add database for checklist persistence
- Add user authentication
- Add environment-based configuration
- Add logging and monitoring
- Add error tracking
- Consider containerization (Docker)

## Dependencies

Key dependencies and their purposes:

- **fastapi**: Web framework for API
- **uvicorn**: ASGI server
- **langgraph**: Workflow orchestration
- **langchain**: LLM integration
- **langchain-openai**: OpenAI integration
- **langchain-anthropic**: Anthropic/Claude integration
- **langchain-google-genai**: Google Gemini integration
- **pydantic**: Data validation
- **python-dotenv**: Environment variable management

## Contributing

When modifying the code:

1. Follow existing code style
2. Update relevant documentation
3. Test changes locally
4. Update `manual_tasks.md` if adding new manual tasks
5. Update `USER_GUIDE.md` if UI/UX changes

## Troubleshooting Development Issues

### Python Import Errors

If you see `ModuleNotFoundError`:
```bash
# Ensure you're in the project root
# Check PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Port Conflicts

If port 8000 is in use:
```bash
# Find process using port
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process or use different port
uvicorn backend.main:app --reload --port 8001
```

### Virtual Environment Issues

If packages aren't found:
```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Additional Resources

- FastAPI Docs: https://fastapi.tiangolo.com/
- LangGraph Docs: https://langchain-ai.github.io/langgraph/
- LangChain Docs: https://python.langchain.com/

Happy coding! 🚀

