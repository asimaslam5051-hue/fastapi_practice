from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    # One-to-many: a user can have many articles
    articles = relationship("DbArticle", back_populates="user")


class DbArticle(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Back reference to DbUser
    user = relationship("DbUser", back_populates="articles")

