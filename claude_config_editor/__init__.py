"""
Claude Config Editor - Web-based editor for Claude configurations
Supports both Claude Code (.claude.json) and Claude Desktop (claude_desktop_config.json)
"""

__version__ = "1.0.0"
__author__ = "SijanC147"

from .server import main

__all__ = ["main", "__version__"]
