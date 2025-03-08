class Carro:

    def __init__(self, marca, modelo, color):
        self._marca = marca #Protected, Unicamente en esta clase
        self.__modelo = modelo #Private, solamente a travez de los metodos
        self.color = color #Public, por defecto
        self.encendido = False

    #GET acceder, SET modificar, todo para modificar atributos de un objeto fuera de la clase

    def get_marca(self):
        print(self.__marca)

    def set_marca(self, marca):
        self.__marca = marca

    def encender(self):
        self.encendido = True
        print(f"El carro ha encendido({self.__marca}, {self.__modelo}).")
    
    def apagar(self):
        self.encendido = False
        print("El carro se ha apagado")

    def acelerar(self):
        if self.encendido:
            print("El carro esta acelerando")
        else:
            print("El carro debe estar encendido para acelerar")

mi_carro = Carro("Toyota", "Crolla", "Blanco")
mi_carro.marca="Mitsubishi"
mi_carro.set_marca("Lotus")

print(mi_carro.marca)

mi_carro.enceder()
mi_carro.acelerar()
