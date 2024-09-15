import os


def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')


def load_ai_name():
  if os.path.exists('ainame.txt'):
    with open('ainame.txt', 'r') as file:
      return file.read().strip()
  return None


def save_ai_name(name):
  with open('ainame.txt', 'w') as file:
    file.write(name)
