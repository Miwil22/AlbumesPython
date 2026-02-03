# Memoria del Proyecto Álbumes - NEXUS.AUDIO

## 1 y 2. Desarrollo Local: Integración Web y Persistencia  [Github](https://github.com/Miwil22/AlbumesPython/tree/rama-punto-1-y-2)

* **Frontend (Jinja2):** Se ha integrado el motor de plantillas **Jinja2** con **FastAPI**.
* **Base de Datos (Docker MySQL):** Se ha sustituido el almacenamiento en memoria por una base de datos **MySQL 8.0** ejecutada en un contenedor **Docker**.
    * **Ventaja:** Garantiza que los datos persistan entre reinicios del servidor y evita tener que instalar MySQL.
* **Estilo Visual:** Se ha implementado una interfaz personalizada con temática "Dark Metalcore" (NEXUS).

### Arquitectura Actual:
La aplicación Python conecta localmente (`localhost`) contra el contenedor Docker que expone el puerto `3306`.

![Captura del entorno local](src/static/img/punto1-2.png)