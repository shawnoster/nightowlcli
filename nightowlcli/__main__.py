"""Night Owl CLI entry point."""

from typing import Annotated

import typer

from .funky import get_funky

app = typer.Typer(help="Night Owl CLI – a Python CLI skeleton.")


@app.command()
def funky(
    funk_level: Annotated[
        str,
        typer.Argument(help="The level of funk to bring to the party."),
    ] = "white guy at a wedding",
) -> None:
    """Turn up the funk to FUNK_LEVEL."""
    get_funky(funk_level)


def main() -> None:
    """Entry point – delegates to the Typer app for CLI argument parsing."""
    app()


if __name__ == "__main__":
    main()
