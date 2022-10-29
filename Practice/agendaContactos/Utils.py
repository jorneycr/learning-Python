import os

# from App import app
from Constantes import CARPETA, EXTENSION
from Contacto import Contacto


def agregar_contacto(self):
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
            # app()


