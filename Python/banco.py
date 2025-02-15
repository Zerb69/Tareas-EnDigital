cuenta={
    'dueño': 'Julio',
    'saldo': '1000$'
}
def menu():
    print('Bienvenido!\r\n')
    print('1: Retirar dinero de tu cuenta\r\n')
    print('2: Ingresar dinero a tu cuenta\r\n')
    print('3: Consultar dinero de la cuenta\r\n')
    print('4: Salir\r\n')

    opcion = input('Ingresa tu eleccion: ')
    if opcion == 1:
        print(f'Prueba')
        
    elif opcion == 2:
        print(f'Prueba')

    elif opcion == 3:
        print(f'Aqui tienes!{cuenta}')

    elif opcion == 4:
        (f'Hasta luego!')
menu()

