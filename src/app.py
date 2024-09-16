from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
from .chat import chat_with_gpt, AI_MODEL
from .cmds import *
from .functions import clear_screen, load_ai_name, save_ai_name, json_path

console = Console()

if AI_MODEL is None:
    AI_MODEL = "gpt-3.5-turbo"


def main():
    ai_name = load_ai_name()

    if ai_name is None:

        ai_name = Prompt.ask(
            "[bold cyan]What would you like to name your AI?[/bold cyan]"
        )
        save_ai_name(ai_name)
        console.print("[bold green]Saved![/bold green]")
        clear_screen()
    else:
        console.print(f"[bold green]Using saved AI name:[/bold green] {ai_name}")
        clear_screen()

    # Title wiht a box around it
    title = Text.from_markup(
        f'[bold underline magenta]Welcome to Shelaii![/bold underline magenta]\nType "help" for a list of commands.'
    )
    title_panel = Panel(
        title, border_style="bold purple", title_align="center", expand=False
    )

    model_panel = Panel(
        f"[bold blue]Currently using AI Model:[/bold blue] {AI_MODEL}",
        border_style="bold green",
        title="Model Information",
        title_align="left",
        expand=False,
    )

    console.print(title_panel)
    console.print(model_panel)
    console.print(
        f"[bold green]{ai_name}:[/bold green] [yellow]How can I help you today?[/yellow]"
    )

    while True:
        try:
            prompt = Prompt.ask("[bold green]You[/bold green]")

            if prompt.lower() == "exit":
                console.print("[bold red]Goodbye![/bold red]")
                break

            if prompt.lower().startswith("chgname "):
                chgname(prompt[8:].strip())
                continue

            if prompt.lower().startswith("chgmodel "):
                chgmodel(prompt[9:].strip())
                continue

            if prompt.lower() != "help":

                with open(json_path, "r") as file:
                    data = json.load(file)
                    ai_name = data["ai-name"]
                    # Loading JSON everytime cause name var doesn't update if changed
                console.print(f"[yellow]{ai_name} is thinking...[/yellow]")
                response = chat_with_gpt(prompt)
                markdown = Markdown(response)
                console.print(markdown)
            else:
                command_list = "[bold yellow]chgname[/bold yellow] - Change the name of your AI\n[bold yellow]chgmodel[/bold yellow] - Change your AI model"
                help_panel = Panel(
                    f"{command_list}",
                    title="Command Menu",
                    border_style="bold cyan",
                    title_align="center",
                    expand=False,
                )
                console.print(help_panel)

        except KeyboardInterrupt:
            # CTRL C
            confirm_exit = Prompt.ask(
                "[bold red]\nAre you sure you want to exit? [y/n][/bold red]",
                choices=["y", "n"],
                default="n",
            )

            if confirm_exit.lower() == "y":
                console.print("[bold red]Exiting... Goodbye![/bold red]")
                break
            else:
                console.print("[bold green]Continuing...[/bold green]")
