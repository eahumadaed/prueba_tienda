class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(stock, 0)  # Asegura que el stock no sea negativo

    def __str__(self):
        return f"Producto: {self.__nombre}, Precio: {self.__precio:,.0f}, Stock: {self.__stock}"

    def __eq__(self, other):
        return self.__nombre == other.__nombre

    def agregar_stock(self, cantidad):
        self.__stock += max(cantidad, 0)  # Evita agregar stock negativo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        self.__stock = max(value, 0)  # Asegura que el stock no sea negativo
