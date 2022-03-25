from .NodoRobot import NodoRobot
class ListaRobots:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def Vacio(self):
        return self.cabeza == self.cola == None

    def agregarNodo(self, tipo, nombre, capacidad):
        nuevo = NodoRobot(tipo, nombre, capacidad)
        if self.Vacio():
            self.cabeza = self.cola = nuevo
        elif self.cabeza == self.cola:
            self.cola = nuevo
            self.cabeza.siguiente = self.cola
            self.cola.anterior = self.cabeza
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo

    def RetornarRobots(self, tipo):
        aux = []
        actual = self.cabeza
        while actual != None:
            if tipo == actual.tipo:
                aux.append(actual.nombre)
            actual = actual.siguiente
        return aux
        
    def RetornarRobot(self, nombre):
        actual = self.cabeza
        while actual != None:
            if nombre == actual.nombre:
                return actual
            actual = actual.siguiente
        
    def verificarNombre(self, nombre):
        actual = self.cabeza
        while actual != None:
            if nombre == actual.nombre:
                return True
            actual = actual.siguiente
        return False

    def __len__(self):
        return self.tamanio