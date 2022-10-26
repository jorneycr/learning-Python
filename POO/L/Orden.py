from Producto import Producto


class Orden:
    contadorOrdenes = 0
    def __init__(self, productos):
        Orden.contadorOrdenes += 1
        self._id_Orden = Orden.contadorOrdenes
        self._productos = list(productos)

    def agregarProducto(self, producto):
        self._productos.append(producto)

    def calcularTotal(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + ' | '

        return f'Orden: {self._id_Orden}, \nProductos: {productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100)
    producto2 = Producto('Pantalom', 200)
    productos1 = [producto1, producto2]
    order1 = Orden(productos1)
    print(order1)
    order2 = Orden(productos1)
    print(order2)

