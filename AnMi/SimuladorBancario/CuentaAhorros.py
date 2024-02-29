class CuentaAhorros:
    # Aqui va el codigo del empleado
    '''---------------------------------------
    # Atributos
    ----------------------------------------'''
    saldo = ""
    interesmensual = ""

    '''--------------------------------------
    # Metodos
    --------------------------------------'''

    def ConsultarSaldo(self):
        return self.saldo

    def ConsigarValor(self, nvalor):
        self.saldo += nvalor 
    
    def RetirarValor(self, retvalor):
        self.saldo -= retvalor 