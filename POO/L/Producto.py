class Producto:
    contadorProductos = 0

    def __init__(self, nombre, precio):
        Producto.contadorProductos += 1
        self._id_producto = Producto.contadorProductos
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
    producto1 = Producto('Camisa',100)
    print(producto1)
    producto2 = Producto('Pantalom',200)
    print(producto2)
