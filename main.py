from fastapi import FastAPI, File, UploadFile, Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from modules import prepocess as pp
from modules import generate as gen
import shutil
import os

MEDIA_PATH = 'media'
WORDART_PATH = 'wordarts'

if not os.path.exists(MEDIA_PATH):
    os.mkdir(MEDIA_PATH)

if not os.path.exists(WORDART_PATH):
    os.mkdir(WORDART_PATH)


app = FastAPI()
templates = Jinja2Templates(directory="templates")
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

    
    try:
        text = pp.extract_text(filepath)
        text = pp.clean_text(text)
        words = pp.process_text(text)
        # print(words)
        wordlist, top_ten_kw = gen.get_keywords(words)
    except Exception:
        return {"message": "There was an error while generating keywords"}
        
    try:
        wordart = gen.get_wordart(wordlist)
        wordart_name = file.filename.split('.')[0] + '.png'
        wordart.to_file(wordarts_path + wordart_name)
    except Exception:
        return {"message": "There was an error while generating wordart"}

    return {
            "Wordart": f"http://192.168.1.231:8001/static/{wordart_name}",
            "Top Ten Keywords": f"{top_ten_kw}"
            }



