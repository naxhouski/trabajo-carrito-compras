from gestion import catalogo, agregar_al_carrito, obtener_valor_dolar, vaciar_carrito,cargar_carrito, info_carrito,calc_total,guardar_carrito

if cargar_carrito():
    print("\n[INFO] Se recuperó tu carrito de la sesión anterior")
else:
    print("[INFO] No se encontro ningun carrito guardado, Iniciando sesion nueva")


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
    try:
        op=int(input("ingrese la opcion que desea (1-5): "))
    except ValueError:
        print("ERROR: Ingrese una opcion valida")
        continue

    if op == 1:
        print("\n" + "="*50)
        print(f"{'PRODUCTO':<20} | {'PRECIO':<10} | {'SECCION'}")
        print("="*50)
        
        producto_dict = catalogo()
        for prod, detalle in producto_dict.items():
            nombre_legible = prod.replace("_", " ").capitalize()
            print(f"{nombre_legible:<20} | ${detalle['precio']:<10} | {detalle['seccion']}")
        print("="*50)

    elif op==2:
       producto_dict = catalogo()
       pedido =input("\n Ingrese el nombre del producto que desea comprar: ").lower().strip().replace(" ", "_")

       if pedido in producto_dict:
            try:
               cantidad=int(input(f"cuantas unidades de '{pedido}' va llevar: "))
               if cantidad > 0:
                   agregar_al_carrito(pedido, cantidad)
                   print(f"se guardaron {cantidad} de '{pedido.replace('_',' ')}' al carrito")
               else:
                   print("EEROR: la cantidad que ingresa debe ser mayor a 0")
            except ValueError:
                print("EEROR: solo ingresar cantidades numericas enteras")
       else:
            print("ERROR: el producto que escribio no esta en el catalogo")
            continue
    elif op==3:
        print("\n===========================================")
        print("             RESUMEN DE COMPRA             ")
        print("===========================================")

        carro = info_carrito()
        if len(carro) == 0:
            print("tu carrito de compras esta vacio")
        else:
            producto_dict = catalogo()
            for prod, cant in carro.items():
                precio_u = producto_dict[prod]["precio"]
                sub_item = precio_u * cant
                print(f" {prod.replace('_', ' ').capitalize():<18} x{cant:<3} | suntotal: ${sub_item}")

            print("----------------------------------------------------------")
            cupon = input("¿tiene algun codigo de descuento? (Enter si no):").strip()

            sub, desc, tot =calc_total(cupon)

            print(f"subtotal:          ${sub} CLP")
            if desc > 0:
                print(f"Descuento (10%): -${desc} CLP")
            print(f"TOTAL A PAGAR:     ${tot} CLP")
            print("-----------------------------------------------------------")
            

            print("verificando cotizacion del dolar en el banco de chile...")
            val_dolar = obtener_valor_dolar()
            if val_dolar:
                total_usd = tot / val_dolar
                print(f"Valor USD hoy:    ${val_dolar} CLP")
                print(f"TOTAL EQUIVALENTE: ${total_usd:.2f} USD")
            else:
                print("[API] No se pudo conseguir la taza actual")
        print("===========================================")
    elif op==4:
      vaciar_carrito()
      print("\n[INFO] Se ha vaciado el carrito. todos los articulos fueron borrados.")
    
    elif op==5:
        print("\n Guardando los datos de la sesion...")
        if guardar_carrito:
            print("[INFO] El respaldo del carrito se ha guardado con exito")
        else:
            print("\n[ADVERTENCIA] NO SE PUDO GUARDAR TU CARRITO")
        print("Gracias por preferir nuestro supermercado")
        break
    else:
     print("Opcion invalida. solo debe ingresar del 1 al 5")