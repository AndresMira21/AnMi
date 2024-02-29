class CDT:
    # Aqui va el codigo 
    '''---------------------------------------------
    # Atributos
    ---------------------------------------------'''
    ValorInversion = ""
    InteresMensual = ""
    MesApertura = ""

    '''---------------------------------------------
    # Metodos
    ---------------------------------------------'''
    
    def ConsultarSaldo(self):
        return self.saldo

    def ConsigarValor(self, nvalor):
        self.saldo += nvalor 
    
    def RetirarValor(self, retvalor):
        self.saldo -= retvalor 