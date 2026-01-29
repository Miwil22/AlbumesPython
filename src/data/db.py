import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "albumes.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row 
    return conn

def iniciar_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS albumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            artista TEXT NOT NULL,
            genero TEXT NOT NULL,
            fecha_lanzamiento TEXT NOT NULL
        )
    """)
    
    cursor.execute("SELECT COUNT(*) FROM albumes")
    if cursor.fetchone()[0] == 0:
        datos = [
            ("POST HUMAN: NEX GEN", "Bring Me The Horizon", "Alt Metal", "2024-05-24"),
            ("The Death of Peace of Mind", "Bad Omens", "Industrial", "2022-02-25"),
            ("Scoring The End of the World", "Motionless in White", "Metalcore", "2022-06-10"),
            ("Take Me Back To Eden", "Sleep Token", "Prog Metal", "2023-05-19")
        ]
        cursor.executemany("INSERT INTO albumes (nombre, artista, genero, fecha_lanzamiento) VALUES (?, ?, ?, ?)", datos)
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

def crear_nuevo_album(nombre, artista, genero, fecha):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO albumes (nombre, artista, genero, fecha_lanzamiento) VALUES (?, ?, ?, ?)", 
                   (nombre, artista, genero, fecha))
    conn.commit()
    conn.close()

def obtener_album_por_id(id_album):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM albumes WHERE id = ?", (id_album,))
    fila = cursor.fetchone()
    conn.close()
    if fila:
        return dict(fila)
    return None