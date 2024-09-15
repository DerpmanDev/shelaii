import os
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
from chat import chat_with_gpt, AI_MODEL

console = Console()


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


def main():
    ai_name = load_ai_name()

    if ai_name is None:

        ai_name = Prompt.ask(
            "[bold cyan]What would you like to name your AI?[/bold cyan]")
        save_ai_name(ai_name)
        console.print("[bold green]Saved![/bold green]")
        clear_screen()
    else:
        console.print(
            f"[bold green]Using saved AI name:[/bold green] {ai_name}")
        clear_screen()

    # Title wiht a box around it
    title = Text.from_markup(
        "[bold magenta]Welcome to Shelaii![/bold magenta]")
    title.stylize("bold underline", 0, len(title))

    title_panel = Panel(title,
                        border_style="bold yellow",
                        title_align="center",
                        expand=False)

    model_panel = Panel(
        f"[bold blue]Currently using AI Model:[/bold blue] {AI_MODEL}",
        border_style="bold green",
        title="Model Information",
        title_align="left",
        expand=False)

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

            console.print(
                f"[bold yellow]{ai_name} is thinking...[/bold yellow]")
            response = chat_with_gpt(prompt)
            markdown = Markdown(response)
            console.print(markdown)

        except KeyboardInterrupt:
            # CTRL C
            confirm_exit = Prompt.ask(
                "[bold red]\nAre you sure you want to exit? [y/n][/bold red]",
                choices=["y", "n"],
                default="n")

            if confirm_exit.lower() == "y":
                console.print("[bold red]Exiting... Goodbye![/bold red]")
                break
            else:
                console.print("[bold green]Continuing...[/bold green]")


if __name__ == "__main__":
    main()
