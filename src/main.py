from typing import Annotated
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Session, select

from models.album import Album, AlbumCreate, AlbumResponse, map_album_to_response, map_create_to_album
from data.db import get_session, init_db
from data.album_repository import AlbumRepository
from routers.api_albumes_router import router as api_albumes_router

import uvicorn

@asynccontextmanager
async def lifespan(application: FastAPI):
    init_db()
    yield

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(api_albumes_router)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/albumes", response_class=HTMLResponse)
async def ver_albumes(request: Request, session: SessionDep):
    repo = AlbumRepository(session)
    albumes = repo.get_all_albums()
    return templates.TemplateResponse("albumes/albumes.html", {"request": request, "albumes": albumes})
@app.get("/albumes/new", response_class=HTMLResponse)
async def nuevo_album_form(request: Request):

    """"Formulario para añadir un album nuevo"""
    return templates.TemplateResponse("albumes/album_form.html", {
        "request": request,
        "album": Album()
    })

@app.post("/albumes/new", response_class=HTMLResponse)
async def crear_album(request: Request, session: SessionDep):
    """Crear un nuevo album desde el formulario"""
    form_data = await request.form()
    nombre = form_data.get("nombre")
    artista = form_data.get("artista")
    genero = form_data.get("genero")
    fecha_lanzamiento = form_data.get("fecha_lanzamiento") or None
    
    album_create = AlbumCreate(
        nombre=nombre,
        artista=artista,
        genero=genero,
        fecha_lanzamiento=fecha_lanzamiento
    )
    repo = AlbumRepository(session)
    album = map_create_to_album(album_create)
    repo.create_album(album)

    return RedirectResponse(url="/albumes", status_code=303)

@app.get("/albumes/{album_id}", response_class=HTMLResponse)
async def album_por_id(album_id: int, request: Request, session: SessionDep):
    repo = AlbumRepository(session)
    album_encontrado = repo.get_album(album_id)
    if not album_encontrado:
        raise HTTPException(status_code=404, detail="Album no encontrado")
    album_response = map_album_to_response(album_encontrado)
    return templates.TemplateResponse("albumes/albumes_detalle.html", {
        "request": request,
        "album": album_response
    })

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)