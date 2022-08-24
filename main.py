import json
from fastapi import FastAPI, File, UploadFile, Request,Form
from fastapi.staticfiles import StaticFiles
from modules import utils

import shutil
import os
import time

MEDIA_PATH = 'media'
WORDART_PATH = 'wordarts'

if not os.path.exists(MEDIA_PATH):
    os.mkdir(MEDIA_PATH)

if not os.path.exists(WORDART_PATH):
    os.mkdir(WORDART_PATH)


app = FastAPI()
app.mount("/static", StaticFiles(directory="wordarts"), name="static")


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    filepath = "media/"+file.filename
    wordarts_path = "wordarts/"
    try:
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception:
        return {"message": "There was an error uploading the file"}

    wordart_name, top_ten_kw = utils.wordify(file, filepath, wordarts_path)

    return {
            "Wordart": f"http://192.168.1.231:8001/static/{wordart_name}",
            "Top Ten Keywords": f"{top_ten_kw}"
            }