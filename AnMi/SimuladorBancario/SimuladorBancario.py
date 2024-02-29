from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente

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

    def ConsignarCuentaCorriente(self,saldo):
        return self.cuentacorriente.ConsigarValor()


    def CalcularSaldoTotal(self):
        return 'El saldo total es de: '+self.cuentaahorros.ConsultarSaldo() + self.cuentacorriente.ConsultarSaldo()
    
    def PasarAhorrosaCorriente(self):
        import self.cuentaahorros, self.cuentacorriente, CuentaCorriente

    def ConsultarSaldoCorriente(self):
        return self.cuentacorriente.ConsultarSaldo()

    def RetirarTodo(self):
        # Codigo
        # self.cuentacorriente.RetirarValor() +- self.cuentaahorros.RetirarValor()
        return 0
    
    def DuplicarAhorro(self):
        self.saldo.CuentaAhorros = self.saldo.CuentaAhorros() * 2
        return self.saldo.CuentaAhorros
