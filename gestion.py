def catalogo():
    productos = {
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
    
    return productos

def pedido_usuario():
    ingresos_usuario=[]