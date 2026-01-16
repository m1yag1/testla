import click
from rich.console import Console

console = Console()


@click.command()
@click.version_option()
def main():
    """FOSS Test Case Management"""
    console.print("[bold green]Hello from testla![/bold green]")


if __name__ == "__main__":
    main()
