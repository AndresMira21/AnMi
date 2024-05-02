from Silla import Silla

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
            if x<x:
                self.sillasEconomicas.append(x, Silla.CLASE.eco, Silla.UBICACION.ventana)
            elif x<x:
                self.sillasEconomicas.append(x, Silla.CLASE.eco, Silla.UBICACION.pasillo)
            else:
                self.sillasEconomicas.append(x, Silla.CLASE.eco, Silla.UBICACION.centro)