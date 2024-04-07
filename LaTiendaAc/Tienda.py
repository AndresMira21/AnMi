from Producto import Producto

class Tienda:
    
    '''----------------------------------------------------
    # Atributos
    ----------------------------------------------------'''
    #__producto1 = None
    #__producto2 = None
    #__producto3 = None
    #__producto4 = None

    '''----------------------------------------------------
    # Metodos
    ----------------------------------------------------'''
    def __init__(self):
        self.__producto1 = Producto('Papeleria', 'Lapiz', '500.0', '30', '9')
        self.__producto2 = Producto('Papeleria', 'Borrador', '300.0', '15', '5')
        self.__producto3 = Producto('Supermercado', 'Kilo de cafe', '5600.0', '20', '10')
        self.__producto4 = Producto('Drogueria', 'Desinfectante', '3200.0', '12', '11')
        self.dineroEnCaja = 0
    
    def getProducto1(self):
        return self.__producto1
    
    def getProducto2(self):
        return self.__producto2 
    
    def getProducto3(self):
        return self.__producto3
    
    def getProducto4(self):
        return self.__producto4
    
    def getdineroEnCaja(self):
        return self.__dineroEnCaja
    
    def venderProducto(self, nombreProducto, cantidad):
        return
    
    def cuantosPapeleria(self):
        return 0

    def darPrecioProducto(self, pNumeroProducto):
        if pNumeroProducto == 1:
            return self.__producto1.getValorUnitario()
        elif pNumeroProducto == 2:
            return self.__producto2.getValorUnitario()
        elif pNumeroProducto == 3:
            return self.__producto3.getValorUnitario()
        elif pNumeroProducto == 4:
            return self.__producto4.getValorUnitario()
        
    def darPrecioProducto(self, pNumeroProducto):
        if pNumeroProducto == self.__producto1.getNombre():
            return self.__producto1.getValorUnitario()
        elif pNumeroProducto == self.__producto2.getNombre():
            return self.__producto2.getValorUnitario()
        elif pNumeroProducto == self.__producto3.getNombre():
            return self.__producto3.getValorUnitario()
        elif pNumeroProducto == self.__producto4.getNombre():
            return self.__producto4.getValorUnitario()