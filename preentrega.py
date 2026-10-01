productos = []

while True:
    print("=" * 40)
    print("Sistema de gestion de productos")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Elegi una opción (1-5): ").strip()

    if opcion == "1":
        print("---Agregar producto---")
        nombre = input("nombre del producto: ").strip().title()
        while nombre == "":
            print("el nombre no puede estar vacio.")
            nombre = input("nombre del producto: ").strip()

        categoria = input("categoria del producto: ").strip()
        while categoria == "":
            print("La categoria no puede estar vacia.")
            categoria = input("categoria del producto: ").strip()

        precio_str = input("ingresa el precio del producto: ").strip()
        while not precio_str.isdigit():
            print("Error: ingresa solo numeros positivos.")
            precio_str = input("ingresa el precio del producto: ").strip()
        precio = int(precio_str)

        productos.append([nombre, categoria, precio])
        print("Producto agregado con éxito.")

    elif opcion == "2":
        print("--- Lista de productos ---")
        if len(productos) == 0:
            print("Todavía no hay productos cargados.")
        else:
            for i in range(len(productos)):
                print(f"ID:{i+1}\n - Nombre: {productos[i][0]}\n - Categoria: {productos[i][1]}\n - Precio: ${productos[i][2]}")

    elif opcion == "3":
        print("--- Buscar producto ---")
        if len(productos) == 0:
            print("Todavía no hay productos cargados.")
        else:
            busqueda = input("Ingresa el nombre a buscar: ").strip().lower()
            encontrados = 0
            for i in range(len(productos)):
                if productos[i][0].lower() == busqueda:
                    print(f"ID:{i+1}\n - Nombre: {productos[i][0]}\n - Categoria: {productos[i][1]}\n - Precio: ${productos[i][2]}")
                    encontrados += 1
            if encontrados == 0:
                print("No se encontraron resultados.")

    elif opcion == "4":
        print("--- Eliminar producto ---")
        if len(productos) == 0:
            print("Todavía no hay productos cargados.")
        else:
            for i in range(len(productos)):
                print(f"ID:{i+1} - {productos[i][0]}")
            posicion_str = input("Ingresa el ID del producto a eliminar: ").strip()
            if posicion_str.isdigit() and 1 <= int(posicion_str) <= len(productos):
                posicion = int(posicion_str) - 1
                eliminado = productos.pop(posicion)
                print(f"Producto '{eliminado[0]}' eliminado con éxito.")
            else:
                print("ID inválido.")

    elif opcion == "5":
        print("hasta luego")
        break

    else:
        print("Opción no válida")

