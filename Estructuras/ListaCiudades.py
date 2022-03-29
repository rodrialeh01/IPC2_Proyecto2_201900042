from .NodoCiudad import NodoCiudad
from .NodoCelda import NodoCelda
import os
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

    def verificarNombre(self, nombre):
        actual = self.cabeza
        while actual != None:
            if nombre == actual.nombre:
                return True
            actual = actual.siguiente
        return False

    def GraficarMatriz(self, nodo):
        contenido = ''
        file = open('MapasGenerados/Matriz_' + str(nodo.nombre) + '.dot', 'w')
        contenido += '''digraph structs {
	node [shape=plaintext]
	patron [fontsize="40pt", label=<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="2" CELLPADDING="20">\n'''
        filas = int(nodo.matriz.filas.tamanio)
        columnas = int(nodo.matriz.columnas.tamanio)
        matrizc = nodo.matriz
        contenido += '''<TR>
    <TD border="0">'''+str(nodo.nombre)+'''</TD>'''
        for i in range(columnas):
            contenido += '<TD border="0">'+ str(i+1) + '</TD>'
        
        contenido += '\n</TR>'

        for i in range(filas):
            contenido += '''\n<TR>
        <TD border="0">'''+str(i+1)+'''</TD>'''

            for j in range(columnas):
                if nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == '*':
                    contenido+="\n<TD bgcolor=\"black\">   </TD>"
                elif nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'E':
                    contenido+="\n<TD bgcolor=\"yellowgreen\">   </TD>"
                elif nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'C':
                    contenido+="\n<TD bgcolor=\"royalblue1\">   </TD>"
                elif nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'R':
                    contenido+="\n<TD bgcolor=\"grey39\">   </TD>"
                elif nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'M':
                    contenido+="\n<TD bgcolor=\"red3\">   </TD>"
                elif nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == ' ':
                    contenido+="\n<TD>   </TD>"
            contenido += '</TR>'
        contenido += '''</TABLE>>]
}'''

        file.write(contenido)
        file.close()
        os.system('dot -Tpng MapasGenerados/Matriz_'+str(nodo.nombre)+'.dot -o MapasGenerados/Matriz_'+str(nodo.nombre)+'.png')
        #os.startfile('Matriz_' + nodo.nombre + '.png')
        print('Grafica del patron inicial generada con exito')

    def GraficarMatrizTotal(self, nodo):
        contenido = ''
        file = open('MapasOperados/MisionRescate_' + str(nodo.nombre) + '.dot', 'w')
        contenido += '''digraph structs {
	node [shape=plaintext]
	patron [fontsize="40pt", label=<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="2" CELLPADDING="20">\n'''
        filas = int(nodo.matriz.filas.tamanio)
        columnas = int(nodo.matriz.columnas.tamanio)
        matrizc = nodo.matriz
        contenido += '''<TR>
    <TD border="0">'''+str(nodo.nombre)+'''</TD>'''
        for i in range(columnas):
            contenido += '<TD border="0">'+ str(i+1) + '</TD>'
        
        contenido += '\n</TR>'

        for i in range(filas):
            contenido += '''\n<TR>
        <TD border="0">'''+str(i+1)+'''</TD>'''

            for j in range(columnas):
                if nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == '*':
                    contenido+="\n<TD bgcolor=\"black\">   </TD>"
                elif nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'E':
                    contenido+="\n<TD bgcolor=\"yellowgreen\">   </TD>"
                elif nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'C':
                    contenido+="\n<TD bgcolor=\"royalblue1\">   </TD>"
                elif nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'R':
                    contenido+="\n<TD bgcolor=\"grey39\">   </TD>"
                elif nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'M':
                    contenido+="\n<TD bgcolor=\"red3\">   </TD>"
                elif nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == ' ':
                    contenido+="\n<TD>   </TD>"
                elif nodo.matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'P':
                    contenido+="\n<TD bgcolor=\"goldenrod\">   </TD>"
            contenido += '</TR>'
        contenido += '''</TABLE>>]
}'''

        file.write(contenido)
        file.close()
        os.system('dot -Tpng MapasOperados/MisionRescate_'+str(nodo.nombre)+'.dot -o MapasOperados/MisionRescate_'+str(nodo.nombre)+'.png')
        os.startfile('MapasOperados\MisionRescate_' + nodo.nombre + '.png')
        #print('Grafica del patron inicial generada con exito')

    def Mision_Rescate(self,nombrec,xi,yi,xf,yf):
        #! VARIABLES PARA PODER ITERAR LA MISION
        ciudad = self.retornarNodo(nombrec)
        entrada = ciudad.matriz.retornarNodo(xi,yi)
        unidadcivil = ciudad.matriz.retornarNodo(xf,yf)
        
        #COMIENZA LA BUSQUEDA
        actual:NodoCelda = entrada
        while actual != unidadcivil:
            #& ----------CAMINOS LIBRES----------------
            #~VERIFICACION DERECHA
            if actual.derecha.caracter == ' ':
                #actual.derecha.caracter = 'P'
                actual = actual.derecha
                actual.caracter = 'P'
            #?VERIFICACION ABAJO
            elif actual.abajo.caracter == ' ':
                #actual.arriba.caracter = 'P'
                actual = actual.abajo
                actual.caracter = 'P'
            #*VERIFICACION ARRIBA
            elif actual.arriba.caracter == ' ':
                #actual.abajo.caracter = 'P'
                actual = actual.arriba
                actual.caracter = 'P'
            #^VERIFICACION IZQUIERDA
            elif actual.izquierda.caracter == ' ':
                #actual.izquierda.caracter = 'P'
                actual = actual.izquierda
                actual.caracter = 'P'
            #& ----------UNIDADES CIVILES----------------
            #~VERIFICACION DERECHA
            elif actual.derecha.caracter == 'C':
                actual = actual.derecha
            #?VERIFICACION ARRIBA
            elif actual.arriba.caracter == 'C':
                actual = actual.arriba
            #*VERIFICACION ABAJO
            elif actual.abajo.caracter == 'C':
                actual = actual.abajo
            #^VERIFICACION IZQUIERDA
            elif actual.izquierda.caracter == 'C':
                actual = actual.izquierda
            else:
                #& ----------PASOS EQUIVOCADOS----------------
                #~VERIFICACION DERECHA
                if actual.derecha.caracter == 'P':
                    actual.caracter = ' '
                    actual = actual.derecha
                #?VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'P':
                    actual.caracter = ' '
                    actual = actual.arriba
                #*VERIFICACION ABAJO
                elif actual.abajo.caracter == 'P':
                    actual.caracter = ' '
                    actual = actual.abajo
                #^VERIFICACION IZQUIERDA
                elif actual.izquierda.caracter == 'P':
                    actual = actual.izquierda
        self.GraficarMatrizTotal(ciudad)
    
    def __len__(self):
        return self.tamanio