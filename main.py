from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from modules import prepocess as pp
from modules import generate as gen
import shutil

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/hello", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "id": 500})


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})

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
        print(words)
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
            # "Wordart": f"http://0.0.0.0:8001/{wordart_name}",
            "Top Ten Keywords": f"{top_ten_kw}"
            }



