# Global Smart Zone - Backend

This directory contains the FastAPI backend for Global Smart Zone.

Quick start (development):

1. Copy `.env.example` to `.env` and set values.
2. Create a virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Run the app:

```bash
uvicorn app.main:app --reload
```
