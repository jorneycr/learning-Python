import os

from Contacto import Contacto

CARPETA = 'contactos/'
EXTENSION = '.txt'

def app():
    crear_directorio()
    mostrarMenu()

    preguntar = True
    while preguntar:
        opcion = input('Selecione una opcion: \r\n')
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            ver_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion Invalida, intente de nuevo')

def agregar_contacto():
    print('Escriba los datos para el nuevo contacto')
    nombre_contacto = input('Nombre de Contacto:\r\n')

    with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

        tel_contacto = input('Agrega telefono:\r\n')
        categoria_contacto = input('Categoria contacto: \r\n')

        contacto = Contacto(nombre_contacto, tel_contacto, categoria_contacto)

        archivo.write('Nombre: ' + contacto.nombre + '\r\n')
        archivo.write('Tel: ' + contacto.tel + '\r\n')
        archivo.write('Categoria: ' + contacto.categoria + '\r\n')

        print('\r\n Contacto creado correctamente \r\n')


def editar_contacto():
    print('Editar contacto')

def ver_contacto():
    print('Ver contacto')

def buscar_contacto():
    print('Buscar contacto')

def eliminar_contacto():
    print('Eliminar contacto')

def mostrarMenu():
    print('Menu, digite la opcion deseada:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contacto')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)



app()