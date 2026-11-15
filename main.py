from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get ("/inicio")
def inicio():
     return{"mensaje":"hola desde fastAPI"}
  
class Users(BaseModel):
    id:int
    name:str
    age:int

users_db=[Users(id=1,name="pepe",age=19),Users(id=2,name="laura",age=22),Users(id=3,name="diego",age=25)]

@app.get("/users")
def users():
     return users_db

 