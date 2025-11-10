import sys
from pathlib import Path

# Add project root to sys.path so imports work
sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from mangum import Mangum

# Import your modules
import models
from database import engine
from authentication import router as authentication_router
from user import router as user_router
from article import router as article_router
from product import router as product_router
from item import router as item_router
from file import router as file_router
from blog_post import router1, router2, router3, router4

app = FastAPI(title="FastAPI on Vercel")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(file_router)
app.include_router(authentication_router)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(article_router)
app.include_router(item_router)
app.include_router(router1)
app.include_router(router2)
app.include_router(router3)
app.include_router(router4)

# Static files
app.mount('/files', StaticFiles(directory="files"), name="files")

# Database setup
models.Base.metadata.create_all(bind=engine)

# Routes
@app.get("/hello")
def index():
    return {"message": "Hello World!"}

@app.get("/")
def root():
    return {"message": "Hello FastAPI on Vercel"}

# Mangum handler for Vercel
handler = Mangum(app)
