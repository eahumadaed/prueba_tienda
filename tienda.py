from abc import ABC, abstractmethod #https://docs.python.org/3/library/abc.html
from producto import Producto

class Tienda(ABC):
    def __init__(self, nombre, costo_envio):
        self._nombre = nombre
        self.costo_envio = costo_envio
        self._productos = []
        
        
class Supermercado(Tienda):
    def listar_productos(self):
        resultado = []
        for producto in self._productos:
            mensaje = f"{producto.nombre} - ${producto.precio}"
            if producto.stock < 10:
                mensaje += " - Pocos productos disponibles"
            resultado.append(mensaje)
        return "\n".join(resultado)