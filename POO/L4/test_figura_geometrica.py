from Cuadrado import Cuadrado
from Rectangulo import Rentangulo

print('Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(5, 'rojo')
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
# print(cuadrado1.color)
print(cuadrado1.calcularArea())
print(cuadrado1)

print('Rectangulo'.center(50,'-'))
rentangulo1 = Rentangulo(4, 6, 'verde')
print(rentangulo1.ancho)
print(rentangulo1.alto)
print(rentangulo1.calcularArea())
print(rentangulo1)