import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from database import obtener_albumes

app = FastAPI()

basedir = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=os.path.join(basedir, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(basedir, "templates"))

@app.get("/")
def ver_web(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "titulo": "Inicio - NEXUS"
    })

@app.get("/albumes") 
def ver_albumes(request: Request):
    lista_albumes = obtener_albumes()
    
    return templates.TemplateResponse("albumes/albumes.html", {
        "request": request,
        "albumes": lista_albumes
    })

@app.get("/api/info")
def ver_api():
    return {"mensaje": "API conectada a MySQL Localhost"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)