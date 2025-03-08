class Carro:
    def agregar_carro(self,marca,modelo,cilindrada):
        self.marca= marca
        self.modelo= modelo
        self.cilindrada= cilindrada
        print(f"agregar carro...{self.marca, self.modelo, self.cilindrada}")
    def mostrar_informacion(self):
        print(f"Las caracteristicas del vehiculo son...{self.marca, self.modelo, self.cilindrada}")


car = Carro()
car.agregar_carro("Renault","Clio","Inline-6")
car.mostrar_informacion()