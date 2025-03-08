class Medico:
    def __init__(self,cirugia,guardia,recepcion,diagnostico):
        self.cirugia=cirugia
        self.guardia=guardia
        self.recepcion=recepcion
        self.diagnostico=diagnostico
    def mostrar_informacion(self):
        print(f'La rutina del doctor es: {self.cirugia,self.guardia,self.recepcion,self.diagnostico}')

doctor = Medico('Operacion de emergencia', 'Cubrir horario nocturno este fin de semana', 'Atender la recepcion 3 horas diarias', 'Evaluacion de BMI para pacientes con sobre e infra peso')
doctor.mostrar_informacion()

class Clinica(Medico):
    def __init__(self, cirugia, guardia, recepcion, diagnostico, clinica_perteneciente, residenciado):
        super().__init__(cirugia, guardia, recepcion, diagnostico)
        self.clinica_perteneciente=clinica_perteneciente
        self.residenciado=residenciado

    def get_residenciado(self):
        return self.residenciado
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Clinica Perteneciente: {self.clinica_perteneciente}")
        print(f"Esta residenciado: {'Si' if self.residenciado else 'No'}")

doctor = Medico('Operacion de emergencia', 'Cubrir horario nocturno este fin de semana', 'Atender la recepcion 3 horas diarias', 'Evaluacion de BMI para pacientes con sobre e infra peso')
doctor.mostrar_informacion()

clinica=Clinica("Centro Medico Israel Ranuarez Balsa", True)
clinica.mostrar_informacion()