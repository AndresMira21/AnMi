class CuentaCorriente:
    # Aqui va el codigo del empleado
    '''--------------------------------
    # Atributos
    --------------------------------'''
    saldo = 0

    '''--------------------------------------
    # Metodos
    --------------------------------------'''

    def ConsultarSaldo(self):
        return self.saldo

    def ConsigarValor(self, nvalor):
        self.saldo += nvalor 
    
    def RetirarValor(self, retvalor):
        retvalor = retvalor * 0.01
        self.saldo -= retvalor 