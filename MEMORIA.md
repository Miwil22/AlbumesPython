# Memoria del Proyecto Álbumes - NEXUS.AUDIO

# Memoria del Proyecto Álbumes - NEXUS.AUDIO

## 1 y 2. Desarrollo Local: Integración Web y Persistencia  [Github](https://github.com/Miwil22/AlbumesPython/tree/rama-punto-1-y-2)

* **Frontend (Jinja2):** Se ha integrado el motor de plantillas **Jinja2** con **FastAPI**.
* **Base de Datos (Docker MySQL):** Se ha sustituido el almacenamiento en memoria por una base de datos **MySQL 8.0** ejecutada en un contenedor **Docker**.
    * **Ventaja:** Garantiza que los datos persistan entre reinicios del servidor y evita tener que instalar MySQL.
* **Estilo Visual:** Se ha implementado una interfaz personalizada con temática "Dark Metalcore" (NEXUS).

### Arquitectura Actual:
La aplicación Python conecta localmente (`localhost`) contra el contenedor Docker que expone el puerto `3306`.

![Captura del entorno local](src/static/img/punto1-2.png)


## 3. Dockerización con MySQL y Estilo [Github](https://github.com/Miwil22/AlbumesPython/tree/rama-punto-3)
La aplicación se ha contenerizado utilizando **Docker**, lo que garantiza que el entorno de desarrollo sea idéntico al de producción. Se han orquestado dos servicios en el `docker-compose.yml`:
1.  **fastapi-app:** La aplicación web (API + Frontend).
2.  **fastapi-db:** Base de datos **MySQL**.

Además, se ha implementado el diseño final "Dark Mode" (NEXUS) con CSS personalizado, mejorando la experiencia de usuario (UX).

![App](src/static/img/punto3.png)
