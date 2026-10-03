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
    final_prompt = f"""
    {system_context}
         Important: Do not use any markdown symbols like * or # in your response. Give plain text.
    Student Question: {user_question}
    """
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=final_prompt,
         config={
            "system_instruction": """
            You are an expert academic teaching assistant exclusively for Digital Communication. 
            Follow these rules strictly:
            1. If the student's question is NOT about Digital Communication (e.g., other subjects, general topics, or unrelated queries), you must reply: "I cannot find this information in the course materials."
            2. If the student's question IS about Digital Communication:
               - First, check the provided reference course context. If the answer is found there, use it.
               - If the answer is NOT found in the course context, use your expert general engineering knowledge to provide an accurate and helpful answer about Digital Communication.
            """
        }
        )
        
        return response.text
    except Exception as e:
        return f"Error communicating with AI provider: {str(e)}"