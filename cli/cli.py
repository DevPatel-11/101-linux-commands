import typer
from commands import hello

# Create the root CLI app
app = typer.Typer(help="101 Linux Commands CLI 🚀")

# Register subcommands
# Typer commands should have typed arguments
# (Typer uses them for automatic parsing and help docs)
app.add_typer(hello.app, name="hello")

def main() -> None:
    """CLI entry point."""
    app()

if __name__ == "__main__":
    app()
