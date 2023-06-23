from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Date ,ForeignKey
from sqlalchemy.orm import relationship


class Users(Base):
  '''
  This class is a model User to use for the user table
  '''
   
  __tablename__ = "users"
   
  user_id    = Column(Integer, primary_key=True, index=True, autoincrement=True)
  username   = Column(String, nullable=False)
  email      = Column(String, unique=True, nullable=False)
  first_name = Column(String, nullable=False) 
  last_name  = Column(String, nullable=False)
  birth_date = Column(Date, nullable=False)
  gender     = Column(String, nullable=False)
  password   = Column(String(255), nullable=False)   
   
  # Relations
  # thougths_relationship = relationship("Thought", back_populates="users_relationship")
  # questions_relationship = relationship("Questions", back_populates="users_relationship")