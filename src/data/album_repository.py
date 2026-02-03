from sqlmodel import Session, select
from models.album import Album

class AlbumRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_albums(self) -> list[Album]:
        statement = select(Album)
        return self.session.exec(statement).all()

    def get_album(self, album_id: int) -> Album | None:
        return self.session.get(Album, album_id)

    def get_album_by_id(self, album_id: int) -> Album | None:
        return self.get_album(album_id)

    def create_album(self, album: Album) -> Album:
        self.session.add(album)
        self.session.commit()
        self.session.refresh(album)
        return album

    def update_album(self, album_id: int, data: dict) -> Album:
        album = self.get_album(album_id)
        if album:
            for key, value in data.items():
                if value is not None: 
                    setattr(album, key, value)
            self.session.commit()
            self.session.refresh(album)
        return album

    def delete_album(self, album_id: int) -> None:
        album = self.get_album(album_id)
        if album:
            self.session.delete(album)
            self.session.commit()