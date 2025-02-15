class Medico:
    def agregar_rutina(self,cirugia,guardia,recepcion,diagnostico):
        self.cirugia=cirugia
        self.guardia=guardia
        self.recepcion=recepcion
        self.diagnostico=diagnostico
    def mostrar(self):
        print(f'La rutina del doctor es: {self.cirugia,self.guardia,self.recepcion,self.diagnostico}')

doctor = Medico()
doctor.agregar_rutina('Operacion de emergencia', 
                      'Cubrir horario nocturno este fin de semana', 
                      'Atender la recepcion 3 horas diarias', 
                      'Evaluacion de BMI para pacientes con sobre e infra peso')
doctor.mostrar()