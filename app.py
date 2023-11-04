from fastapi import FastAPI
from pydantic import BaseModel
from main import Main

class Item(BaseModel):
    title: str


app = FastAPI()
obj=Main()

@app.get("/")
def read_root():
    return {"msg":"Welcome to the app!"}


@app.post("/recommendations")
async def create_item(item: Item):
    res=obj.search(item.title)
    return res

