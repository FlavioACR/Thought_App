from fastapi import FastAPI, status, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.database import database_engine, Base 
# Routers
from routers.user import user_router


app = FastAPI()
app.title = "My Thoughts APP with FastAPI"
app.version = "0.0.1"

# Plantillas HTML
template = Jinja2Templates(directory='./templates')

# Declaración de la carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

Base.metadata.create_all(bind=database_engine)

# Principal base template this is only to create the SuperTemplate:
@app.get(
    path='/',
    status_code=status.HTTP_200_OK,
    summary="Welcome page to the users",
    tags=['Home'])
def home_page(request: Request):
    '''
    Welcome pages  & Hello World FastAPI 

    This path operation is the welcome to new and old users in the app

    '''
    return template.TemplateResponse('welcome_page.html', {"request": request})

# ROUTERS:
app.include_router(user_router)