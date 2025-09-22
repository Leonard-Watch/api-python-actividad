from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware # importa el middleware de cors

app = FastAPI()

# Define los orígenes que pueden hacer peticiones a tu API
# En este caso, solo permitiremos localhost en el puerto 8000
origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Permite los orígenes definidos
    allow_credentials=True, # Permite cookies
    allow_methods=["*"], # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], # Permite todas las cabeceras
)


# Repositorio de datos: una lista de diccionarios en memoria.
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1200},
    {"id": 2, "nombre": "Mouse", "precio": 25},
    {"id": 3, "nombre": "Teclado", "precio": 75}
]

# --- Endpoints de la API

# GET: Obtiene todos los productos
@app.get("/productos")
def get_productos():
    return productos

# POST: Crea un nuevo producto
@app.post("/productos")
def create_producto(producto: dict):
    productos.append(producto)
    return {"message": "Producto creado con éxito", "data": producto}

# TAREA: Agregar un endpoint PUT para actualizar un producto.
# Deberá recibir el ID del producto y los nuevos datos.
@app.put("/productos/{id}")
def update_producto(id: int, producto_actualizado: dict):
    idx = next((i for i, p in enumerate(productos) if p["id"] == id), None)
    if idx is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if "nombre" in producto_actualizado:
        productos[idx]["nombre"] = producto_actualizado["nombre"]
    if "precio" in producto_actualizado:
        productos[idx]["precio"] = producto_actualizado["precio"]

    return {"message": "Producto actualizado", "data": productos[idx]}
# TAREA: Agregar un endpoint DELETE para eliminar un producto.
# Deberá recibir el ID del producto a eliminar.
@app.delete("/productos/{id}")
def delete_producto(id: int):
    idx = next((i for i, p in enumerate(productos) if p["id"] == id), None)
    if idx is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    eliminado = productos.pop(idx)
    return {"message": "Producto eliminado", "data": eliminado}