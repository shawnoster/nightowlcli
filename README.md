# nightowlcli

```
  ___    
 (o,o)   Night Owl CLI
 {`"'}   A modern Python 3.13+ CLI skeleton
 -"-"-
```

## what?

A bare-bones CLI skeleton using current (2025) Python best practices — `uv` for
package management, `Typer` for the CLI, `ruff` for linting/formatting, and
`pytest` for tests. Clone, rename, delete `funky.py`, and ship.

## in the box

- **Python 3.13+**
- **[uv](https://docs.astral.sh/uv/)** – fast package manager and project tool
- **[Typer](https://typer.tiangolo.com/)** – CLI framework built on Click, driven by type hints
- **[ruff](https://docs.astral.sh/ruff/)** – linter + formatter (replaces flake8, black, isort)
- **[pytest](https://pytest.org/)** – testing framework with coverage via pytest-cov
- `pyproject.toml` only – no `setup.py`, no `requirements.txt`

## folder structure

```
nightowlcli/
├── README.md
├── pyproject.toml          # project metadata, deps, tool config
├── .python-version         # pins Python 3.13 for uv
├── LICENSE
├── nightowlcli/            # the package
│   ├── __init__.py
│   ├── __main__.py         # CLI entry point (Typer app)
│   ├── funky.py            # example module — replace with your code
│   └── errors.py           # custom exceptions
└── test/
    ├── __init__.py
    └── test_funky.py       # pytest tests
```

## how?

### install uv (one-time)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### set up the project

```bash
# install deps and create .venv automatically
uv sync --dev

# run the CLI
uv run nightowlcli
uv run nightowlcli funky "disco inferno"
uv run nightowlcli --help
```

### run tests

```bash
uv run pytest
uv run pytest --cov=nightowlcli   # with coverage
```

### lint and format

```bash
uv run ruff check .       # lint
uv run ruff format .      # format
uv run ruff check --fix . # auto-fix lint issues
```

## make it yours

1. Rename the root folder and the `nightowlcli/` package folder to your project name.
2. Update `pyproject.toml` — name, version, description, author, URLs.
3. Delete `funky.py` and `test/test_funky.py`, add your own modules and tests.
4. Update this `README.md`.

## don't forget to...

- Replace `LICENSE` with your preferred license and update `pyproject.toml` to match.
- Add your real dependencies under `[project] dependencies` in `pyproject.toml`.
- Run `uv lock` after changing dependencies to update `uv.lock`.
- Pin the right Python version in `.python-version` if 3.13 isn't what you need.
