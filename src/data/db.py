import mysql.connector

db_config = {
    'host': '127.0.0.1',      
    'user': 'root',          
    'password': '',   
    'database': 'albumes_db'  
}

def get_connection():
    temp_config = db_config.copy()
    del temp_config['database']
    
    conn = mysql.connector.connect(**temp_config)
    cursor = conn.cursor()
    
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['database']}")
    conn.close()

    return mysql.connector.connect(**db_config)

def iniciar_db():
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS albumes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            artista VARCHAR(255) NOT NULL,
            genero VARCHAR(255) NOT NULL,
            fecha_lanzamiento DATE NOT NULL
            )
    """)

    cursor.execute("SELECT COUNT(*) FROM albumes")
    count = cursor.fetchone()[0]

    if count == 0:
        print("Cargando datos nuevos en MySQL...")
        
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
            VALUES (%s, %s, %s, %s)
        """, datos)
        
        conn.commit()
        print("Datos insertados correctamente.")

    cursor.close()
    conn.close()

def obtener_albumes():
    iniciar_db() 
    conn = get_connection()
    cursor = conn.cursor(dictionary=True) 
    
    cursor.execute("SELECT * FROM albumes")
    resultados = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return resultados