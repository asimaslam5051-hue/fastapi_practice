# api/index.py
from mangum import Mangum
from main import app  # import your FastAPI app from main.py

# Wrap FastAPI app in Mangum so it works with Vercel (AWS Lambda style)
handler = Mangum(app)
