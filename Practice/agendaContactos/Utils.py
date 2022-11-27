import os

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

def ver_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')

def buscar_contacto():
    nombre = input('Seleciones el contacto que sea buscar: \r\n')
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('Informacion de contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
    except IOError:
        print('El archivo no existe!!!\r\n')
        return True

def eliminar_contacto():
    nombre = input('Seleciones el contacto que sea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n Eliminado correctamente')
    except expression  as identifier:
        print('Ese contacto no existe\r\n')
        print('Agregalo como nuevo contacto\r\n')
        agregar_contacto()

