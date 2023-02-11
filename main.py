from fastapi import FastAPI, Request, Form
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

@app.post('/')
async def run(request: Request):
    data = await request.form()
    res.update(data)
    print(data)
    return templates.TemplateResponse("item.html", {"request": request, "data": data})

@app.get('/getval')
def val():
    return {"results": res}