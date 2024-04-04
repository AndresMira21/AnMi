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
        if cantidad <self.__cantidadBodega and self.__cantidadBodega < self.__cantidadMinima:
            return 'recibirxd'
        else:
    
    def CambiarValorUnitario(self):
        if(self.__valorUnitario == self.__tipo=='FARMACIA' or self.__tipo=='PAPELERIA'):
            self.__valorUnitario -= self.__valorUnitario*0.1
        elif(self.__valorUnitario == self.__tipo=='SUPERMERCADO'):
            self.__valorUnitario += self.__valorUnitario*0.05
    



        para la clase Producto 
        aumentar el vallor unitario del producto utilizando la siuiente politica: 
        si el producto cuesta menos de mil aumentar el 1% si cuesta entre mil y '5mil' aumentar el 2% si cuesta mas de '5mil' aumentar el 3%
        el metodo se llamara subirValorUnitario

        recibir un pedidio solo si en la bodega se tiene menos unidades undicada en el tope minimo en caso contrario el metodo no debe hacer nada
        el metodo se llama hacerPedido y tiene un parametro

        modificar el precio del producto utilizando la siguiente politica: si el producto es de drogueria o papeleria debe disminuir un 10%, si es de supermercado debe aumentar un 5%, 
        el metodo se llama cambiarValorUnitario

        Par la clase tienda
        vender una cierta cantidad de producto cuyo nombre es igual al recibido como parametro, el metodo retorna el numero de unidades efectivamente vendidas, 
        suponga que el nombre que se recibe com parametro corresponde a uno de los producto de la tienda. utilice el metodo vender de la clase Producto como parte de su solucion
        el metodo se llamara venderProducto y recibe dos parametros: nombreproducto y cantidad

        calcula el numero de producto de papeleria que se venden en la tienda
        el metodo se llama cuantosPapeleria





           


