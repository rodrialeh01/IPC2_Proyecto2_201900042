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
            self.cabeza.siguiente = self.cola
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamanio += 1

    def retornarNodo(self, nombre):
        actual = self.cabeza
        while actual != None:
            if nombre == actual.nombre:
                return actual
            actual = actual.siguiente