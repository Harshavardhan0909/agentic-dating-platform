# Local development

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Check `http://localhost:8000/health`. The API starts with 25 synthetic profiles. This branch is a runnable backend demo; a production deployment still needs a frontend hosting target and persistent database.
