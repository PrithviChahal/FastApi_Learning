from fastapi import FastAPI , status ,HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/create_post", status_code= status.HTTP_400_BAD_REQUEST)
def create_user():
    return{
        "Msg":"User created"
    }

# Custom Response
@app.get("/posts")
def getPosts():
    return{
        "status": "Success",
        "Message": "User_Fatched",
        "Data":{
            "Name":"Prithvi",
            "Age":25
        }

    }


# Error Handling
@app.get("/users/{user_id}")
def getusers(user_id:int):
    if user_id != 1:
        return HTTPException(
            status_code= 404,
            detail= "User not found"
        )
    return{
        "UserID": user_id,
        "Name":"Prithvi"
    }


# custom Exception
class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def userNotFoundHandler(request:Request, exc:UserNotFoundException):
    return JSONResponse(
        status_code= 404,
        content={
            "Status":"Error",
            "Msg":f"User {exc.name} not found"
        }

    )        

@app.get("/userName/{name}")
def getusers(name:str):
    if name != "Prithvi":
        raise UserNotFoundException(name)
    return{
        "Name": name
    }        