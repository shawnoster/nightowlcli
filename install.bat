@echo off
REM Quick dev install using uv.
REM Run this from the project root.

where uv >nul 2>&1
if %errorlevel% neq 0 (
    echo uv not found - installing...
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
)

uv sync --dev
echo.
echo Done! Try:
echo   uv run nightowlcli --help
