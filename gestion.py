import json
import os
import requests

carrito={}

def catalogo():
    return {
        # Frutas y Verduras
        "manzana": {"precio": 1200, "seccion": "Frutas y Verduras", "stock": 50},
        "platano": {"precio": 1500, "seccion": "Frutas y Verduras", "stock": 40},
        "tomate": {"precio": 1800, "seccion": "Frutas y Verduras", "stock": 35},
        "zanahoria": {"precio": 900, "seccion": "Frutas y Verduras", "stock": 60},
        
        # Lácteos y Huevos
        "leche": {"precio": 1050, "seccion": "Lácteos", "stock": 30},
        "queso": {"precio": 4500, "seccion": "Lácteos", "stock": 15},
        "yogur": {"precio": 450, "seccion": "Lácteos", "stock": 80},
        "huevos_12_un": {"precio": 3200, "seccion": "Lácteos", "stock": 25},
        
        # Abarrotes / Despensa
        "arroz": {"precio": 1300, "seccion": "Despensa", "stock": 100},
        "fideos": {"precio": 850, "seccion": "Despensa", "stock": 120},
        "aceite": {"precio": 2500, "seccion": "Despensa", "stock": 45},
        "harina": {"precio": 1100, "seccion": "Despensa", "stock": 50},
        "azucar": {"precio": 1400, "seccion": "Despensa", "stock": 70},
        "cafe": {"precio": 3800, "seccion": "Despensa", "stock": 20},
        
        # Carnicería y Fiambrería
        "pollo_entero": {"precio": 6500, "seccion": "Carnicería", "stock": 12},
        "carne_molida": {"precio": 5900, "seccion": "Carnicería", "stock": 15},
        "jamon": {"precio": 2200, "seccion": "Fiambrería", "stock": 30},
        
        # Bebidas y Snacks
        "bebida_cola": {"precio": 1800, "seccion": "Bebidas", "stock": 60},
        "jugo_naranja": {"precio": 1200, "seccion": "Bebidas", "stock": 40},
        "papas_fritas": {"precio": 1600, "seccion": "Snacks", "stock": 50}
    }

def agregar_al_carrito(producto, cantidad):
    if producto in carrito:
        carrito[producto] +=cantidad
    else:
        carrito[producto] = cantidad
    return True

def info_carrito():
    return carrito

def vaciar_carrito():
    carrito.clear()
    return True

def calc_total(codigo_descuento=""):
    productos_supermercado = catalogo()
    subtotal =0

    for prod, cant in carrito.items():
        precio_unidad = productos_supermercado[prod]["precio"]
        subtotal += precio_unidad * cant

    descuento = 0
    if codigo_descuento.upper().strip() =="elprofeesbuenaonda":
        descuento =int(subtotal * 0.10)

    total = subtotal - descuento
    return subtotal, descuento, total

def guardar_carrito():
    try:
        with open("carrito_guardado.json","w", enconding="utf-8") as archivo:
            json.dump(carrito, archivo, indent=4)
        return True
    except:
        return False
    
def cargar_carrito():
    global carrito
    if os.path.exists("carrito_guardado.json"):
        try:
            with open("carrito_guardado.json", "r", encoding="utf-8") as archivo:
                carrito = json.load(archivo)
            return True
        except:
            return False
    return False
def obtener_valor_dolar():
    try:
        url ="https://mindicador.cl/api/dolar"
        respuesta = requests.get(url, timeout=5)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos["serie"][0]["valor"]
        return None
    except:
        return None