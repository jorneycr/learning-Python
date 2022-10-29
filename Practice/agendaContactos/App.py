import os

from Utils import agregar_contacto, editar_contacto, ver_contacto, buscar_contacto, eliminar_contacto
from Constantes import CARPETA

def app():
    crear_directorio()
    mostrarMenu()

    preguntar = True
    while preguntar:
        opcion = input('Selecione una opcion: \r\n')
        opcion = int(opcion)

        if opcion == 1:
            res = agregar_contacto()
            preguntar = False
            if res:
                app()
        elif opcion == 2:
            res = editar_contacto()
            preguntar = False
            if not res:
                app()
        elif opcion == 3:
            ver_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 0:
            print('Adios')
            return
        else:
            print('Opcion Invalida, intente de nuevo')


def mostrarMenu():
    print('Menu, digite la opcion deseada:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contacto')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')
    print('0) Salir')

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

app()