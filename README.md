# play-pydantic-ai
Experimenting with pydantic-ai

## Development

### Initial Setup
For new developers setting up this project:

1. **Install UV** (if not already installed):
   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository**:
   ```sh
   git clone git@github.com:mapa17/play-pydantic-ai.git
   cd play-pydantic-ai
   ```

3. **Initialize the project**:
   ```sh
   uv sync
   ```
   This will:
   - Create a virtual environment in `.venv/` using Python 3.13
   - Install all dependencies (including dev dependencies like pytest)
   - Install the project in development mode

4. **Verify the setup**:
   ```sh
   uv run play-pydantic-ai
   ```

### Running the Application
```sh
# Run via CLI entry point
uv run play-pydantic-ai

# Run as a module
uv run python -m play_pydantic_ai.main
```

### Testing
Use uv to run pytest + coverage
```sh
uv run pytest
```