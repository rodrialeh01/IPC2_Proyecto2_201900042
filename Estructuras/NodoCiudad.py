from .MatrizDispersa import MatrizDispersa
from .ListaRecursos import ListaRecursos
from .ListaUCiviles import ListaUCiviles
class NodoCiudad:
    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.matriz = MatrizDispersa()
        self.recursos = ListaRecursos()
        self.civiles = ListaUCiviles()
        self.anterior = None
        self.siguiente = None