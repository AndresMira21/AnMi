class Silla: 
    # {} es un objeto, diccionario; [] es un arreglo
    #clase = ['ejecutiva','economica']

    #clase = {
        #'eje': 'Ejecutiva' ,
        #'eco': 'Economica'
    #}

    #persona = {
        #'nombre' : 'Juan',
        #'apellido' : 'Gonzales',
        #'fNacimiento': '1-1-2000'
    #}

    CLASE = {
        'eje' : 'Ejecutiva',
        'eco' : 'Economica'
    }

    UBICACION = {
        'ventana' : 'Ventana',
        'centro' : 'Centro',
        'pasillo' : 'Pasillo'
    }

    def __init__(self, pNumero, PClase, pUbicacion):
        self.__numero = pNumero
        # Operador ternario 
        # Forma 1 - operador pClase debe ser true or false                                                                                                                                                                
        self.__clase = (self.CLASE.eje, self.CLASE.eco)[PClase]  
        # Forma 2
        # self.clase = self.CLASE.eje if pClase=='Ejecutiva' else self.CLASE.eco
        if pUbicacion == 'ventana':
            self.__ubicacion = self.UBICACION.ventana
        elif pUbicacion == 'centro':
            self.__ubicacion = self.UBICACION.centro
        elif pUbicacion == 'pasillo':
            self.__ubicacion = self.UBICACION.pasillo 
        else:
            self.__ubicacion = None 

        self.__pasajero=None 

    def asignarPasajero(self, pPasajero):
        self.__pasajero=pPasajero

    def designarSilla(self):
        self.__numero=None

    def sillaAsignada(self):
        return True if self.__numero==None else False
    
    def getNumero(self):
        return self.__numero 
    
    def getClase(self):
        return self.__clase
    
    def getUbicacion(self):
        return self.__ubicacion
    
    def getPasajero(self):
        return self.__pasajero 
    