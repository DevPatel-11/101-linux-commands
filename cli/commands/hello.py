import typer

app = typer.Typer(help="Hello command group")


@app.command()
def greet(name: str = "World") -> None:
    """Say hello to someone."""
    typer.echo(f"Hello, {name}!")
