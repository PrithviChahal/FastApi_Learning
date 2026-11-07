from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {"Message": "Hello world"}


# User Route
@app.get("/user/{user_id}")
def users(user_id:int):
    return {
        "User" : user_id
    }

# Query params
@app.get("/products")
def products(limit : int = 18):
    return {
        "Limit" : limit
    }

# Multiple query params
@app.get("/info")
def info(name : str = None, age : int = 0):
    return{
        "Name" : name,
        "Age" : age
    }


# PostApi Method 1 without validation
@app.post("/createUserM1")
def createUserM1(user:dict):
    return{
        "Message":"User Created",
        "Data": user
    }


# Method 2 with validation
@app.post("/createUserM2")
def createUserM2(name:str,age:int):
    return{
        "Message":"User Created",
        "Name":name,
        "Age":age
    }

# Method 3
class User(BaseModel):
    name:str
    age:int

@app.post("/createUserM3")
def createuserM3(user:User):
    return{
        "Message": "User Created",
        "Data": user
    }    


# Nested pydantic models
class Address(BaseModel):
    city: str
    pincode:int

class Employee(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/Employee")
def Employee(employee:Employee):
    return{
        "Msg":"Employee created",
        "Employee": employee
    }        