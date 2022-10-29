import os
import time

from Constantes import CARPETA, EXTENSION
from Contacto import Contacto

def agregar_contacto():
        print('Escriba los datos para el nuevo contacto')
        nombre_contacto = input('Nombre de Contacto:\r\n')

        existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION)

        if not existe:
            with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

                tel_contacto = input('Agrega telefono:\r\n')
                categoria_contacto = input('Categoria contacto: \r\n')

                contacto = Contacto(nombre_contacto, tel_contacto, categoria_contacto)

                archivo.write('Nombre: ' + contacto.nombre + '\r\n')
                archivo.write('Tel: ' + contacto.tel + '\r\n')
                archivo.write('Categoria: ' + contacto.categoria + '\r\n')

                print('\r\n Contacto creado correctamente \r\n')
        else:
            print('\r\nEse contacto ya existe! \r\n')
            return existe

def editar_contacto():
    print('Escribe el nombre de contacto a editar')
    nombre_anterior = input('Cual contactot desea editar:\r\n')
    existe = existe_contacto(nombre_anterior)
    if existe:
        print('Puedes editar')
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            nombre_contacto = input('Agrega el nuevo nombre:\r\n')
            tel_contacto = input('Agrega el nuevo  telefono:\r\n')
            categoria_contacto = input('Agrega la nuevo categoria contacto: \r\n')

            contacto = Contacto(nombre_contacto, tel_contacto, categoria_contacto)

            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Tel: ' + contacto.tel + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            archivo.close()

            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            print('\r\n Contacto editado correctamente \r\n')

    else:
        print('No existe el contacto')
        return existe


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

def ver_contacto():
    print('Ver contacto')

def buscar_contacto():
    print('Buscar contacto')

def eliminar_contacto():
    print('Eliminar contacto')

