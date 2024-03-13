class LineaTelefonica:
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    
    # Numero de llamadas realizadas
    numeroLlamadas = ''
    
    # Numero de minutos consumidos
    numeroMinutos = ''
    
    # Costo total de las llamadas
    costoLlamadas = ''
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    # Inicializar el número de llamadas, número de minutos y costo de llamadas en 0.
    def __init__(self):
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0
        # TODO Parte2 PuntoA: Completar el método según la documentación dada.

    #Retorna el costo total de las llamadas realizadas.
    def darCostoLlamadas(self):
        # TODO Parte2 PuntoB: Completar el método según la documentación dada.
        return self.costoLlamadas

    # Retorna el número de llamadas realizadas por esta línea.
    def darNumeroLlamadas(self):
        # TODO Parte2 PuntoC: Completar el método según la documentación dada.
        return self.numeroLlamadas
    
    # Retorna el número de minutos consumidos.
    def darNumeroMinutos(self):
        # TODO Parte2 PuntoD: Completar el método según la documentación dada.
        return self.numeroMinutos
        
    # Reinicia la línea telefónica, dejando todos sus valores en cero.
    # post: El número de llamadas, número de minutos y costo de llamadas son 0.
    def reiniciar(self):
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0

        # TODO Parte2 PuntoE: Completar el método según la documentación dada.

    # Agrega una llamada local a la línea telefónica
    # post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 35 ).
    # :param pMinutos Número de minutos de la llamada. pMinutos >0.
    def agregarLlamadaLocal(self, pMinutos):
        
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += pMinutos
        # Suma el costo (costo por minuto: 35 pesos)
        self.costoLlamadas += pMinutos * 35

    """
        Agrega una llamada de larga distancia a la línea telefónica.
        
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 380 )
        
        :param pMinutos: Número de minutos de la llamada. pMinutos >0.
        """
    def agregarLlamadaLargaDistancia(self, pMinutos):
        
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.costoLlamadas += pMinutos * 380
        # TODO Parte2 PuntoF: Completar el método según la documentación dada.

    '''
        Agrega una llamada a celular a la lÍnea telefónica
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 999 )
        :param pMinutos Número de minutos de la llamada. pMinutos >0.
    '''
    def agregarLlamadaCelular(self, pMinutos):

        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.costoLlamadas += pMinutos * 999
        # TODO Parte2 PuntoG: Completar el método según la documentación dada.
       
