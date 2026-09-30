# Academic Teaching Assistant (RAG-based AI)

A local FastAPI-based web application that acts as an interactive academic teaching assistant using Google Gemini LLM and markdown-based context.

## System Requirements
- Python 3.10+
- Google Gemini API Key

## Installation & Configuration

1. **Clone or open the project folder in VS Code:**
   ```bash
   cd path/to/my_ai_ta
  1. Install dependencies:
  pip install fastapi uvicorn google-generativeai python-dotenv pydantic
 2. Configure Environment Variables:
Create a .env file in the root directory and add your API key and model:

Code snippet
GEMINI_API_KEY=your_actual_api_key_here
GEMINI_MODEL=gemini-1.5-flash
3.Execution
Start the FastAPI backend server using Uvicorn with auto-reload:

4.Bash
uvicorn main:app --reload
Open your browser and navigate to:

5.Plaintext
[http://127.0.0.1:8000](http://127.0.0.1:8000)44