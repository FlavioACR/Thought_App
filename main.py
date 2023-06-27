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
    summary="Home's app and Hello World",
    tags=['home'])
def home_page(request: Request):
    '''
    Home's app & Hello World FastAPI 

    This path operation say hellow to everybody user in the app

    Parameters: Nothing
    
    Returns   : A json with the greeting information
    '''
    return template.TemplateResponse('welcome_page.html', {"request": request})

