def App():
    archivo =open('archivo.txt', 'w') #w: write, r: read, a: append
    for i in range(0,10):
        archivo.write(f"Esta es la linea {i}\n")
    archivo.close()
App()

#r: Solo lectura (default)
#w: Solo escritura (sobrescribe el archivo si existe)
#a: Añadir (añade al final del archivo)
#x: Crear (crea un nuevo archivo, si ya existe, lanza un error)
#b: Binario (para abrir archivos binarios)
#+: Leer y Escribir