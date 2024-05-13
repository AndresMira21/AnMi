from Libro import Libro

class TiendaLibros:
    
    def __init__(self):
        self.__caja= 1000000
        self.__catalogo =[] 

    def getCatalogo(self):
        return self.__catalogo
    
    def getCaja(self):
        return self.__caja
    
    def setCaja(self, caja):
        self.__caja = caja
    
    def BuscarLibroPorTitulo(self, titulo):
        libroBuscado = None

        for libro in self.__catalogo:
            if libro.getTitulo() == titulo:
                libroBuscado = libro
                break

        return libroBuscado
    
    def BuscarLibroPorISBN(self, isbn):
        libroBuscado = None

        for libro in self.__catalogo:
            if libro.getIsbn() == isbn:
                libroBuscado = libro
                break

        return libroBuscado
    
    def registrarLibro(self, titulo, isbn, precioCompra, precioVenta, cantidadActual, rutaImagen):

        buscar = self.BuscarLibroPorISBN(isbn)
        nuevo = None

        if buscar == None:
            nuevo = Libro(titulo, isbn, precioCompra, precioVenta, cantidadActual, rutaImagen)
            self.__catalogo.append(nuevo)
        
        return nuevo
    
    def EliminarLibro(self, isbn):
        buscar = self.BuscarLibroPorISBN(isbn)
        eliminado = False

        if buscar:
            if buscar.getCantidadActual() == 0:
                self.__catalogo.remove(buscar)
                eliminado = True
            
        return eliminado 
            
    def DarLibroMasEconomico(self):
        menosCostoso = None
        
        if(len(self.__catalogo)>0):
            menosCostoso = self.__catalogo[0]
            for libro in self.__catalogo:
                if libro.getPrecioVenta() < menosCostoso.getPrecioVenta():
                    menosCostoso = libro   

        return menosCostoso

    def DarLibroMasCostoso(self):
        masCostoso = None
        
        if(len(self.__catalogo)>0):
            masCostoso = self.__catalogo[0]
            for libro in self.__catalogo:
                if libro.getPrecioVenta() > masCostoso.getPrecioVenta():
                    masCostoso = libro   

        return masCostoso
    
    def Vender(self, cantidad, fecha, isbn, titulo=None):
        vendido = False
        buscado = self.BuscarLibroPorISBN(isbn)

        if titulo is not None and buscado is None:
        # if titulo and not buscado: 
            buscado = self.BuscarLibroPorTitulo(titulo)

        if buscado:
            vendido = buscado.vender(cantidad, fecha)
            self.setCaja(self.getCaja+(cantidad*buscado.getPrecioVenta()))

        return vendido 

    def abastecer(self, isbn, cantidad, fecha):
        buscado = False

        if buscado:
            abastecer = buscado.abastecer(cantidad, fecha)
            self.setCaja(self.getCaja-(cantidad*buscado.get))
