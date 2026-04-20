"""Tests for nightowlcli.funky."""

import pytest

from nightowlcli.funky import get_funky


def test_get_funky_prints_funk_level(capsys: pytest.CaptureFixture[str]) -> None:
    """get_funky should print the supplied funk level."""
    get_funky("test")
    captured = capsys.readouterr()
    assert captured.out == "Turning the funk up to test\n"


def test_get_funky_default_level(capsys: pytest.CaptureFixture[str]) -> None:
    """get_funky works with the canonical default funk level."""
    get_funky("white guy at a wedding")
    captured = capsys.readouterr()
    assert "white guy at a wedding" in captured.out


def test_get_funky_empty_string(capsys: pytest.CaptureFixture[str]) -> None:
    """get_funky handles an empty string without raising."""
    get_funky("")
    captured = capsys.readouterr()
    assert "Turning the funk up to" in captured.out


@pytest.mark.parametrize(
    "level",
    ["low", "medium", "🎸 max overdrive", "100"],
)
def test_get_funky_various_levels(
    capsys: pytest.CaptureFixture[str], level: str
) -> None:
    """get_funky echoes any funk level correctly."""
    get_funky(level)
    captured = capsys.readouterr()
    assert level in captured.out
