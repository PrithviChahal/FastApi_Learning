from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

Users = []

class User(BaseModel):
    name:str
    age:int


@app.post("/users")
def create_user(user:User):
    Users.append(user)
    return{
        "Msg":"User Created",
        "Data": user
    }  

@app.put("/users/{user_id}")
def updateUser(user_id:int,user:User,notify:bool=False):
    if user_id < len(Users):
        Users[user_id] = user
        return{
            "Msg":"User Updated...",
            "Notify":notify,
            "Data": user
        }
    return{
        "Msg":"User not found"
    }

@app.get("/users")
def getUsers():
    return Users

