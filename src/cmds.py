import json
from .functions import save_ai_name, json_path
from rich.console import Console

console = Console()


def chgname(prompt):
    new_name = prompt
    save_ai_name(new_name)
    console.print(f'[blue]Updated name to[/blue] [yellow]"{new_name}!"[/yellow]')

    console.print(
        f"[bold green]{new_name}:[/bold green] [yellow]How can I help you today?[/yellow]"
    )


def chgmodel(type):
    with open(json_path, "r") as file:
        data = json.load(file)
        data["model-type"] = type
    with open(json_path, "w") as file:
        json.dump(data, file, indent=4)

    console.print(f"[bold cyan]Updated AI model to[/bold cyan] {type}")
