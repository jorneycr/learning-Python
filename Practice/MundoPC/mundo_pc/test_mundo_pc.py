from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

monitor = Monitor('HP', 15)
teclado = Teclado('MSI', 'Tipo C')
raton = Raton('Dell','USB')
compu = Computadora('HP', monitor, teclado, raton)

monitor1 = Monitor('ACER', 15)
teclado1 = Teclado('MSI', 'Tipo C')
raton1 = Raton('Apple', 'USB')
compu1 = Computadora('ACER', monitor1, teclado1, raton1)

computadoras = [compu, compu1]
Orden1 = Orden(computadoras)
print(Orden1)
