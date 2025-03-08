class Restaurante:

    def __init__(self, nombre, categoria, precio):
        print("Yo me ejecuto automaticamente cuando creas un objeto de la clase")
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio
    def agregar_restaurante(self, nombre):
        self.nombre=nombre
        print(f"Agregar restaurante...{self.nombre}")

    def mostrar_informacion(self):
        print(f"El nombre del restaurante: {self.nombre} y es de la categoria: {self.categoria}")

restaurante =Restaurante("El pollo loco", "comida casual", 50)
restaurante.mostrar_informacion()

class Hotel(Restaurante):
    def __init__(self, nombre, categoria, precio, numero_habitaciones, piscina):
        super().__init__(nombre, categoria, precio)
        self.numero_habitaciones=numero_habitaciones
        self.tiene_piscina=piscina

    def get_piscina(self):
        return self.piscina
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Numero de habitaciones: {self.numero_habitaciones}")
        print(f"Tiene piscina: {'Si' if self.tiene_piscina else 'No'}")
    
restaurante=Restaurante("El pollo loco", "comida casual", 50)
restaurante.mostrar_informacion()

hotel=Hotel("Hotel POO", "5 estrellas", 500, 100, True)

hotel.mostrar_informacion()