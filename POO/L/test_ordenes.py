from Orden import Orden
from Producto import Producto

producto1 = Producto('Camisa', 100)
producto2 = Producto('Pantalom', 200)
producto3 = Producto('Camisa', 500)
producto4 = Producto('Pantalom', 300)
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

order1 = Orden(productos1)
print(order1)
print(f'Total orden1: {order1.calcularTotal()}')
order2 = Orden(productos2)
print(order2)
print(f'Total orden2: {order2.calcularTotal()}')
