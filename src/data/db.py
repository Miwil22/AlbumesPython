from sqlmodel import create_engine, SQLModel, Session
from models.album import Album
from datetime import date

db_user: str = "miguel"
db_password: str = "1234"
db_server: str = "localhost"
db_port: int = 3306
db_name: str = "albumesdb"

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(Album(nombre="That's the Spirit", artista="Bring Me the Horizon", genero="Metalcore", precio=25.00, fecha_estreno=date(2015, 9, 11)))
        session.add(Album(nombre="The Black Parade", artista="My Chemical Romance", genero="Emo", precio=30.00, fecha_estreno=date(2006, 10, 24)))
        session.add(Album(nombre="THE DEATH OF PEACE OF MIND", artista="Bad Omens", genero="Metalcore", precio=35.00, fecha_estreno=date(2022, 10, 25)))
        session.add(Album(nombre="Nothing Personal", artista="All Time Low", genero="Pop Punk", precio=25.00, fecha_estreno=date(2009, 7, 7)))
        session.add(Album(nombre="Scoring The End Of The World", artista="Motionless In White", genero="Industrial Metal", precio=30.00, fecha_estreno=date(2022, 6, 10)))

        session.commit()