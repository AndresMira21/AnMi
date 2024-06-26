class Transaccion:

    '''----------------------------------------
    ----------------------------------------'''
    fecha = ''
    TIPO = {
        1: 'Venta',
        2: 'ABASTECIMIENTO'
    }
    
    def __init__(self, tipo, cantidad, fecha):
        self.__fecha = fecha
        self.__tipo = self.TIPO['1'] if tipo==1 else self.TIPO['2']
        self.__cantidad = cantidad

    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, tipo):
        self.__tipo = tipo
    
    def getFecha(self):
        return self.__fecha
    
    def setFecha(self, fecha):
        self.__fecha = fecha

    def getCantidad(self):
        return self.__cantidad
    
    def setCantidad(self, cantidad):
        self.__cantidad = cantidad