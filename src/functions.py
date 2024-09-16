import os
import json

json_path = "src/data/ai-data.json"


def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')


def check_ai_data():
  if not os.path.exists(json_path):
    print(f"{json_path} does not exist. Creating a new one.")
    with open(json_path, 'w') as file:
      json.dump({}, file, indent=4)
    return

  if os.stat(json_path).st_size == 0:
    print(f"{json_path} is empty. Resetting to an empty JSON.")
    with open(json_path, 'w') as file:
      json.dump({}, file, indent=4)
    return

  try:
    with open(json_path, 'r') as file:
      json.load(file)
  except json.JSONDecodeError:
    print(f"{json_path} is corrupted. Resetting to an empty JSON.")
    with open(json_path, 'w') as file:
      json.dump({}, file, indent=4)


check_ai_data()


def load_ai_name():
  if os.path.exists(json_path):
    with open(json_path, 'r') as file:
      data = json.load(file)
      return data.get("ai-name", None)


def save_ai_name(name):
  if os.path.exists(json_path):
    with open(json_path, 'r') as file:
      try:
        data = json.load(file)
      except json.JSONDecodeError:
        data = {}
  else:
    data = {}

  data["ai-name"] = name

  with open(json_path, 'w') as file:
    json.dump(data, file, indent=4)


# -


def load_ai_model():
  if os.path.exists(json_path):
    with open(json_path, 'r') as file:
      data = json.load(file)
      return data.get("model-type", None)
