from sqlalchemy.orm import Session
from models import DbUser
from schemas import UserBase
from hash import Hash
from fastapi import HTTPException, status

#  Create User
def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        Email=request.Email,
        password=Hash.bcrypt(request.password)   
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


#  Get all users
def get_all_users(db: Session):
    return db.query(DbUser).all()


#  Get single user by ID
def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"User with username {username} not found")
    return user


#  Update user
def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    user.username = request.username
    user.email = request.email
    user.password = Hash.bcrypt(request.password)   # update ke time bhi hash karna hoga

    db.commit()
    db.refresh(user)
    return user


#  Delete user
def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}