playlist  = {} #Diccionario vacio
playlist['canciones'] = [] #lista vacia de canciones

def app():
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('Como deseas nombrar la playlist?\r\n ')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

            agregar_playlist = False
            agregar_canciones()

def agregar_canciones():
    agregar_canciones = True

    while agregar_canciones:
        nombre_playlist = playlist['nombre']
        pregunta = f'Agrega canciones para la playlist {nombre_playlist} \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'

        cancion = input(pregunta)

        if cancion == 'X':
            agregar_canciones = False

            mostrar_resumen()
        else:
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones \r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()