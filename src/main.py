from typing import Annotated
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Session

from models.album import Album, AlbumCreate, map_album_to_response, map_create_to_album
from data.db import init_db, get_session
from data.album_repository import AlbumRepository
from routers.api_albumes_router import router as api_albumes_router

import uvicorn

@asynccontextmanager
async def lifespan(application: FastAPI):
    try:
        init_db()
    except Exception as e:
        print(f"Advertencia crítica: {e}")
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
    return templates.TemplateResponse("albumes/album_form.html", {
        "request": request,
        "album": None
    })

@app.post("/albumes/new", response_class=HTMLResponse)
async def crear_album(request: Request, session: SessionDep):
    form_data = await request.form()
    
    fecha = form_data.get("fecha_lanzamiento")
    if not fecha: fecha = None

    album_create = AlbumCreate(
        nombre=form_data.get("nombre"),
        artista=form_data.get("artista"),
        genero=form_data.get("genero"),
        fecha_lanzamiento=fecha
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
        return RedirectResponse(url="/albumes")
        
    return templates.TemplateResponse("albumes/album_detalle.html", {
        "request": request, 
        "album": album_encontrado
    })


@app.get("/albumes/delete/{album_id}")
async def borrar_album_web(album_id: int, session: SessionDep):
    repo = AlbumRepository(session)
    repo.delete_album(album_id)
    return RedirectResponse(url="/albumes", status_code=303)

@app.get("/albumes/edit/{album_id}", response_class=HTMLResponse)
async def editar_album_form(album_id: int, request: Request, session: SessionDep):
    repo = AlbumRepository(session)
    album = repo.get_album(album_id)
    if not album:
        return RedirectResponse(url="/albumes")
    
    return templates.TemplateResponse("albumes/album_form.html", {
        "request": request,
        "album": album
    })

@app.post("/albumes/edit/{album_id}")
async def actualizar_album_web(album_id: int, request: Request, session: SessionDep):
    form_data = await request.form()
    fecha = form_data.get("fecha_lanzamiento")
    if not fecha: fecha = None

    repo = AlbumRepository(session)
    datos_nuevos = {
        "nombre": form_data.get("nombre"),
        "artista": form_data.get("artista"),
        "genero": form_data.get("genero"),
        "fecha_lanzamiento": fecha
    }
    repo.update_album(album_id, datos_nuevos)
    return RedirectResponse(url=f"/albumes/{album_id}", status_code=303)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)