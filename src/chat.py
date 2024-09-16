# chat.py
import json
from g4f.client import Client
from .functions import load_ai_name, load_ai_model, json_path

user = load_ai_name()
AI_MODEL = load_ai_model()

if AI_MODEL is None:
    with open(json_path, "r") as file:
        data = json.load(file)

    data["model-type"] = "gpt-3.5-turbo"

    with open(json_path, "w") as file:
        json.dump(data, file, indent=4)


def chat_with_gpt(prompt):
    client = Client()
    # loading this everytime so model updates without restarting
    with open(json_path, "r") as file:
        data = json.load(file)

    try:
        response = client.chat.completions.create(
            model=data["model-type"],
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error: {e}")
