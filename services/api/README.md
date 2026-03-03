# API Service

This fodler contains the backend API build with FastAPI.

We keep the API in `services\api` so the repository can later support additional services
(e.g., Next.js frontend in `web/`) while staying organized.


# 🧠 Why app/?

We separate:

```bash
services/api/
    app/   ← actual FastAPI application code
```

This allows:

- Dockerfile to stay clean

- Alembic config to live alongside app

- Future scaling (multiple services possible)

- Clear separation between infrastructure and application logic
 
# 🧠 Why __init__.py?

This makes app a Python package.

That allows imports like:

```bash
from app.main import app
```

Without it, Python wouldn’t treat app/ as a module.