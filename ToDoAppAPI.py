from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class ToDo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def create_todo(todo:ToDo):
    todos.append(todo)
    return{
        "Msg":"ToDo Added",
        "Data": todo
    }

@app.get("/todos")
def getTodos():
    return todos

@app.get("/todo/{todo_id}")
def getTodo(todo_id:int):
    for i in todos:
        if i.id == todo_id:
            return i
    return {"Error":f"ToDo id {todo_id} is not found"}    


@app.put("/todos/{todo_id}")
def updateTodo(todo_id:int,updatedtodo:ToDo):
    for index,i in enumerate(todos):
        if i.id == todo_id:
            todos[index] = updatedtodo
            return{
                "Msg":"Data Updated Successfully...",
                "Data": updatedtodo
            }
    return {"Error":f"ToDo id {todo_id} is not found"}

@app.delete("/todos/{todo_id}")
def deleteToDo(todo_id:int):
    for index,i in enumerate(todos):
        if i.id == todo_id:
            todos.pop(index)
            return{
                "Msg":"Data Deleted Successfully..."
            }
    return {"Error":f"ToDo id {todo_id} is not found"}    

