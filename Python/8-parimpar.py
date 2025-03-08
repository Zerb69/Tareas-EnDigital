pregunta = input('Pon un numero y te digo si es par o impar\r\n')
pregunta = '\r\n escribe "cerrar" para salir de la app\r\n'
preguntar= True

while True:
    numero=input("Ingresa un numero (o escribe 'cerrar' para salir):")
    if numero.lower()=="cerrar":
        break
    try:
        numero=int(numero)
        if numero %2==0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")
    except ValueError:
        print("Por favor ingresa un numero valido")