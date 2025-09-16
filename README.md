# api-python-actividad
Repositorio para los que deseen trabajar la actividad de apis con el lenguaje python

# API de Python (FastAPI) - Actividad

Esta es la plantilla base para la actividad de la clase. Tu objetivo es completar los endpoints `PUT` y `DELETE` para gestionar la lista de productos.

## Guía de Inicio

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/api-python-actividad.git](https://github.com/TU_USUARIO/api-python-actividad.git)
    cd api-python-actividad
    ```
    (Reemplaza TU_USUARIO con tu nombre de usuario de GitHub).

2.  **Instalar dependencias:**
    Asegúrate de tener Python instalado y ejecuta:
    ```bash
    pip install fastapi "uvicorn[standard]"
    ```

3.  **Ejecutar la API:**
    ```bash
    uvicorn main:app --reload
    ```
    La API se ejecutará en http://127.0.0.1:8000. Puedes ver la documentación interactiva en http://127.0.0.1:8000/docs.

## Tarea

Completa la lógica de los siguientes endpoints en el archivo `main.py`:

* **PUT /productos/{id}:** Actualiza un producto existente por su ID.
* **DELETE /productos/{id}:** Elimina un producto por su ID.

Una vez terminada la tarea, sube tu código a un nuevo repositorio en tu propia cuenta de GitHub y envía el enlace.
