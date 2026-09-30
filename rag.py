import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

def load_context_file(filepath="subject_context.md"):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return "You are a helpful academic teaching assistant."

def generate_teaching_response(user_question: str) -> str:
    system_context = load_context_file()
    prompt = f"""
    {system_context}

    Student Question: {user_question}
    """
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error communicating with AI provider: {str(e)}"