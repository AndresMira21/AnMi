from Fecha import Fecha

class Empleado:
    # Aqui va el codigo del empleado
    '''--------------------------------------
    # Atributos
    --------------------------------------'''
    
    nombre = ''
    apellido = ''
    '''------------------------------------
    # 1 = Masculino 2 = Femenino
    ------------------------------------'''
   
    sexo = 0
    salario = 0

    '''---------------------------------
    # Asociaciones
    ---------------------------------'''

    fechaNacimiento = Fecha()
    fechaIngreso = Fecha()

    '''----------------------------------
    # Metodos
    ----------------------------------'''
    
    def CambiarSalario(self, nuevoSalario):
        # Aqui va el codigo
        return 0
    
    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        # Codigo aqui
        return None
    
    def ConsultarSalario(self):
        # Codigo
        return self.salario

    def ConsultarNombre(self):
        # Codigo
        return self.nombre
    
    def ConsultarApellido(self):
        # Codigo
        return self.apellido
    
    def ConsultarNombreCompleto(self):
        # Codigo
        return self.nombre +" "+ self.apellido

    def AumentoSalarial(self):
        nSalario = self.salario * 0.05
        nSalario = nSalario + self.salario
        self.salario = nSalario
        return "El nuevo salario es de: "+self.salario

    def DuplicarSalario(self):
        # Aqui va el codigo
        # Forma 1
        # self.salario = self.salario*2
        # Forma 2 pro
        self.salario *= 2       

    def CalcularSalarioAnual(self):
        # Codigo
        # Forma 1
        salarioanual = self.salario * 12 
        return salarioanual
        # Forma 2
        # return self.salario * 12

        def ConsultarDiaCumpleanios(self):
            return 'El dia de su cumpleaños es : '+self.fechaNacimiento.ConsultarDia()

        def CalcularImpuesto(self):
            # Forma 1
            total = self.CalcularSalarioAnual()
            return (total * 19.5) / 100

            # Forma 2
            #return self.CalcularSalarioAnual() * 0.195
        
