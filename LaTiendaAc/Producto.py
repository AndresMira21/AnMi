from enum import Enum

'''------------------------------------------------
# Enumeraciones
------------------------------------------------'''
class Tipo(Enum):
    
    '''----------------------------------------------
    # Listado de enumeraciones
    ----------------------------------------------'''
    PAPELERIA = 1
    SUPERMERCADO = 2
    FARMACIA = 3

class Producto:
    
    '''-------------------------------------------
    # Constantes
    -------------------------------------------'''
    __IVA_PAPELERIA = 0.16
    __IVA_SUPERMERCADO = 0.04
    __IVA_FARMACIA = 0.12
    
    '''----------------------------------------
    # Atributo
    ----------------------------------------'''
    __nombre = None
    __tipo = Enum('Tipo',['PAPELERIA', 'SUPERMERCADO', 'FARMACIA'])
    __valorUnitario = 0.0
    __cantidadBodega = 0
    __cantidadMinima = 0
    __cantidadUnidadesVendidas = 0

    '''---------------------------------------
    # Metodos
    ---------------------------------------'''
    def __init__(self, tipo, pNombre, pValorUnitario, pCantidadBodega, pCantidadMinima):
        self.__tipo=tipo
        self.__nombre=pNombre
        self.__valorUnitario=pValorUnitario
        self.__cantidadBodega=pCantidadBodega
        self.__cantidadMinima=pCantidadMinima
        self.__cantidadUnidadesVendidas = 0

    def getNombre(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo
    
    def getValorUnitario(self):
        return self.__valorUnitario
    
    def getCantidadBodega(self):
        return self.__cantidadBodega
    
    def getCantidadMinima(self):
        return self.__cantidadMinima
    
    def getCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setValorUnitario(self, valorUnitario):
        self.__valorUnitario = valorUnitario

    def setCantidadBodega(self, cantidadBodega):
        self.__cantidadBodega = cantidadBodega

    def setCantidadMinima(self, cantidadMinima):
        self.__cantidadMinima = cantidadMinima

    def Vender(self, cantidad):
        if cantidad <= self.__cantidadBodega:
            self.__cantidadUnidadesVendidas += cantidad
            self.__cantidadBodega -= cantidad 
        else:
            print('Cantidad no disponible')
 
    def HaySuficiente(self, cantidad):
        # Forma 1
        if cantidad <= self.__cantidadBodega:
            return True
        else:
            return False
        # Forma 2
        haySuficiente = False
        if cantidad <= self.__cantidadBodega:
            haySuficiente = True
        return haySuficiente
        # Forma 3 ?
        return cantidad <= self.__cantidadBodega

    def DarIva(self):
        if(self.__tipo=='PAPELERIA'):
            return self.__IVA_PAPELERIA
        elif(self.__tipo=='FARMACIA'):
            return self.__IVA_FARMACIA
        elif(self.__tipo=='SUPERMERCADO'):
            return self.__IVA_SUPERMERCADO
        else:
            print('Categoria de producto no existe')

    def SubirValorUnitario(self):
        if(self.__valorUnitario < 1000.0):
            self.__valorUnitario += self.__valorUnitario*0.01
        elif(1000.0 <= self.__valorUnitario <= 5000.0):
            self.__valorUnitario += self.__valorUnitario*0.02
        elif(self.__valorUnitario > 5000.0):
            self.__valorUnitario += self.__valorUnitario*0.03

    def HacerPedido(self, cantidad):
        if self.__cantidadBodega < self.__cantidadMinima:
            self.__cantidadBodega + cantidad
            return 'Si hay suficiente producto'
    
    def CambiarValorUnitario(self):
        if Tipo.FARMACIA | Tipo.PAPELERIA:
            self.__valorUnitario -= self.__valorUnitario *0.1
        elif Tipo.SUPERMERCADO:
            self.__valorUnitario += self.__valorUnitario*0.05

    def nombreTipoProducto(self):
        if self.__tipo == Tipo.PAPELERIA:
            return 'EL producto es de tipo Papeleria'
        elif self.__tipo == Tipo.SUPERMERCADO:
            return 'EL producto es de tipo Supermercado'
        elif self.__tipo == Tipo.FARMACIA:
            return 'El producto es de tipo Farmacia'
        else:
            return 'El producto es de tipo desconocido'
    
    def aumentarValorUnitario(self):
        if self.__tipo == Tipo.FARMACIA:
            self.__valorUnitario += self.__valorUnitario*0.01
        elif self.__tipo == Tipo.SUPERMERCADO:
            self.__valorUnitario += self.__valorUnitario*0.03
        elif self.__tipo == Tipo. PAPELERIA:
            self.__valorUnitario += self.__valorUnitario*0.02

    

#Para la clase tienda
#vender una cierta cantidad de producto cuyo nombre es igual al recibido como parametro, el metodo retorna el numero de unidades efectivamente vendidas, 
#suponga que el nombre que se recibe com parametro corresponde a uno de los producto de la tienda. utilice el metodo vender de la clase Producto como parte de su solucion
#el metodo se llamara venderProducto y recibe dos parametros: nombreproducto y cantidad

#calcula el numero de producto de papeleria que se venden en la tienda
#el metodo se llama cuantosPapeleria





           


