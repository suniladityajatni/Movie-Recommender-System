# from fastapi import FastAPI
# from pydantic import BaseModel
# from main import Main

# class Item(BaseModel):
#     title: str


# app = FastAPI()
# obj=Main()

# @app.get("/")
# def read_root():
#     return {"msg":"Welcome to the app!"}


# @app.post("/recommendations")
# async def create_item(item: Item):
#     res=obj.search(item.title)
#     return res



# main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from main import Main

app = FastAPI()
obj=Main()

# Create an instance of Jinja2Templates for rendering HTML templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/rec")
async def process_input(text: str = Form(...)):
    res=obj.search(text)
    return {"movies": res}
