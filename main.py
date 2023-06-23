from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.database import engine, Base 
# Routers
from routers.user import user_router


app = FastAPI()
app.title = "My Thoughts APP with FastAPI"
app.version = "0.0.1"

# Plantillas HTML
template = Jinja2Templates(directory='./templates')

# Declaración de la carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

Base.metadata.create_all(bind=engine)
