from fastapi import FastAPI
import models
from database import engine
from  mangum import Mangum
from authentication import router as authentication_router
from user import router as user_router
from article import router as article_router
from product import router as product_router
from file import router as file_router
from blog_post import router1, router2, router3, router4
from item import router as item_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="FastAPI on Vercel")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

@app.get("/hello")
def index():
    return {"message": "Hello World!"}

models.Base.metadata.create_all(bind=engine)
app.mount('/files',StaticFiles(directory = "files"), name = "files")





@app.get("/")
def root():
    return{"Message":"hello FastAPI on vercel"}

handler = Mangum(app)


