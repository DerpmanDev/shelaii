# chat.py
from g4f.client import Client
from .functions import load_ai_name

user = load_ai_name()

AI_MODEL = "gpt-3.5-turbo"

def chat_with_gpt(prompt):
    client = Client()
    try:
        response = client.chat.completions.create(
            model=AI_MODEL,
            messages=[{
                "role": "user",
                "content": prompt
            }],
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error: {e}")
