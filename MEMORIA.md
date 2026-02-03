## 1 y 2. Desarrollo Local: Integración Web y Persistencia  [Github](https://github.com/Miwil22/AlbumesPython/tree/rama-punto-1-y-2)

* **Frontend (Jinja2):** Se ha integrado el motor de plantillas **Jinja2** con **FastAPI**.
* **Base de Datos (Docker MySQL):** Se ha sustituido el almacenamiento en memoria por una base de datos **MySQL 8.0** ejecutada en un contenedor **Docker**.
    * **Ventaja:** Garantiza que los datos persistan entre reinicios del servidor y evita tener que instalar MySQL.
* **Estilo Visual:** Se ha implementado una interfaz personalizada con temática "Dark Metalcore" (NEXUS).

### Arquitectura Actual:
La aplicación Python conecta localmente (`localhost`) contra el contenedor Docker que expone el puerto `3306`.

![Captura del entorno local](src/static/img/punto1-2.png)

## 2. Base de datos en local [Github](https://github.com/Miwil22/AlbumesPython/tree/rama-punto-2)
En esta fase se ha implementado la conexión a una base de datos persistente utilizando **SQLModel**. Esto asegura la integridad de los datos, evitando que se pierdan al reiniciar el servidor, un problema común cuando se trabaja con almacenamiento en memoria.

![App](src/static/img/punto2.png)

## 3. Dockerización con MySQL y Estilo [Github](https://github.com/Miwil22/AlbumesPython/tree/rama-punto-3)
La aplicación se ha contenerizado utilizando **Docker**, lo que garantiza que el entorno de desarrollo sea idéntico al de producción. Se han orquestado dos servicios en el `docker-compose.yml`:
1.  **fastapi-app:** La aplicación web (API + Frontend).
2.  **fastapi-db:** Base de datos **MySQL**.

Además, se ha implementado el diseño final "Dark Mode" (NEXUS) con CSS personalizado, mejorando la experiencia de usuario (UX).

![App](src/static/img/punto3.png)

## 4. Migración a PostgreSQL [Github](https://github.com/Miwil22/AlbumesPython/tree/rama-punto-4)
Para demostrar la flexibilidad del ORM y preparar el sistema para un entorno de producción más robusto, se ha migrado el motor de base de datos a **PostgreSQL**.

**Cambios Técnicos:**
- **Versión:** Se seleccionó **PostgreSQL 15** por ser una versión estable y ampliamente soportada, que ofrece un excelente equilibrio entre rendimiento, seguridad y compatibilidad con las librerías modernas de Python.
- **Driver:** Se actualizó el driver de Python a `psycopg2-binary` para permitir la comunicación con el nuevo motor.
- **Transparencia:** Gracias al uso de SQLModel, no fue necesario reescribir las consultas SQL en el código de la aplicación; el ORM gestionó la traducción de dialectos automáticamente.

![App](src/static/img/punto4.png)