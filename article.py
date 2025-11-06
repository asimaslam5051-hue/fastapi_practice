from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import ArticleBase, ArticleDisplay
from typing import List
import db_article
from auth.oauth2 import oauth2_schema
from models import DbArticle
from auth.oauth2 import get_current_user,oauth2_schema
from db_user import   UserBase
router = APIRouter(
   prefix="/article",
   tags=["article"]
)

@router.post("/", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


@router.get("/{id}")#, response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return{

       "data":db_article.get_article(db, id),
       "current_user": current_user
    }
