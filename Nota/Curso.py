class curso:
    '''------------------------------
    # Atributos
    ------------------------------'''
    def __init__(self):
        self.__notas = [4, 5, 3, 2, 3.5, 1, 3.5, 4, 3.5, 5, 4.5, 4.2]

    '''------------------------------
    # Metodos
    ------------------------------'''
    def Arreglo(self):
        arreglo = len(self.__notas)
        return arreglo
    def darPromedio(self):
        promedio = sum(self.__notas) / len(self.__notas)
        return promedio
    
    def darProemdio2(self):
        suma = 0.0
        indice = 0
 
        while indice < 12:
            suma += self.__notas[indice]
            indice += 1
        return suma/indice 
        
    def calcularCantidadAprobados(self):
        aprobados = 0
        indice = 0
        
        while indice < 12:
            if (self.__notas[indice]>=3.0)and(self.__notas[indice]<=5.0):
                aprobados += 1
        return aprobados
    
    def calcularCantidadAprobados2(self):
        aprobados = 0
        for indice in range(12):
            if (self.__notas[indice]>=3.0)and(self.__notas[indice]<=5.0):
                aprobados +=1
        return aprobados
    
    def calcularCantidadAprobados3(self):
        aprobados = 0
        for nota in self.__notas:
            if nota >= 3.0 and nota <= 5.0:
                aprobados +=1
        return aprobados
    
    def calcularMayorNota(self):
        mayor_nota = 0
        for nota in self.__notas:
            if nota > mayor_nota:
                mayor_nota = nota
        return mayor_nota
            
    def hacerCurva(self):
        for indice in range(12):
            self.nota[indice] = self.__notas[indice]
            self.__notas[indice] < 5.0

    def hacerCurva2(self):
        for nota in self.__notas:
            aumento = 0.05 * nota
            pnota = min(nota + aumento, 5.0)
        return pnota

    def cambiarNotas(self):
        if self.__notas > 4.0:
            self.__notas -= 0.5
        elif self.__notas < 2.0:
            self.__notas += 0.5

    def darMenorNota(self):
        menor = self.__notas [0]
        for nota in self.__notas:
            if nota < menor:
                menor = nota
        return menor
    