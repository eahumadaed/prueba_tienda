class Producto:
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = max(0, stock)
