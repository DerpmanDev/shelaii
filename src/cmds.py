from functions import load_ai_name, save_ai_name
from rich.console import Console

console = Console()


def chgname(prompt):
  new_name = prompt
  save_ai_name(new_name)
  console.print(f'[blue]Updated name to[/blue] [yellow]"{new_name}!"[/yellow]')

  ai_name = load_ai_name()
  console.print(
      f"[bold green]{ai_name}:[/bold green] [yellow]How can I help you today?[/yellow]"
  )
