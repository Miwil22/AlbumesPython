import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from data.db import obtener_albumes, crear_nuevo_album, obtener_album_por_id

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

@app.get("/albumes/new")
def form_nuevo_album(request: Request):
    return templates.TemplateResponse("albumes/album_form.html", {"request": request})

@app.post("/albumes/new")
async def guardar_album(request: Request):
    form = await request.form()
    crear_nuevo_album(
        nombre=form.get("nombre"),
        artista=form.get("artista"),
        genero=form.get("genero"),
        fecha=form.get("fecha_lanzamiento")
    )
    return RedirectResponse(url="/albumes", status_code=303)

@app.get("/albumes/{album_id}")
def ver_detalle(album_id: int, request: Request):
    album = obtener_album_por_id(album_id)
    
    if not album:
        return RedirectResponse(url="/albumes")
    
    return templates.TemplateResponse("albumes/album_detalle.html", {
        "request": request,
        "album": album
    })

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)