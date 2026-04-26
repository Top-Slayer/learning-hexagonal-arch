if ! command -v uv > /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

uv sync
uv run python -m compileall src # check compile time
uv run python -m uvicorn main:app --reload --app-dir src
