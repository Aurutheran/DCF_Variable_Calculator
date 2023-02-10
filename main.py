from fastapi import FastAPI
from starlette.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

stored_data = {}

class Data(BaseModel):
    id: str
    value: str

@app.post("/store_data")
async def store_data(data: Data):
    stored_data[data.id] = data.value
    return {"message": "Data stored successfully"}

@app.get("/delete/{id}")
async def delete_form(request, id: str):
    with open("templates/delete.html", "r") as file:
        content = file.read().format(id=id)
        return HTMLResponse(content=content, status_code=200)

@app.post("/delete/{id}")
async def delete_data(id: str):
    if id in stored_data:
        del stored_data[id]
        return {"message": "Data deleted successfully"}
    else:
        return {"message": "Data not found"}
