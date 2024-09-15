# chat.py
import openai

openai.api_key = ""
openai.api_base = "https://api.pawan.krd/cosmosrp/v1"

AI_MODEL = "cosmosrp-8k"


def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model=AI_MODEL,
            messages=[{
                "role": "user",
                "content": prompt
            }],
        )
        return response.choices[0].message["content"]
    except Exception as e:
        raise Exception(f"Error: {e}")
