"""Custom exceptions for Night Owl CLI.

All exceptions raised by this package are defined here so callers can
import a single module to handle errors cleanly.
"""


class NightOwlError(Exception):
    """Base exception for all Night Owl CLI errors."""


class ConfigError(NightOwlError):
    """Raised when a configuration value is missing or invalid."""


class CommandError(NightOwlError):
    """Raised when a CLI command fails due to bad input or state."""
