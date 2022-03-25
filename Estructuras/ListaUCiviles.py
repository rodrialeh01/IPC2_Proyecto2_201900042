from .NodoUCiviles import NodoUCiviles
class ListaUCiviles:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def Vacio(self):
        return self.cabeza == self.cola == None

    def InsertarNodo(self,id,x,y):
        nuevo = NodoUCiviles(id,x,y)
        if self.Vacio():
            self.cabeza = self.cola = nuevo
        elif self.cabeza == self.cola:
            self.cola = nuevo
            self.cabeza.siguiente = self.cola
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamanio += 1
        print('se agrego el nodo id: ' + str(id))

    def retornarNodo(self,id):
        actual = self.cabeza
        while actual != None:
            if actual.id == id:
                return actual
            actual = actual.siguiente

    def __len__(self):
        return self.tamanio