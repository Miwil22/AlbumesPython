from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from typing import Annotated
from models.album import Album, AlbumCreate, AlbumResponse, map_album_to_response, map_create_to_album

from data.album_repository import AlbumRepository
from data.db import get_session, init_db

router = APIRouter(prefix="/api/albumes", tags=["albumes"])

SessionDep = Annotated[Session, Depends(get_session)]

@router.get("/", response_model=list[AlbumResponse])
async def lista_albumes(session: SessionDep):
    repo = AlbumRepository(session)
    albums = repo.get_all_albums()
    return [map_album_to_response(album) for album in albums]

@router.post("/", response_model=AlbumResponse)
async def nuevo_album(album_create: AlbumCreate, session: SessionDep):
    repo = AlbumRepository(session)
    album = map_create_to_album(album_create)
    album_creado = repo.create_album(album)
    return map_album_to_response(album_creado)

@router.get("/{album_id}", response_model=AlbumResponse)
async def album_por_id(album_id: int, session: SessionDep):
    repo = AlbumRepository(session)
    album_encontrado = repo.get_album(album_id)
    if not album_encontrado:
        raise HTTPException(status_code=404, detail="Album no encontrado")
    return map_album_to_response(album_encontrado)

@router.delete("/{album_id}", status_code=204)
async def borrar_album(album_id: int, session: SessionDep):
    repo = AlbumRepository(session)
    album_encontrado = repo.get_album(album_id)
    if not album_encontrado:
        raise HTTPException(status_code=404, detail="Album no encontrado")
    repo.delete_album(album_id)
    return

@router.patch("/{album_id}", response_model=AlbumResponse)
async def actualizar_album(album_id: int, album: Album, session: SessionDep):
    repo = AlbumRepository(session)
    album_encontrado = repo.get_album(album_id)
    if not album_encontrado:
        raise HTTPException(status_code=404, detail="Album no encontrado")
    album_data = album.model_dump(exclude_unset=True)
    album_encontrado.sqlmodel_update(album_data)
    repo.update_album(album_encontrado.id, album_data)
    return map_album_to_response(album_encontrado)

@router.put("/", response_model = AlbumResponse)
async def cambia_album(album: Album, session: SessionDep):
    repo = AlbumRepository(session)
    album_encontrado = repo.get_album(album.id)
    if not album_encontrado:
        raise HTTPException(status_code=404, detail="Album no encontrado")
    album_data = album.model_dump()
    album_encontrado.sqlmodel_update(album_data)
    repo.update_album(album_encontrado.id, album_data)
    return map_album_to_response(album_encontrado)
