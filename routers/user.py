from fastapi import APIRouter, Request, status, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from services.user import UserService
from config.database import Session
#   From models.py for SQLalchemy:
from models.user import Users as UserModel
#   From schemas.py for Pydantic:
from schemas.user import UserCreate # UserBase, , User


# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field
# FastAPI
from fastapi import FastAPI, Request, Response, Form, APIRouter, Depends, Path, Query, status, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
# From apps modules: #   config.py:
from config.database import Session
# From models.py for SQLalchemy:
from models.user import Users as UserModel
# From schemas.py for Pydantic:
from schemas.user import UserBase, UserCreate, User
from services.user import UserService


user_router = APIRouter()

template = Jinja2Templates(directory='./templates')

##--------------------------- ROUTERS & CRUD ---------------------------## 

@user_router.get(path='/login',
                 response_class=HTMLResponse,
                 status_code=status.HTTP_202_ACCEPTED,
                 summary="Page to login a user in the app",
                 tags=["Users"])
def login_user(req: Request):
    return template.TemplateResponse("login.html", {"request": req})


@user_router.get(path='/signup',
                 response_class=HTMLResponse,
                 status_code=status.HTTP_202_ACCEPTED,
                 summary="Create a User in the App",
                 tags=["Users"])
def signup_user(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})


@user_router.post(path='/creating_user',
                  response_model=User,
                  status_code=status.HTTP_201_CREATED,
                  summary="Sign Up a new user in the app",
                  tags=["users"])
def create_user(user: UserCreate):
    # Necesito cambiar la esctructura para devolver el formulario conectado al html.
    """"
    Create_user:
    
    This path operation register a user in the app
    
    Parameters: 
    
         - Request body parameter
            - user: UserCreate 
    
    Returns a successfull registered message
    
        - message: The user has successfully registered
    """
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "The user has successfully registered"})


# @user_router.post(path="/creating_user",
#                   response_class=HTMLResponse,
#                   status_code=status.HTTP_201_CREATED,
#                   summary="Procesin the data input to create a user",
#                   tags=["Users"])
# def creating_user(username: str = Form(),
#                   email: str = Form(),
#                   first_name: str = Form(),
#                   last_name: str = Form(),
#                   birth_date: str = Form(),
#                   gender: str = Form(),
#                   password: str = Form()):
    
#     new_user_data = {
#         "username": username,
#         "email": email,
#         "first_name": first_name,
#         "last_name": last_name,
#         "birth_date": birth_date,
#         "gender":gender,
#         "password":password
#     }

#     # Sesion DB
#     db = Session()
#     # Llamar al servicio de creación, usar un metodo y pasar al metodo como parametro los datos del usuario.
#     UserService(db).create_user(new_user_data)
    