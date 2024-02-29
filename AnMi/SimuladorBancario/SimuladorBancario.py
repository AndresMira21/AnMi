from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT 

class SimuladorBancario:
    # Aqui va el codigo
    '''-----------------------------
    # Atributos
    -----------------------------'''
    Cedula = ""
    Nombres = ""
    MesActual = ""

    '''---------------------------------
    # Asociaciones 
    ---------------------------------'''
    cuentaahorros = CuentaAhorros()
    cuentacorriente = CuentaCorriente()
    cuentacdt = CDT()

    '''-----------------------------
    # Metodos
    -----------------------------'''
    def ConsignarValor(self, ValoraConsignar):
        # Codigo

        # ValoraConsignar + saldo = saldo
        # return "Su saldo ahora es de: "+saldo 
        return ''

    def RetirarValor(self, ValoraRetirar):
        # Codigo

        # ValoraRetirar - saldo = saldo
        # return "Su saldo disponible es de: "+saldo
        return ''
    
    def DarInteresMensual(self):
        # Codigo

        # 
        return ''

    def ConsignarCuentaCorriente(self,nvalor):
        return self.cuentacorriente.ConsigarValor(nvalor)


    def CalcularSaldoTotal(self):
        return self.cuentaahorros.ConsultarSaldo() + self.cuentacorriente.ConsultarSaldo() + self.cuentacdt.ConsultarSaldo()
    
    def PasarAhorrosACorriente(self):
        # Forma 1
        self.cuentacorriente.ConsigarValor(self.cuentaahorros.ConsultarSaldo()) 
        self.cuentaahorros.RetirarValor(self.cuentaahorros.ConsultarSaldo())
        # Forma 2
        saldoAhorros = self.cuentaahorros.ConsultarSaldo()
        self.ConsignarCuentaCorriente(saldoAhorros)
        self.cuentaahorros.RetirarValor(self, saldoAhorros)

    def ConsultarSaldoCorriente(self):
        return 'Tu saldo es: '+self.cuentacorriente.ConsultarSaldo()

    def RetirarTodo(self, monto):
        total = self.CalcularSaldoTotal()
        self.cuentacorriente.RetirarValor(self.cuentacorriente.ConsultarSaldo())
        self.cuentaahorros.RetirarValor(self.cuentaahorros.ConsultarSaldo())
         
    def DuplicarAhorro(self):
        # Forma 1
        self.cuentaahorros.ConsigarValor(self.cuentaahorros.ConsultarSaldo())
        # Forma 2 no se utiliza
        self.cuentaahorros.saldo *= 2