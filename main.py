<<<<<<< HEAD
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
res = {}

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/')
def render(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})

@app.post('/', response_class=HTMLResponse)
async def run(request: Request):
    data = await request.form()
    res.update(data)
    return templates.TemplateResponse("item.html", {"request": request.form, "data": data})
=======
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
>>>>>>> 94ce9c962cba14834ab7a0f83921acb2aee67a0f
