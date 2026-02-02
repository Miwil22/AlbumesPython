# Memoria del Proyecto Álbumes - NEXUS.AUDIO

## 1. Integración de Jinja2 y API
Se han añadido plantillas HTML utilizando el motor **Jinja2** para visualizar los datos de la API. Esto permite separar la lógica de los datos (Backend) de la presentación visual (Frontend).

![App](src/static/img/punto1.png)

## 2. Base de datos en local
En esta fase se ha implementado la conexión a una base de datos real utilizando **SQLModel**. Esto asegura la persistencia de los datos, evitando que se pierdan al reiniciar el servidor.

![App](src/static/img/punto2.png)

## 3. Dockerización con MySQL y Estilo
La aplicación se ha contenerizado utilizando **Docker**. Se han creado dos servicios en el `docker-compose.yml`:
1.  **fastapi-app:** La aplicación web.
2.  **fastapi-db:** Base de datos **MySQL**.

Además, se ha implementado el diseño final "Dark Mode" (NEXUS) con CSS personalizado.

![App](src/static/img/punto3.png)

## 4. Migración a PostgreSQL
Para demostrar la flexibilidad del ORM, se ha migrado el sistema a **PostgreSQL** manteniendo la infraestructura de Docker.
- Se cambió el contenedor de base de datos a `postgres:15`.
- Se actualizó el driver de Python a `psycopg2-binary`.
- El código de la aplicación no requirió cambios gracias a SQLModel.

![App](src/static/img/punto4.png)

## 5. Despliegue en la Nube (Render)
El proyecto ha sido desplegado en producción utilizando la plataforma **Render**.

### Paso 1: Creación de la Base de Datos
Primero, se creó una instancia de **PostgreSQL** gestionada en la nube (zona Frankfurt).

![Creación DB](src/static/img/punto5.1.png)
![Plan Gratuito](src/static/img/punto5.2.png)

Una vez creada y disponible, obtuvimos la **Internal Database URL** para la conexión interna dentro de la red de Render.

![Estado DB](src/static/img/punto5.3.png)
![Credenciales](src/static/img/punto5.4.png)

### Paso 2: Creación del Web Service
Se creó un nuevo servicio web conectado al repositorio de GitHub (`master`).

![Nuevo Servicio](src/static/img/punto5.5.png)

Render detectó automáticamente que el proyecto utiliza **Docker** gracias al `Dockerfile` presente en el repositorio.

![Configuración Docker](src/static/img/punto5.6.png)

### Paso 3: Variables de Entorno
Para conectar la web con la base de datos sin exponer credenciales en el código, se configuró la variable de entorno `DB_URL` con la dirección interna de la base de datos PostgreSQL creada anteriormente.

![Variables de Entorno](src/static/img/punto5.7.png)

### Paso 4: Despliegue y Resultado Final
Render construyó la imagen de Docker y desplegó el servicio correctamente (`Your service is live`).

![Logs del Despliegue](src/static/img/punto5.8.png)

La aplicación es ahora accesible públicamente a través de internet, totalmente funcional y con persistencia de datos en la nube.

![Resultado Final](src/static/img/punto5.9.png)