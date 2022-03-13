from .NodoCiudad import NodoCiudad

class ListaCiudades:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def Vacio(self):
        return self.cabeza == self.cola == None

    def InsertarCiudad(self, nombre, filas, columnas):
        nuevo = NodoCiudad(nombre,filas,columnas)
        if self.Vacio():
            self.cabeza = self.cola = nuevo
        elif self.cabeza == self.cola:
            self.cola = nuevo
            self.cola.anterior = self.cabeza
            self.cabeza.siguiente = self.cabeza
        else:
            nuevo.anterior = self.cola.anterior
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamanio += 1