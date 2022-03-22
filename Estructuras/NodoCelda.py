class NodoCelda:
    def __init__(self, x, y, caracter, capacidad):
        self.x = x
        self.y = y
        self.caracter = caracter
        self.capacidad = capacidad
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None
