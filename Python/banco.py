billetera = int(700)
cuenta={
    'dueño': 'Julio',
    'saldo': int(1000),
    'clave': '80085'
}

def login():
    user=input(f'Bienvenido al sistema, por favor ingrese su usuario\r\n')
    if user==cuenta['dueño']:
        password=(input('Excelente '+ user +' por favor ingrese su contraseña\r\n'))
        if password==cuenta['clave']:
            menu()
        elif password!=cuenta['clave']:
            print('Clave invalida, vuelvalo a intentar\r\n')
            login()
    elif user!=cuenta['dueño']:
        print('Usuario invalido, vuelvalo a intentar\r\n')
        login()

def usuario():
    nuevo=input('Ingrese el nuevo propetario de la cuenta\r\n')
    confirm=input('Por favor confirme su identidad\r\n')
    if confirm==cuenta['clave']:
        cuenta['dueño']=nuevo
        print(f'Operacion exitosa, bienvenido '+ nuevo)
    elif confirm!=cuenta['clave']:
        print(f'Clave erronea, cerrando proceso de cambio de usuario...')

def transfe():
    try:
        meter=int(input('Ingrese la monto a transferir\r\n'))
        if meter<=billetera:
            cuenta['saldo']= cuenta['saldo']+meter
            print(f'¡Transaccion exitosa!')
        elif meter>billetera:
             print(f'Monto insuficiente')
    except ValueError:
        print(f'Datos invalidos, verifique nuevamente')       

def retiro():
    try:
        retirar=int(input('Ingrese el monto a retirar\r\n'))
        if retirar<=cuenta['saldo']:
            cuenta['saldo']= cuenta['saldo']-retirar
            print(f'¡Transaccion exitosa!')
        elif retirar>cuenta['saldo']:
            print(f'Saldo insuficiente')
        else:
            print(f'Informacion invalida')
    except ValueError:
        print(f'Datos invalidos, verifique nuevamente')     



def menu():
    print('Bienvenido!\r\n')
    print('1: Retirar dinero de tu cuenta\r\n')
    print('2: Ingresar dinero a tu cuenta\r\n')
    print('3: Consultar saldo de la cuenta\r\n')
    print('4: Cambiar el propetario de la cuenta\r\n')

    try:
        opcion =int(input('Ingresa tu eleccion: '))
        if opcion == 1:
            retiro()
        
        elif opcion == 2:
            transfe()

        elif opcion == 3:
            print(f'Aqui tienes!{cuenta}')

        elif opcion == 4:
            usuario()

    except ValueError:
        print(f'Opcion invalida, vuelve a intentar')

login()

continuamenu='si'
while continuamenu=='si':
    menu()
    continuamenu=input('¿Desea realizar otra operación?\r\n')
    if continuamenu != "si":
        print('¡Hasta luego!')