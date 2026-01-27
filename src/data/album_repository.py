from sqlmodel import Session, select
from models.album import Album

class AlbumRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_all_albums(self) -> list[Album]:
        albums = self.session.exec(select(Album)).all()
        return albums
    
    def get_album(self, album_id: int) -> Album:
        album = self.session.get(Album, album_id)
        return album
    
    def create_album(self, album: Album) -> Album:
        self.session.add(album)
        self.session.commit()
        self.session.refresh(album)
        return album
    
    def update_album(self, album_id: int, album_data: dict) -> Album:
        album = self.get_album(album_id)
        for key, value in album_data.items():
            setattr(album, key, value)
        self.session.commit()
        self.session.refresh(album)
        return album
    
    def delete_album(self, album_id: int) -> None:
        album = self.get_album(album_id)
        self.session.delete(album)
        self.session.commit()