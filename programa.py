from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

def main():
    print("Bienvenido al sistema de gestión de tiendas.")
    # Solicitar el nombre de la tienda
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    # Solicitar el costo de delivery
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    # Mostrar un menú de selección de tipo de tienda
    print("Seleccione el tipo de tienda:")
    print("1. Restaurante")
    print("2. Supermercado")
    print("3. Farmacia")
    opcion = int(input("Ingrese el número correspondiente al tipo de tienda: "))
    # Crear la instancia de tienda correspondiente según la selección
    if opcion == 1:
        tienda = Restaurante(nombre_tienda, costo_delivery)
    elif opcion == 2:
        tienda = Supermercado(nombre_tienda, costo_delivery)
    elif opcion == 3:
        tienda = Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Opción no válida. Saliendo del programa.")
        return
    acciones = {
        "1": "Agregar producto",
        "2": "Listar productos",
        "3": "Realizar una venta",
        "4": "Salir"
    }
    while True:
        print("\nSeleccione una acción:")
        for key, value in acciones.items():
            print(f"{key}. {value}")

        opcion = input("Ingrese el número de la acción deseada: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio del producto: "))
            stock_producto = int(input("Ingrese el stock del producto (opcional, 0 por defecto): ") or "0")
            producto = Producto(nombre_producto, precio_producto, stock_producto)
            tienda.agregar_producto(producto)
        elif opcion == "2":
            print("Listado de productos:")
            print(tienda.listar_productos())
        elif opcion == "3":
            while True:
                nombre_producto = input("Ingrese el nombre del producto a vender: ")
                if not tienda.verificar_producto(nombre_producto):
                    print("Producto no encontrado")
                    continue
                break
            cantidad = int(input("Ingrese la cantidad a vender: "))
            tienda.realizar_venta(nombre_producto, cantidad)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
