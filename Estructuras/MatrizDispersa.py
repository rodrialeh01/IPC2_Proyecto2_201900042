from .NodoCabecera import NodoCabecera
from .ListaCabecera import ListaCabecera
from .NodoCelda import NodoCelda

class MatrizDispersa():
    def __init__(self):
        self.filas = ListaCabecera('X')
        self.columnas = ListaCabecera('Y')

    def InsertarNodo(self, x, y, caracter):
        nuevo = NodoCelda(x, y, caracter)
        nodox = self.filas.getCabecera(x)
        nodoy = self.columnas.getCabecera(y)

        if nodox == None:
            nodox = NodoCabecera(x)
            self.filas.InsertarNodoCabecera(nodox)

        if nodoy == None: 
            nodoy = NodoCabecera(y)
            self.columnas.InsertarNodoCabecera(nodoy)

        if nodox.indicador == None:
            nodox.indicador = nuevo
        else:
            if nuevo.y < nodox.indicador.y:
                nuevo.derecha = nodox.indicador              
                nodox.indicador.izquierda = nuevo
                nodox.indicador = nuevo
            else:
                actual : NodoCelda = nodox.indicador 
                while actual != None:
                    if nuevo.y < actual.y:
                        nuevo.derecha = actual
                        nuevo.izquierda = actual.izquierda
                        actual.izquierda.derecha = nuevo
                        actual.izquierda = nuevo
                        break
                    elif nuevo.x == actual.x and nuevo.y == actual.y:
                        print('Se repite: ')
                        print('Coordenada X: ' + str(actual.x))
                        print('Coordenada Y: ' + str(actual.y))
                        break
                    else:
                        if actual.derecha == None:
                            actual.derecha = nuevo
                            nuevo.izquierda = actual
                            break
                        else:
                            actual = actual.derecha

        
        if nodoy.indicador == None: 
            nodoy.indicador = nuevo
        else: 
            if nuevo.x < nodoy.indicador.x:
                nuevo.abajo = nodoy.indicador
                nodoy.indicador.arriba = nuevo
                nodoy.indicador = nuevo
            else:
                actual2 : NodoCelda = nodoy.indicador
                while actual2 != None:
                    if nuevo.x < actual2.x:
                        nuevo.abajo = actual2
                        nuevo.arriba = actual2.arriba
                        actual2.arriba.abajo = nuevo
                        actual2.arriba = nuevo
                        break
                    elif nuevo.x == actual2.x and nuevo.y == actual2.y:
                        print('Se repite: ')
                        print('Coordenada X: ' + str(actual.x))
                        print('Coordenada Y: ' + str(actual.y))
                        break
                    else:
                        if actual2.abajo == None:
                            actual2.abajo = nuevo
                            nuevo.arriba = actual2
                            break
                        else:
                            actual2 = actual2.abajo
        
        print('Se añadio el nuevo nodo en la coordenada ' + str(self.filas.coordenada) + ': ' + str(nuevo.x) + ', coordenada ' + str(self.columnas.coordenada)+ ': ' + str(nuevo.y)+ '\n Con el caracter: "' +str(nuevo.caracter) + '"')

