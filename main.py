from gestion import catalogo,pedido_usuario

def menu():
    print("\n===========================================")
    print("      SISTEMA DE CARRITO DE COMPRAS        ")
    print("===========================================")
    print("1) VER CATALOGO DE PRODUCTOS")
    print("2) AGREGAR PRODUCTO AL CARRITO")
    print("3) VER RESUMEN DEL CARRITO Y TOTAL")
    print("4) VACIAR EL CARRITO DE COMPRAS")
    print("5) SALIR DEL SISTEMA")
    print("===========================================")
    
while True:
    menu()
    op=int(input("ingrese la opcion que desea: "))

    if op==1:
        print("CATALOGO DEL SUPERMERCADO")
        print(catalogo())
        continue
    elif op==2:
        pedidos=input("que desea comprar del catalago: ")
        pedido_usuario=pedidos
    elif op==3:
        print("carrito".upper())
        print(pedido_usuario())   
    elif op==4:
        print("Gracias por su visita, Vuelva pronto ;)")
        break


#fin del progrmaa