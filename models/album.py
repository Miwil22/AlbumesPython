from datetime import date
from sqlmodel import Field, SQLModel
from pydantic import BaseModel

class Album(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, max_length=100)
    artista: str = Field(index=True, max_length=100)
    genero: str | None = Field(default=None, max_length=50)
    fecha_lanzamiento: date | None = Field(default=None)

class AlbumCreate(BaseModel):
    nombre: str
    artista: str
    genero: str | None = None
    fecha_lanzamiento: date | None = None

class AlbumUpdate(BaseModel):
    nombre: str | None = None
    artista: str | None = None
    genero: str | None = None
    fecha_lanzamiento: date | None = None

class AlbumResponse(BaseModel):
    id: int
    nombre: str
    artista: str
    genero: str | None = None
    fecha_lanzamiento: date | None = None

def map_album_to_response(album: Album) -> AlbumResponse:
    return AlbumResponse(
        id=album.id,
        nombre=album.nombre,
        artista=album.artista,
        genero=album.genero,
        fecha_lanzamiento=album.fecha_lanzamiento
    )

def map_create_to_album(album_create: AlbumCreate) -> Album:
    return Album(
        nombre=album_create.nombre,
        artista=album_create.artista,
        genero=album_create.genero,
        fecha_lanzamiento=album_create.fecha_lanzamiento
    )

def map_update_to_album(album: Album, album_update: AlbumUpdate) -> Album:
    if album_update.nombre is not None:
        album.nombre = album_update.nombre
    if album_update.artista is not None:
        album.artista = album_update.artista
    if album_update.genero is not None:
        album.genero = album_update.genero
    if album_update.fecha_lanzamiento is not None:
        album.fecha_lanzamiento = album_update.fecha_lanzamiento
    return album

