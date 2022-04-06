from .NodoPila import NodoPila 
class Pila:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def Vacio(self):
        return self.primero == self.ultimo == None

    def Apilar(self, celda):
        nuevo = NodoPila(celda)
        if self.Vacio():
            self.primero = self.ultimo = nuevo
        elif self.primero == self.ultimo:
            self.primero = nuevo
            self.primero.siguiente = self.ultimo
        else:
            nuevo.siguiente = self.primero
            self.primero = nuevo
        self.tamanio += 1

    def Desapilar(self):
        if self.Vacio():
            self.primero = self.ultimo = None
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            actual = self.primero
            self.primero = actual.siguiente
        self.tamanio -= 1

    def Imprimir(self):
        actual = self.primero
        while(actual != None):
            print(actual.celda)
            actual = actual.siguiente

    def __len__(self):
        return self.tamanio
