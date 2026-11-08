from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
Users = []

class UserCreate(BaseModel):
    name:str
    age:int
    password:str

class UserResponse(BaseModel):
    name:str
    age:int

@app.get("/users", response_model= list[UserResponse])
def getUsers():
    return Users

@app.post("/users")
def registerUser(user:UserCreate):
    Users.append(user)
    return{
        "Msg":"User Registered",
        "Data": user
    }

