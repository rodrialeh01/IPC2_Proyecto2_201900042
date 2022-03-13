from .NodoCabecera import NodoCabecera

class ListaCabecera:
    def __init__(self, coordenada):
        self.cabeza = None
        self.cola = None
        self.coordenada = coordenada
        self.tamanio = 0

    def Vacio(self):
        return self.cabeza == self.cola == None

    def InsertarNodoCabecera(self, nuevo):
        if self.Vacio():
            self.cabeza = self.cola = nuevo
        else:
            if nuevo.id < self.cabeza.id:
                nuevo.siguiente = self.cabeza
                self.cabeza.anterior = nuevo
                self.cabeza = nuevo
            elif nuevo.id > self.cola.id:
                self.cola.siguiente = nuevo
                nuevo.anterior = self.cola
                self.cola = nuevo
            else:
                actual = self.cabeza
                while actual != None:
                    if nuevo.id < actual.id:
                        nuevo.siguiente = actual
                        nuevo.anterior = actual.anterior
                        actual.anterior.siguiente = nuevo
                        actual.anterior = nuevo
                        break
                    elif nuevo.id > actual.id:
                        actual = actual.siguiente
                    else:
                        break
        self.tamanio += 1

    def mostrarCabeceras(self):
        actual = self.cabeza
        while actual != None:
            print('Coordenada '+ self.coordenada + ' -> '+ str(actual.id))
            actual = actual.siguiente

    def getCabecera(self, id):
        actual = self.cabeza
        while actual != None:
            if id == actual.id:
                return actual
            actual = actual.siguiente

'''
filas = ListaCabecera('X')
n8 = NodoCabecera(8)
n6 = NodoCabecera(6)
n10 = NodoCabecera(10)
n7 = NodoCabecera(7)
n9 = NodoCabecera(9)
filas.InsertarNodoCabecera(n8)
filas.InsertarNodoCabecera(n6)
filas.InsertarNodoCabecera(n10)
filas.InsertarNodoCabecera(n7)
filas.InsertarNodoCabecera(n9)
filas.mostrarCabeceras()
'''