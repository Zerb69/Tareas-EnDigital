playlist={}
playlist['canciones']=[]

def app():
    agregar_playlist=True
    while agregar_playlist:
        nombre_playlist=input('Como deseas nombrar tu playlist:\n')

        if nombre_playlist:
            playlist['nombre']=nombre_playlist
            agregar_playlist=False
            agregar_canciones()
            mostrar_resumen()

def agregar_canciones():
    print('Agregando canciones a la playlist:', playlist['nombre'])
    while True:
        cancion=input('Ingresa el nombre de la cancion(o "X" para salir): ')
        if cancion.lower() == 'x':

            break

        playlist['canciones'].append(cancion)
        print('Cancion agregada:', cancion)

        print('Playlist actualizada!')
        print(playlist)

def mostrar_resumen():
    print(f'Plaulist', playlist['nombre'])
    print('Canciones de la playlist:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()