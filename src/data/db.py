from dotenv import load_dotenv
import os
from sqlmodel import create_engine, Session, SQLModel
from models.album import Album

load_dotenv()

db_user: str = os.getenv("DB_USER", "miguel")
db_password: str = os.getenv("DB_PASSWORD", "1234")
db_server: str = os.getenv("DB_SERVER", "fastapi-db")
db_port: str = os.getenv("DB_PORT", "3306")
db_name: str = os.getenv("DB_NAME", "albumesdb")

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}"
engine = create_engine(os.getenv("DB_URL", DATABASE_URL), echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        session.add(Album(nombre="Thriller", artista="Michael Jackson", genero="Pop", fecha_lanzamiento="1982-11-30"))
        session.add(Album(nombre="Back in Black", artista="AC/DC", genero="Hard Rock", fecha_lanzamiento="1980-07-25"))
        session.add(Album(nombre="The Dark Side of the Moon", artista="Pink Floyd", genero="Progressive Rock", fecha_lanzamiento="1973-03-01"))
        session.add(Album(nombre="Future Nostalgia", artista="Dua Lipa", genero="Pop", fecha_lanzamiento="2020-03-27"))
        session.add(Album(nombre="Un Verano Sin Ti", artista="Bad Bunny", genero="Urbano", fecha_lanzamiento="2022-05-06"))
        session.add(Album(nombre="Motomami", artista="Rosalía", genero="Pop/Experimental", fecha_lanzamiento="2022-03-18"))
        session.commit()