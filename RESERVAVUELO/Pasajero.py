class Pasajero:

    def __init__(self, pCedula, pNombre):
        self.Cedula = pCedula
        self.Nombre = pNombre

    def getCedula(self):
        return self.Cedula
    
    def setCedula(self, pCedula):
        self.Cedula = pCedula

    def getNombre(self):
        return self.Nombre
    
    def setNombre(self, pNombre):
        self.Nombre = pNombre

    