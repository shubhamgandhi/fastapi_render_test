from typing import Optional
from fastapi import FastAPI
from nicegui import ui, app
from matplotlib import pyplot as plt
import numpy as np
import random

def init(fastapi_app: FastAPI) -> None:
    @ui.page('/show')
    def show():
        ui.label('Hello, FastAPI!')

        # NOTE dark mode will be persistent for each user across tabs and server restarts
        ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
        ui.checkbox('dark mode').bind_value(app.storage.user, 'dark_mode')

    ui.run_with(
        fastapi_app,
        storage_secret='pick your private secret here',  # NOTE setting a secret is optional but allows for persistent storage per user
    )

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


frontend.init(app)

if __name__ == '__main__':
    print('Please start the app with the "uvicorn" command as shown in the start.sh script')
