class Empleado:
    # Aqui va el codigo del empleado

    '''--------------------------------------
    # Atributos
    --------------------------------------'''
    nombre = 'Pepito'
    apellido = 'Lopez'
    
    '''------------------------------------
    # 1 = Masculino 2 = Femenino
    ------------------------------------'''
    sexo = 0
    salario = 0

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