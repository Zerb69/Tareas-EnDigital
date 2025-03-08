import os

def crear_archivo(nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Este es el contenido inicial del archivo. \n")
        print(f"Archivo {nombre_archivo} creado exitosamente")

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido =archivo.read()
            print(contenido)
    except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe")

def agregar_linea(nombre_archivo, nueva_linea):
     with open(nombre_archivo, "a") as archivo:
          archivo.write(nueva_linea + "\n")
          print("Linea agregada al archivo")

def eliminar_archivo(nombre_archivo):
     try:
          os.remove(nombre_archivo)
          print(f"Archivo {nombre_archivo} eliminado")
     except FileNotFoundError:
          print(f"El archivo {nombre_archivo} no existe")

nombre_archivo="mi_archivo.txt"
crear_archivo(nombre_archivo)
leer_archivo(nombre_archivo)
agregar_linea(nombre_archivo, "Esta es una nueva linea")
eliminar_archivo(nombre_archivo)