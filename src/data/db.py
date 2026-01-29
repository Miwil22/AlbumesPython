import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "albumes.db")

def get_connection():
    """Conecta a la base de datos SQLite (archivo local)."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row 
    return conn

def iniciar_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS albumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            artista TEXT NOT NULL,
            genero TEXT NOT NULL,
            fecha_lanzamiento TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM albumes")
    count = cursor.fetchone()[0]

    if count == 0:
        print("Generando archivo de base de datos local (SQLite)...")
        
        datos = [
            ("POST HUMAN: NEX GEN", "Bring Me The Horizon", "Alt Metal / Electronic", "2024-05-24"),
            ("The Death of Peace of Mind", "Bad Omens", "Industrial / Metalcore", "2022-02-25"),
            ("Scoring The End of the World", "Motionless in White", "Industrial Metal", "2022-06-10"),
            ("Take Me Back To Eden", "Sleep Token", "Prog / Alt Metal", "2023-05-19"),
            ("Paper Hearts", "Sleep Theory", "Alt Rock / Metal", "2023-09-29"),
            ("I Disagree", "Poppy", "Nu Metal / Pop", "2020-01-10"),
            ("The Black Parade", "My Chemical Romance", "Emo / Rock Opera", "2006-10-23"),
            ("Shame On Me", "Catch Your Breath", "Alt Metal", "2023-10-20"),
            ("The Hell We Create", "Fit For A King", "Metalcore", "2022-10-28"),
            ("I Let It In and It Took Everything", "Loathe", "Metalcore / Shoegaze", "2020-02-07")
        ]

        cursor.executemany("""
            INSERT INTO albumes (titulo, artista, genero, fecha_lanzamiento) 
            VALUES (?, ?, ?, ?)
        """, datos)
        
        conn.commit()

    conn.close()

def obtener_albumes():
    iniciar_db() 
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM albumes")
    resultados = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return resultados