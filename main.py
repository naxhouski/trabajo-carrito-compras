from gestion import catalogo,pedido_usuario

def menu():
    print("\n==MENU DEL SUPERMERCADO===")
    print("1)catalago".upper())
    print("2)inrgesar el producto que desea".upper())
    print("3)carrito de compras".upper())
    print("4)salir del supermercado\n")
    
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
