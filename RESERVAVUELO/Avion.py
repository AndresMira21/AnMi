from Silla import Silla
from Pasajero import Pasajero
class Avion:
    SILLAS_EJECUTIVAS = 8
    SILLAS_ECONOMICAS = 42

    def __init__(self):
        self.sillasEjecutivas = []
        self.sillasEconomicas = []

        # append() ; sirve para insertar valores
        self.definicionSillasEjectutivas()
        self.definicionSillasEconomicas()

    def definicionSillasEjectutivas(self):
        for i in range(self.SILLAS_EJECUTIVAS):
            if (i+1)%2 == 0:
                self.sillasEjecutivas.append((i+1), Silla.CLASE.eje, Silla.UBICACION.ventana)
            else:
                self.sillasEjecutivas.append((i+1), Silla.CLASE.eje, Silla.UBICACION.pasillo)

    def definicionSillasEconomicas(self):
        for i in range(self.SILLAS_ECONOMICAS):
            if 1<2:
                self.sillasEconomicas.append(1, Silla.CLASE.eco, Silla.UBICACION.ventana)
            elif 1<3:
                self.sillasEconomicas.append(1, Silla.CLASE.eco, Silla.UBICACION.pasillo)
            else:
                self.sillasEconomicas.append(1, Silla.CLASE.eco, Silla.UBICACION.centro)

    def contarSillasEjecutivasOcupadas(self):
        contador = 0
        for self.sillasEjecutivas in self.SILLAS_EJECUTIVAS:
            if self.sillasEjecutivas in self.definicionSillasEjectutivas():
                contador +=1
        return contador 
    
    def buscarPasajeroEjecutivo(self, pCedula):
    	for Silla in self.sillasEjecutivas:
            if Silla.sillaAsignada() and Silla.getPasajero().getCedula() == pCedula:
                return Silla
        return None
    
    def buscarSillaEconomicaLibre(self,pUbicacion):
        encontrado = False
        Silla = None
        i = 0
        while i < len(self.SILLAS_ECONOMICAS) and not encontrado:
            silla = self.sillasEconomicas[i]
            if not Silla.sillaAsignada() and Silla.getUbicacion() == pUbicacion:
                encontrado = True
            i += 1
        if not encontrado:
            Silla = None
        return Silla

    def asignarSillaEconomica(self, pUbicacion, pPasajero):
        for Silla in self.sillasEconomicas:
            if not Silla.sillaAsignada() and Silla.getUbicacion() == pUbicacion:
                Silla.asignarPasajero(pPasajero)
            return True
        return False

    def anularReservaEjecutivo(self, pCedula):
        for Silla in self.sillasEjecutivas:
            if Silla.sillaAsignada() and Silla.getPasajero().setCedula() == pCedula:
                Silla.designarSilla()
                return True
        return False  
    
    def contarVentanasEconomica(self):
        contador = 0
        for Silla in self.sillasEconomicas:
            if not Silla.sillaAsignada() and Silla.getUbicacion() == Silla.UBICACION.ventana:
                contador += 1
        return contador    

    def hayDosHomonimosEconomica(self):
        nombres = []
        for Silla in self.sillasEconomicas:
            if Silla.sillaAsignada():
                Pasajero = Silla.getPasajero()
                nombre = Pasajero.getNombre()
                if nombre in Pasajero.setNombre():
                    return True
                nombres.append(nombre)
        return False
    
    def contarSillasEconomicasLibres(self):
        contador = 0
        for Silla in self.sillasEconomicas:
            if not Silla.sillaAsignada():
                contador += 1
        return contador

    def contarPasilloEjecutivas(self):
        contador = 0
        for Silla in self.sillasEjecutivas:
            if not Silla.sillaAsignada() and Silla.getUbicacion() == Silla.UBICACION.pasillo:
                contador += 1
        return contador

    def desocuparAvion(self):
        for Silla in self.sillasEconomicas:
            Silla.designarPasajero()
        for Silla in self.sillasEjecutivas:
            Silla.designarPasajero()
               

            