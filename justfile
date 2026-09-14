set shell := ["bash", "-eu", "-o", "pipefail", "-c"]
export UV_PROJECT_ENVIRONMENT := env_var("HOME") + "/.venvs/iliad"

default:
    @just --list

# Install exactly the recorded Python dependencies into WSL's Linux filesystem.
env:
    uv sync --locked

render:
    quarto render
    uv run --locked python scripts/check_render.py

preview:
    quarto preview --no-browser

check:
    uv run --locked python derivations/check_environment.py

# Add notes pages for newly listed worksheets, preserving existing attempts.
worksheets:
    uv run --locked python scripts/scaffold_worksheets.py
