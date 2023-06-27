#   DEPENDENCIES:
#   # Python
#   from typing import Optional, List
#   from datetime import date
#   # Pydantic
#   from pydantic import BaseModel, Field

#   # From models.py for SQLalchemy:
from models.user import Users as UserModel
#   # From schemas.py for Pydantic:
from schemas.user import UserCreate # UserBase, , User   


class UserService():
    '''
    UserService Class
    
    This class contain a logic of the path operations for the object users
    
    ''' 
    def __init__(self, db) -> None:
        self.db = db
        
    
    def create_user(self, user: UserCreate):
        new_user = UserModel(**user.dict())
        # # Filtra aqui el Id y el Pass para aplicar las funciones y posteriormente ingresarlos a la data base:
        # # Pass
        # # new_user["password"] = generate_password_hash(self.data_user["password"], "pbkdf2:sha256:30", 30)  
        
        # # Agrega aqui el Id y listo
        # # Ultimo usuario:
        # last_id = self.db.query().all()
        # new_user["user_id"] = 0
        
              
        # self.db.add(new_user)
        # self.db.commit()
        return  new_user
    
        

