from Empleado import Empleado
from Gerente import Gerente


def imprimirDetalles(obj):
    print(obj)
    print(type(obj))
    if isinstance(obj, Gerente):
        print(obj.departamento)

empleado = Empleado('Jorney', 5000)
imprimirDetalles(empleado)

gerente = Gerente('Ismael', 10000, 'System')
imprimirDetalles(gerente)