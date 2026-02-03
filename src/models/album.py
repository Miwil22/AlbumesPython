from datetime import date
from sqlmodel import Field, SQLModel
from pydantic import BaseModel, field_validator

class Album(SQLModel, table=True):
    """Representa una serie en la base de datos"""
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, max_length=100)
    artista: str = Field(index=True, max_length=100)
    genero: str = Field(index=True, max_length=50)
    precio: float | None = Field(index=True)
    fecha_estreno: date | None = Field(nullable=True)



class AlbumCreate(BaseModel):
    """Modelo para crear un nuevo album (lo que recibe el POST)"""
    nombre: str
    artista: str
    genero: str
    precio: float
    fecha_estreno: date | None = None

    @field_validator("precio")
    def precio_must_be_positive(cls, value):
        if value < 0:
            raise ValueError("El precio debe ser un valor positivo")
        return value
    
class AlbumUpdate(BaseModel):
    """Modelo para actualizar un album (lo que recibe el PUT/PATCH)"""
    nombre: str | None = None
    artista: str | None = None
    genero: str | None = None
    precio: float | None = None
    fecha_estreno: date | None = None
    
    @field_validator("precio")
    def precio_must_be_positive(cls, value):
        if value is not None and value < 0:
            raise ValueError("El precio debe ser un valor positivo")
        return value
    
class AlbumResponse(BaseModel):
    """Modelo de respuesta (lo que devuelve la API al cliente)"""
    id: int
    nombre: str
    artista: str
    genero: str
    precio: float | None
    fecha_estreno: date | None
    
    class Config:
        from_attributes = True

def map_album_to_response(album: Album) -> AlbumResponse:
    """
    Convierte un Album de BD a AlbumResponse para enviar al cliente Album
    (BD) -> AlbumResponse (API)
    """
    return AlbumResponse(
        id=album.id,
        nombre=album.nombre,
        artista=album.artista,
        genero=album.genero,
        precio=album.precio,
        fecha_estreno=album.fecha_estreno
    )

def map_create_to_album(album_create: AlbumCreate) -> Album:
    """
    Convierte AlbumCreate (datos del cliente) a Album (para guardar en BD)
    AlbumCreate (API) -> Album (BD)
    """
    return Album(
        nombre=album_create.nombre,
        artista=album_create.artista,
        genero=album_create.genero,
        precio=album_create.precio,
        fecha_estreno=album_create.fecha_estreno
    )

def map_update_to_album(album: Album, album_update: AlbumUpdate) -> Album:
    """
    Actualiza un Album existente con los datos de AlbumUpdate
    Solo actualiza los campos que vienen informados (no son None)
    """
    if album_update.nombre is not None:
        album.nombre = album_update.nombre
    if album_update.artista is not None:
        album.artista = album_update.artista
    if album_update.genero is not None:
        album.genero = album_update.genero
    if album_update.precio is not None:
        album.precio = album_update.precio
    if album_update.fecha_estreno is not None:
        album.fecha_estreno = album_update.fecha_estreno
    return album