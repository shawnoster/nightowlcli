#!/usr/bin/env bash
# Quick dev install using uv.
# Run this from the project root: bash install.sh
set -euo pipefail

if ! command -v uv &>/dev/null; then
    echo "uv not found – installing..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

uv sync --dev
echo ""
echo "Done! Try:"
echo "  uv run nightowlcli --help"
