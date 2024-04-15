class Tienda:
    def __init__(self, nombre, costo_delivery):
        self._nombre = nombre
        self._costo_delivery = costo_delivery
        self._productos = []  # Lista para almacenar los productos

    def agregar_producto(self, producto):
        # Busca si el producto ya existe en la tienda
        for prod in self._productos:
            if prod.nombre == producto.nombre:
                prod.agregar_stock(producto.stock)  # Añade stock si el producto ya existe
                return
        self._productos.append(producto)  # Añade un nuevo producto si no existe

    def listar_productos(self):
        # Genera un string con la información de todos los productos
        return '\n'.join(str(prod) for prod in self._productos)
    
    def verificar_producto(self,nombre_producto):
        # Verifico que el producto se encuentre en la lista
        return any(producto.nombre == nombre_producto for producto in self._productos)

    def realizar_venta(self, nombre_producto, cantidad):
        # Busca el producto y reduce el stock según la cantidad vendida
        for producto in self._productos:
            if producto.nombre == nombre_producto:
                if cantidad <= producto.stock:
                    producto.stock -= cantidad
                    print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                else:
                    print("No hay suficiente stock para realizar la venta.")
                return
        print("Producto no encontrado.")

class Restaurante(Tienda):
    def agregar_producto(self, producto):
        # Asegura que el stock se mantiene en 0 para restaurantes
        producto.stock = 0
        super().agregar_producto(producto)

    def listar_productos(self):
        # Oculta el stock en el listado de productos
        return '\n'.join(f"{prod.nombre}, Precio: ${format(int(prod.precio), ',').replace(',', '.')}" for prod in self._productos)
    
    def verificar_producto(self,nombre_producto):
        # Verifico que el producto se encuentre en la lista
        return any(producto.nombre == nombre_producto for producto in self._productos)
    
    def realizar_venta(self, nombre_producto, cantidad):
        # Verifica solo si el producto existe, no necesita verificar stock
        for producto in self._productos:
            if producto.nombre == nombre_producto:
                print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                return
        print("Producto no encontrado.")

class Supermercado(Tienda):
    def listar_productos(self):
        # Añade una advertencia si el stock es bajo
        result = []
        for prod in self._productos:
            alerta = "Pocos productos disponibles" if prod.stock < 10 else ""
            result.append(f"{prod} {alerta}")
        return '\n'.join(result)

class Farmacia(Tienda):
    def listar_productos(self):
        # Añade un mensaje de envío gratis para productos caros
        result = []
        for prod in self._productos:
            envio_gratis = "Envío gratis al solicitar este producto" if prod.precio > 15000 else ""
            result.append(f"{prod} {envio_gratis}")
        return '\n'.join(result)
    
    def verificar_producto(self,nombre_producto):
        # Verifico que el producto se encuentre en la lista
        return any(producto.nombre == nombre_producto for producto in self._productos)
    
    def realizar_venta(self, nombre_producto, cantidad):
        # Limita la cantidad de productos que se pueden vender en una transacción
        if cantidad > 3:
            print("No se puede vender más de 3 unidades del mismo producto en la farmacia.")
            return
        super().realizar_venta(nombre_producto, cantidad)
