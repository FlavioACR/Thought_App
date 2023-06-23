from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    
    user_id   : int = Field(...)
    username  : str = Field(...,
                            min_length=3,
                            max_length=15)
    first_name: str = Field(...,
                            min_length=1,
                            max_length=50)
    last_name : str = Field(...,
                            min_length=1,
                            max_length=50)
    birth_date: Optional[date] = Field(default=None)
    gender    : str = Field(...)
    
class UserPassword(BaseModel):
    email     : str = Field(...)    

class UserEmail(BaseModel):
    password: str = Field(...,
                          min_length=5,
                          max_length=25)

class UserLogin(UserPassword, UserEmail):
    pass
    
class User(UserBase, UserEmail):
    pass
    
class UserCreate(User, UserLogin):
    pass
