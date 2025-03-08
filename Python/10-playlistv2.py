playlist={}
playlist['canciones']=[]

def crear_playlist():
    nombre_playlist=input('Como deseas nombrar tu playlist?:\n')
    playlist[nombre_playlist]=[]
    return nombre_playlist

def agregar_canciones(playlist_nombre):
    print('Agregando canciones a la playlist:', playlist_nombre)
    while True:
        cancion=input('Ingresa el nombre de la cancion (o "X" para salir):')
        if cancion.lower()=='x':
            break
        playlist[playlist_nombre].append(cancion)
        print('Cancion agregada:', cancion)

def eliminar_canciones(playlist_nombre):
    print('Eliminando canciones de la playlist:', playlist_nombre)
    while True:
        cancion_eliminar=input('Ingresa el nombre de la cancion a eliminar (o "X" para salir:)')
        if cancion_eliminar.lower()== 'x':
            break
        if cancion_eliminar in playlist[playlist_nombre]:
            playlist[playlist_nombre].remove(cancion_eliminar)
            print('Cancion eliminada:', cancion_eliminar)
        else:
            print('La cancion no se encuentra la playlist')
        print('Playlist actualizada')
        print(playlist)

def app():
    while True:
        print("\Menu:")
        print("1.-Crear nueva playlist")
        print("2.-Agregar canciones a una playlist")
        print("3.-Eliminar canciones de una playlist")
        print("4.-Mostrar todas las playlist")
        print("5.-Salir")

        opcion=input("Selecciona una opcion:")

        if opcion=='1':
            nombre_playlist=crear_playlist()
            agregar_canciones(nombre_playlist)
        elif opcion=='2':
            nombre_playlist=input("A que playlist deseas agregar canciones")