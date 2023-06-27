from fastapi import APIRouter, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse




user_router = APIRouter()

template = Jinja2Templates(directory='./templates')



##--------------------------- ROUTERS & CRUD ---------------------------## 

@user_router.get(path='/signup',
                 response_class=HTMLResponse,
                 status_code=status.HTTP_202_ACCEPTED,
                 summary="Create a User in the App",
                 tags=["Users"])
def signup_user(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})
