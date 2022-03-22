class NodoRobot():
    def __init__(self,tipo, nombre, capacidad):
        self.tipo = tipo
        self.nombre = nombre
        self.capacidad = capacidad
        self.siguiente = None
        self.anterior = None