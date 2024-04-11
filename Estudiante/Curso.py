from enum import Enum
class Departamento(Enum):
    MATEMATICAS = 1
    FISICA = 2
    SISTEMAS = 3
    BIOLOGIA = 4

class Curso:
    '''--------------------------------------
    # Atributos 
    --------------------------------------'''
    MINIMA = 1.5
    MAXIMA = 5.0
    codigo = ''
    nomre = ''
    Departamento = Enum ('Departamento',['MATEMATICAS', 'FISICA', 'SISTEMAS', 'BIOLOGIA'])
    creditos = 0
    nota = 0