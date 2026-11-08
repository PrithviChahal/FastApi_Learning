from fastapi import FastAPI, Depends , Header , HTTPException

app = FastAPI()

def name():
    return{
    "Msg" : "Prithvi"
    }

@app.get("/name")
def getName(data = Depends(name)):
    return data

@app.get("/names")
def getName(data = Depends(name)):
    return data


def varifyToken(token:str = Header(None)):
    if token != "HelloWorld":
        raise HTTPException(
            status_code= 401,
            detail = "unauthorized User"
        )
    return {
        "Msg" : "Authorized User"

    }

@app.get("/secure-token")
def secureData(user = Depends(varifyToken)):
    return {
        "Msg" : "Secure Data Accessed ",
        "User" : user
    }