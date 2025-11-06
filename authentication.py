from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session

import models
from hash import Hash
from database import get_db
from auth import oauth2

router = APIRouter(
    tags=['authentication']
)

@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(models.DbUser.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

    access_token = oauth2.create_access_token(data={"sub": user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }
    