# tarot

Tarot and astrological correspondence utilities by WitchMithras.

This package currently exposes helpers for decan lookup, tarot card selection,
and simple shuffled draws.

## Development

Create a virtual environment and install the package with development tools:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Run the test suite:

```powershell
python -m pytest
```

Run linting:

```powershell
python -m ruff check .
```
