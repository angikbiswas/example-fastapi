from .database import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

class  post(Base):
    __tablename__= "posts"
    id= Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    title= Column(String, nullable=False)
    content= Column(String, nullable=False)
    published= Column(Boolean, server_default='TRUE', nullable=False)
    created_at= Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id= Column(Integer,ForeignKey("users.id",ondelete="CASCADE"), nullable=False)

    owner= relationship("user")

class user(Base):
    __tablename__="users"
    id= Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    email=Column(String, nullable=False, unique=True)
    password= Column(String,nullable=False)
    created_at= Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone_number= Column(String)

class Votes(Base):
    __tablename__="votes"

    users_id= Column(Integer,ForeignKey("users.id",ondelete="CASCADE"), primary_key=True)
    posts_id= Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"), primary_key=True)
