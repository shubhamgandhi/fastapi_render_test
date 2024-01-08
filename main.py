from typing import Optional
from fastapi import FastAPI
from nicegui import ui
from matplotlib import pyplot as plt
import numpy as np
import random


app = FastAPI()


@app.get("/")
async def root():
    ui.label('Clairvoyance').style('color: #6E93D6; font-size: 200%; font-weight: 300')
    ui.run(on_air=False)
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
