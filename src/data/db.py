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
    # Borra las tablas y las crea de nuevo (Reset completo)
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        session.add(Album(nombre="POST HUMAN: NEX GEN", artista="Bring Me The Horizon", genero="Alt Metal / Electronic", fecha_lanzamiento="2024-05-24"))
        session.add(Album(nombre="The Death of Peace of Mind", artista="Bad Omens", genero="Industrial / Metalcore", fecha_lanzamiento="2022-02-25"))
        session.add(Album(nombre="Scoring The End of the World", artista="Motionless in White", genero="Industrial Metal", fecha_lanzamiento="2022-06-10"))
        session.add(Album(nombre="Take Me Back To Eden", artista="Sleep Token", genero="Prog / Alt Metal", fecha_lanzamiento="2023-05-19"))
        session.add(Album(nombre="Paper Hearts", artista="Sleep Theory", genero="Alt Rock / Metal", fecha_lanzamiento="2023-09-29"))
        session.add(Album(nombre="I Disagree", artista="Poppy", genero="Nu Metal / Pop", fecha_lanzamiento="2020-01-10"))
        session.add(Album(nombre="The Black Parade", artista="My Chemical Romance", genero="Emo / Rock Opera", fecha_lanzamiento="2006-10-23"))
        session.add(Album(nombre="Shame On Me", artista="Catch Your Breath", genero="Alt Metal", fecha_lanzamiento="2023-10-20"))
        session.add(Album(nombre="The Hell We Create", artista="Fit For A King", genero="Metalcore", fecha_lanzamiento="2022-10-28"))
        session.add(Album(nombre="I Let It In and It Took Everything", artista="Loathe", genero="Metalcore / Shoegaze", fecha_lanzamiento="2020-02-07"))
        session.commit()