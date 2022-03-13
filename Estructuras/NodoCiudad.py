from .MatrizDispersa import MatrizDispersa
class NodoCiudad:
    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.matriz = MatrizDispersa()
        self.anterior = None
        self.siguiente = None