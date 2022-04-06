from .MatrizDispersa import MatrizDispersa
from .NodoCiudad import NodoCiudad
from .NodoCelda import NodoCelda
from .Pila import Pila
from tkinter import messagebox
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
	patron [fontname="Roboto Condensed"fontsize="15pt", label=<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="2" CELLPADDING="10">\n'''
        filas = int(nodo.matriz.filas.tamanio)
        columnas = int(nodo.matriz.columnas.tamanio)
        matrizc = nodo.matriz
        contenido += '''<TR>
    <TD border="0"></TD>'''
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
        contenido += '''</TABLE>>]'''
        contenido += '''fontname="Roboto Condensed"fontsize="35pt"label="'''+str(nodo.nombre)+'''"\n}'''

        file.write(contenido)
        file.close()
        os.system('dot -Tpng MapasGenerados/Matriz_'+str(nodo.nombre)+'.dot -o MapasGenerados/Matriz_'+str(nodo.nombre)+'.png')
        #os.startfile('Matriz_' + nodo.nombre + '.png')
        print('Grafica del patron inicial generada con exito')

    def GraficarMatrizRescate(self, matriz, nombre, robot, civil):
        contenido = ''
        file = open('MapasOperados/MisionRescate_' + str(nombre) + '.dot', 'w')
        contenido += '''digraph structs {
	node [shape=plaintext]
	patron [fontname="Roboto Condensed"fontsize="15pt", label=<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="2" CELLPADDING="10">\n'''
        filas = int(matriz.filas.tamanio)
        print(str(filas))
        columnas = int(matriz.columnas.tamanio)
        print(str(columnas))
        contenido += '''<TR>
    <TD border="0">'''+str(nombre)+'''</TD>'''
        for i in range(columnas):
            contenido += '<TD border="0">'+ str(i+1) + '</TD>'
        contenido += '\n</TR>'

        for i in range(filas):
            contenido += '''\n<TR>
        <TD border="0">'''+str(i+1)+'''</TD>'''

            for j in range(columnas):
                if matriz.retornarNodo(int(i+1), int(j+1)).caracter == '*':
                    contenido+="\n<TD bgcolor=\"black\">   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'E':
                    contenido+="\n<TD bgcolor=\"yellowgreen\">   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'C':
                    contenido+="\n<TD bgcolor=\"royalblue1\">   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'R':
                    contenido+="\n<TD bgcolor=\"grey39\">   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'M':
                    contenido+="\n<TD bgcolor=\"red3\">   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == ' ':
                    contenido+="\n<TD>   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'P':
                    contenido+="\n<TD bgcolor=\"goldenrod\">   </TD>"
            contenido += '</TR>'
        contenido += '''</TABLE>>]'''
        contenido += '''fontname="Roboto Condensed"fontsize="20pt"label="Tipo de Mision: Rescate\\nUnidad Civil Rescatada: ''' + str(civil.x) + ',' + str(civil.y) + '''\\nRobot Utilizado: ''' + str(robot.nombre) + '(' + str(robot.tipo) + ''')"\n'''
        contenido += '''info1[fontname="Roboto Condensed"fontsize="15pt", label=<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="3" CELLPADDING="10">
<TR>
    <TD border="0" bgcolor="yellowgreen"></TD> 
    <TD border="0">Camino de Entrada </TD> 
</TR>
<TR>
    <TD border="0" bgcolor="black"></TD> 
    <TD border="0">Intransitable </TD> 
</TR>
<TR>
    <TD border="0" bgcolor="royalblue1"></TD> 
    <TD border="0">Unidad Civil</TD> 
</TR>
<TR>
    <TD border="0" bgcolor="red3"></TD> 
    <TD border="0">Unidad Militar</TD> 
</TR>
<TR>
    <TD border="0" bgcolor="grey39"></TD> 
    <TD border="0">Recurso</TD> 
</TR>
<TR>
    <TD border="0" bgcolor="white"></TD> 
    <TD border="0">Camino</TD> 
</TR>
<TR>
    <TD border="0" bgcolor="goldenrod"></TD> 
    <TD border="0">Camino del Robot</TD> 
</TR>
</TABLE>>]\n}'''

        file.write(contenido)
        file.close()
        os.system('dot -Tpng MapasOperados/MisionRescate_'+str(nombre)+'.dot -o MapasOperados/MisionRescate_'+str(nombre)+'.png')
        os.startfile('MapasOperados\MisionRescate_' + nombre + '.png')
        #print('Grafica del patron inicial generada con exito')

    def GraficarMatrizExtraccionRecursos(self, matriz, nombre, robot, recurso, ci, cf):
        contenido = ''
        file = open('MapasOperados/MisionExtracciondeRecursos_' + str(nombre) + '.dot', 'w')
        contenido += '''digraph structs {
	node [shape=plaintext]
	patron [fontname="Roboto Condensed"fontsize="15pt", label=<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="2" CELLPADDING="10">\n'''
        filas = int(matriz.filas.tamanio)
        print(str(filas))
        columnas = int(matriz.columnas.tamanio)
        print(str(columnas))
        contenido += '''<TR>
    <TD border="0">'''+str(nombre)+'''</TD>'''
        for i in range(columnas):
            contenido += '<TD border="0">'+ str(i+1) + '</TD>'
        contenido += '\n</TR>'

        for i in range(filas):
            contenido += '''\n<TR>
        <TD border="0">'''+str(i+1)+'''</TD>'''

            for j in range(columnas):
                if matriz.retornarNodo(int(i+1), int(j+1)).caracter == '*':
                    contenido+="\n<TD bgcolor=\"black\">   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'E':
                    contenido+="\n<TD bgcolor=\"yellowgreen\">   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'C':
                    contenido+="\n<TD bgcolor=\"royalblue1\">   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'R':
                    contenido+="\n<TD bgcolor=\"grey39\">   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'M':
                    contenido+="\n<TD bgcolor=\"red3\">   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'MP':
                    contenido+="\n<TD bgcolor=\"orangered\">   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == ' ':
                    contenido+="\n<TD>   </TD>"
                elif matriz.retornarNodo(int(i+1), int(j+1)).caracter == 'P':
                    contenido+="\n<TD bgcolor=\"goldenrod\">   </TD>"
            contenido += '</TR>'
        contenido += '''</TABLE>>]'''
        contenido += '''fontname="Roboto Condensed"fontsize="20pt"label="Tipo de Mision: Extraccion de Recursos\\nRecurso Extraido: ''' + str(recurso.x) + ',' + str(recurso.y) + '''\\nRobot Utilizado: ''' + str(robot.nombre) + '(' + str(robot.tipo) + ''' - Capacidad de combate inicial ''' + str(ci) + ''', Capacidad de combate final '''+str(cf)+''')"\n'''
        contenido += '''info1[fontname="Roboto Condensed"fontsize="15pt", label=<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="3" CELLPADDING="10">
<TR>
    <TD border="0" bgcolor="yellowgreen"></TD> 
    <TD border="0">Camino de Entrada </TD> 
</TR>
<TR>
    <TD border="0" bgcolor="black"></TD> 
    <TD border="0">Intransitable </TD> 
</TR>
<TR>
    <TD border="0" bgcolor="royalblue1"></TD> 
    <TD border="0">Unidad Civil</TD> 
</TR>
<TR>
    <TD border="0" bgcolor="red3"></TD> 
    <TD border="0">Unidad Militar</TD> 
</TR>
<TR>
    <TD border="0" bgcolor="grey39"></TD> 
    <TD border="0">Recurso</TD> 
</TR>
<TR>
    <TD border="0" bgcolor="white"></TD> 
    <TD border="0">Camino</TD> 
</TR>
<TR>
    <TD border="0" bgcolor="goldenrod"></TD> 
    <TD border="0">Camino del Robot</TD> 
</TR>
<TR>
    <TD border="0" bgcolor="orangered"></TD> 
    <TD border="0">Unidad Militar derrotada</TD> 
</TR>
</TABLE>>]\n}'''

        file.write(contenido)
        file.close()
        os.system('dot -Tpng MapasOperados/MisionExtracciondeRecursos_'+str(nombre)+'.dot -o MapasOperados/MisionExtracciondeRecursos_'+str(nombre)+'.png')
        os.startfile('MapasOperados\MisionExtracciondeRecursos_' + nombre + '.png')
        #print('Grafica del patron inicial generada con exito')


#TODO ----------------------------------------------------------------- METODO PARA MISION DE RESCATE ----------------------------------------------------------------------
    def Mision_Rescate(self,nombrec,xi,yi,xf,yf, robot):
        #! VARIABLES PARA PODER ITERAR LA MISION
        ciudad = self.retornarNodo(nombrec)
        matriz_aux = MatrizDispersa()
        f = 1
        for i in range(int(ciudad.matriz.filas.tamanio)):
            c = 1
            for j in range(int(ciudad.matriz.columnas.tamanio)):
                matriz_aux.InsertarNodo(ciudad.matriz.retornarNodo(f,c).x,ciudad.matriz.retornarNodo(f,c).y,ciudad.matriz.retornarNodo(f,c).caracter,ciudad.matriz.retornarNodo(f,c).capacidad)
                c+=1
            f+=1
        entrada = matriz_aux.retornarNodo(xi,yi)
        print(str(entrada.caracter))
        unidadcivil = matriz_aux.retornarNodo(xf,yf)
        #COMIENZA LA BUSQUEDA
        actual:NodoCelda = entrada
        while actual != unidadcivil:
            #& ----------VERIFICAR NULOS----------------
            #^VERIFICACION IZQUIERDA
            if actual.izquierda == None:
                #& ----------VERIFICAR SI EL SIGUIENTE ES UNA UNIDAD CIVIL----------------
                #~VERIFICACION DERECHA
                if actual.derecha.caracter == 'C':
                    if actual.derecha == unidadcivil:
                        actual = actual.derecha
                #?VERIFICACION ABAJO
                elif actual.abajo.caracter == 'C':
                    if actual.abajo == unidadcivil:
                        actual = actual.abajo
                #*VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'C':
                    if actual.arriba == unidadcivil:
                        actual = actual.arriba
                #& ----------CAMINOS LIBRES DE 1 DIRECCION----------------
                #~VERIFICACION DERECHA
                elif actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.derecha.caracter == ' ':
                        actual = actual.derecha
                        actual.caracter = 'P'
                #?VERIFICACION ABAJO
                elif actual.derecha.caracter != ' ' and actual.arriba.caracter != ' ' and actual.abajo.caracter == ' ':
                        actual = actual.abajo
                        actual.caracter = 'P'
                #*VERIFICACION ARRIBA
                elif actual.derecha.caracter != ' ' and actual.abajo.caracter != ' ' and actual.arriba.caracter == ' ':
                        actual = actual.arriba
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 2 DIRECCIONES----------------
                #~VERIFICACION ARRIBA-ABAJO
                elif actual.arriba.caracter == ' ' and actual.abajo.caracter == ' ' and actual.derecha.caracter != ' ':
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    resta_abajo = unidadcivil.x - actual.abajo.x
                    if abs(resta_arriba) > abs(resta_abajo):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.arriba
                        actual.caracter = 'P'
                #?VERIFICACION DERECHA-ARRIBA
                elif actual.derecha.caracter == ' ' and actual.arriba.caracter == ' ' and actual.abajo.caracter != ' ':
                    resta_actualx = unidadcivil.x - actual.x
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    if abs(resta_arriba) < abs(resta_actualx):
                        actual = actual.arriba
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #!VERIFICACION DERECHA-ABAJO
                elif actual.derecha.caracter == ' ' and actual.abajo.caracter == ' '  and actual.arriba.caracter != ' ':
                    resta_actualx = unidadcivil.x - actual.x
                    resta_abajo = unidadcivil.x - actual.abajo.x
                    if abs(resta_abajo) < abs(resta_actualx):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 3 DIRECCIONES----------------
                #^VERIFICACION ARRIBA-ABAJO-DERECHA
                elif actual.derecha.caracter == ' ' and actual.abajo.caracter == ' ' and actual.arriba.caracter == ' ':
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    resta_abajo = unidadcivil.x -actual.abajo.x
                    resta_actual = unidadcivil.y - actual.y
                    resta_derecha = unidadcivil.y - actual.derecha.y
                    if abs(resta_derecha) > abs(resta_actual):
                        if abs(resta_abajo)< abs(resta_arriba):
                            actual = actual.abajo
                            actual.caracter = 'P'
                        else:
                            actual = actual.arriba
                            actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                elif actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.derecha.caracter != ' ':
                    break
                else:
                    break
            #~VERIFICACION DERECHA
            elif actual.derecha == None:
                #& ----------VERIFICAR SI EL SIGUIENTE ES UNA UNIDAD CIVIL----------------
                #^VERIFICACION IZQUIERDA
                if actual.izquierda.caracter == 'C':
                    if actual.izquierda == unidadcivil:
                        actual = actual.izquierda
                #?VERIFICACION ABAJO
                elif actual.abajo.caracter == 'C':
                    if actual.abajo == unidadcivil:
                        actual = actual.abajo
                #*VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'C':
                    if actual.arriba == unidadcivil:
                        actual = actual.arriba
                #& ----------CAMINOS LIBRES DE 1 DIRECCION----------------
                #^VERIFICACION IZQUIERDA
                elif actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.izquierda.caracter == ' ':
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #?VERIFICACION ABAJO
                elif actual.arriba.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.abajo.caracter == ' ':
                        actual = actual.abajo
                        actual.caracter = 'P'
                #*VERIFICACION ARRIBA
                elif actual.izquierda.caracter != ' ' and actual.abajo.caracter != ' ' and actual.arriba.caracter == ' ':
                        actual = actual.arriba
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 2 DIRECCIONES----------------
                #~VERIFICACION ARRIBA-ABAJO
                elif actual.arriba.caracter == ' ' and actual.abajo.caracter == ' ' and actual.izquierda.caracter != ' ':
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    resta_abajo = unidadcivil.x - actual.abajo.x
                    if abs(resta_arriba) > abs(resta_abajo):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.arriba
                        actual.caracter = 'P'
                #*VERIFICACION IZQUIERDA-ARRIBA
                elif actual.izquierda.caracter == ' ' and actual.arriba.caracter == ' ' and actual.abajo.caracter != ' ':
                    resta_actualx = unidadcivil.x - actual.x
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    if abs(resta_arriba) < abs(resta_actualx):
                        actual = actual.arriba
                        actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #TODO VERIFICACION IZQUIERDA-ABAJO
                elif actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ' and actual.arriba.caracter != ' ':
                    resta_actualx = unidadcivil.x - actual.x
                    resta_abajo = unidadcivil.x - actual.abajo.x
                    if abs(resta_abajo) < abs(resta_actualx):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 3 DIRECCIONES----------------
                #~VERIFICACION ARRIBA-ABAJO-IZQUIERDA
                elif actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ' and actual.arriba.caracter == ' ':
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    resta_abajo = unidadcivil.x -actual.abajo.x
                    resta_actual = unidadcivil.y - actual.y
                    resta_izquierda = unidadcivil.y - actual.izquierda.y
                    if abs(resta_izquierda) > abs(resta_actual):
                        if abs(resta_abajo)< abs(resta_arriba):
                            actual = actual.abajo
                            actual.caracter = 'P'
                        else:
                            actual = actual.arriba
                            actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                elif actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.izquierda.caracter != ' ':
                    
                    break
                else:
                    
                    break
            #*VERIFICACION ARRIBA
            elif actual.arriba == None:
                #& ----------VERIFICAR SI EL SIGUIENTE ES UNA UNIDAD CIVIL----------------
                #~VERIFICACION DERECHA
                if actual.derecha.caracter == 'C':
                    if actual.derecha == unidadcivil:
                        actual = actual.derecha
                #^VERIFICACION IZQUIERDA
                elif actual.izquierda.caracter == 'C':
                    if actual.izquierda == unidadcivil:
                        actual = actual.izquierda
                #?VERIFICACION ABAJO
                elif actual.abajo.caracter == 'C':
                    if actual.abajo == unidadcivil:
                        actual = actual.abajo
                #& ----------CAMINOS LIBRES DE 1 DIRECCION----------------
                #~VERIFICACION DERECHA
                elif actual.izquierda.caracter != ' ' and actual.abajo.caracter != ' ' and actual.derecha.caracter == ' ':
                        actual = actual.derecha
                        actual.caracter = 'P'
                #^VERIFICACION IZQUIERDA
                elif actual.derecha.caracter != ' ' and actual.abajo.caracter != ' ' and actual.izquierda.caracter == ' ':
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #?VERIFICACION ABAJO
                elif actual.derecha.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.abajo.caracter == ' ':
                        actual = actual.abajo
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 2 DIRECCIONES----------------
                #^VERIFICACION IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.abajo.caracter != ' ':
                    resta_derecha = unidadcivil.y - actual.derecha.y
                    resta_izquierda = unidadcivil.y - actual.izquierda.y
                    if abs(resta_derecha) > abs(resta_izquierda):
                        actual = actual.izquierda
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #!VERIFICACION DERECHA-ABAJO
                elif actual.derecha.caracter == ' ' and actual.abajo.caracter == ' ' and actual.izquierda.caracter != ' ' :
                    resta_actualx = unidadcivil.x - actual.x
                    resta_abajo = unidadcivil.x - actual.abajo.x
                    if abs(resta_abajo) < abs(resta_actualx):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #TODO VERIFICACION IZQUIERDA-ABAJO
                elif actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ' and actual.derecha.caracter != ' ' :
                    resta_actualx = unidadcivil.x - actual.x
                    resta_abajo = unidadcivil.x - actual.abajo.x
                    if abs(resta_abajo) < abs(resta_actualx):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 3 DIRECCIONES----------------
                #*VERIFICACION ABAJO-IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ':
                    resta_abajo = unidadcivil.x - actual.abajo.x
                    resta_izquierda = unidadcivil.y -actual.izquierda.y
                    resta_actual = unidadcivil.x - actual.x
                    resta_derecha = unidadcivil.y - actual.derecha.y
                    if abs(resta_abajo) > abs(resta_actual):
                        if abs(resta_izquierda)< abs(resta_derecha):
                            actual = actual.izquierda
                            actual.caracter = 'P'
                        else:
                            actual = actual.derecha
                            actual.caracter = 'P'
                    else:
                        actual = actual.abajo
                        actual.caracter = 'P'
                elif actual.abajo.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.derecha.caracter != ' ':
                    
                    break
                else:
                    
                    break
            #?VERIFICACION ABAJO
            elif actual.abajo == None:
                #& ----------VERIFICAR SI EL SIGUIENTE ES UNA UNIDAD CIVIL----------------
                #~VERIFICACION DERECHA
                if actual.derecha.caracter == 'C':
                    if actual.derecha == unidadcivil:
                        actual = actual.derecha
                #^VERIFICACION IZQUIERDA
                elif actual.izquierda.caracter == 'C':
                    if actual.izquierda == unidadcivil:
                        actual = actual.izquierda
                #*VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'C':
                    if actual.arriba == unidadcivil:
                        actual = actual.arriba
                #& ----------CAMINOS LIBRES DE 1 DIRECCION----------------
                #~VERIFICACION DERECHA
                elif actual.izquierda.caracter != ' ' and actual.arriba.caracter != ' '  and actual.derecha.caracter == ' ':
                        actual = actual.derecha
                        actual.caracter = 'P'
                #^VERIFICACION IZQUIERDA
                elif actual.derecha.caracter != ' ' and actual.arriba.caracter != ' ' and  actual.izquierda.caracter == ' ':
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #*VERIFICACION ARRIBA
                elif actual.derecha.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.arriba.caracter == ' ':
                        actual = actual.arriba
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 2 DIRECCIONES----------------
                #^VERIFICACION IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.arriba.caracter != ' ':
                    resta_derecha = unidadcivil.y - actual.derecha.y
                    resta_izquierda = unidadcivil.y - actual.izquierda.y
                    if abs(resta_derecha) > abs(resta_izquierda):
                        actual = actual.izquierda
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #?VERIFICACION DERECHA-ARRIBA
                elif actual.derecha.caracter == ' ' and actual.arriba.caracter == ' ' and actual.izquierda.caracter != ' ':
                    resta_actualx = unidadcivil.x - actual.x
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    if abs(resta_arriba) < abs(resta_actualx):
                        actual = actual.arriba
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #*VERIFICACION IZQUIERDA-ARRIBA
                elif actual.izquierda.caracter == ' ' and actual.arriba.caracter == ' ' and actual.derecha.caracter != ' ':
                    resta_actualx = unidadcivil.x - actual.x
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    if abs(resta_arriba) < abs(resta_actualx):
                        actual = actual.arriba
                        actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 3 DIRECCIONES----------------
                #?VERIFICACION ARRIBA-IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.arriba.caracter == ' ':
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    resta_izquierda = unidadcivil.y -actual.izquierda.y
                    resta_actual = unidadcivil.x - actual.x
                    resta_derecha = unidadcivil.y - actual.derecha.y
                    if abs(resta_arriba) > abs(resta_actual):
                        if abs(resta_izquierda)< abs(resta_derecha):
                            actual = actual.izquierda
                            actual.caracter = 'P'
                        else:
                            actual = actual.derecha
                            actual.caracter = 'P'
                    else:
                        actual = actual.arriba
                        actual.caracter = 'P'
                elif actual.arriba.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.derecha.caracter != ' ':
                    
                    break
                else:
                    
                    break
            #TODO SIN RESTRICCION DE NULOS
            else:
                #& ----------VERIFICAR SI EL SIGUIENTE ES UNA UNIDAD CIVIL----------------
                #~VERIFICACION DERECHA
                if actual.derecha.caracter == 'C':
                    if actual.derecha == unidadcivil:
                        actual = actual.derecha
                #^VERIFICACION IZQUIERDA
                elif actual.izquierda.caracter == 'C':
                    if actual.izquierda == unidadcivil:
                        actual = actual.izquierda
                #?VERIFICACION ABAJO
                elif actual.abajo.caracter == 'C':
                    if actual.abajo == unidadcivil:
                        actual = actual.abajo
                #*VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'C':
                    if actual.arriba == unidadcivil:
                        actual = actual.arriba
                #& ----------CAMINOS LIBRES DE 1 DIRECCION----------------
                #~VERIFICACION DERECHA
                elif actual.izquierda.caracter != ' ' and actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.derecha.caracter == ' ':
                        actual = actual.derecha
                        actual.caracter = 'P'
                #^VERIFICACION IZQUIERDA
                elif actual.derecha.caracter != ' ' and actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.izquierda.caracter == ' ':
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #?VERIFICACION ABAJO
                elif actual.derecha.caracter != ' ' and actual.arriba.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.abajo.caracter == ' ':
                        actual = actual.abajo
                        actual.caracter = 'P'
                #*VERIFICACION ARRIBA
                elif actual.derecha.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.abajo.caracter != ' ' and actual.arriba.caracter == ' ':
                        actual = actual.arriba
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 2 DIRECCIONES----------------
                #~VERIFICACION ARRIBA-ABAJO
                elif actual.arriba.caracter == ' ' and actual.abajo.caracter == ' ' and actual.izquierda.caracter != ' ' and actual.derecha.caracter != ' ':
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    resta_abajo = unidadcivil.x - actual.abajo.x
                    if abs(resta_arriba) > abs(resta_abajo):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.arriba
                        actual.caracter = 'P'
                #^VERIFICACION IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ':
                    resta_derecha = unidadcivil.y - actual.derecha.y
                    resta_izquierda = unidadcivil.y - actual.izquierda.y
                    if abs(resta_derecha) > abs(resta_izquierda):
                        actual = actual.izquierda
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #?VERIFICACION DERECHA-ARRIBA
                elif actual.derecha.caracter == ' ' and actual.arriba.caracter == ' ' and actual.izquierda.caracter != ' ' and actual.abajo.caracter != ' ':
                    resta_actualx = unidadcivil.x - actual.x
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    if abs(resta_arriba) < abs(resta_actualx):
                        actual = actual.arriba
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #*VERIFICACION IZQUIERDA-ARRIBA
                elif actual.izquierda.caracter == ' ' and actual.arriba.caracter == ' ' and actual.derecha.caracter != ' ' and actual.abajo.caracter != ' ':
                    resta_actualx = unidadcivil.x - actual.x
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    if abs(resta_arriba) < abs(resta_actualx):
                        actual = actual.arriba
                        actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #!VERIFICACION DERECHA-ABAJO
                elif actual.derecha.caracter == ' ' and actual.abajo.caracter == ' ' and actual.izquierda.caracter != ' ' and actual.arriba.caracter != ' ':
                    resta_actualx = unidadcivil.x - actual.x
                    resta_abajo = unidadcivil.x - actual.abajo.x
                    if abs(resta_abajo) < abs(resta_actualx):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #TODO VERIFICACION IZQUIERDA-ABAJO
                elif actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ' and actual.derecha.caracter != ' ' and actual.arriba.caracter != ' ':
                    resta_actualx = unidadcivil.x - actual.x
                    resta_abajo = unidadcivil.x - actual.abajo.x
                    if abs(resta_abajo) < abs(resta_actualx):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 3 DIRECCIONES----------------
                #~VERIFICACION ARRIBA-ABAJO-IZQUIERDA
                elif actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ' and actual.arriba.caracter == ' ' and actual.derecha.caracter != ' ':
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    resta_abajo = unidadcivil.x -actual.abajo.x
                    resta_actual = unidadcivil.y - actual.y
                    resta_izquierda = unidadcivil.y - actual.izquierda.y
                    if abs(resta_izquierda) > abs(resta_actual):
                        if abs(resta_abajo)< abs(resta_arriba):
                            actual = actual.abajo
                            actual.caracter = 'P'
                        else:
                            actual = actual.arriba
                            actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #^VERIFICACION ARRIBA-ABAJO-DERECHA
                elif actual.derecha.caracter == ' ' and actual.abajo.caracter == ' ' and actual.arriba.caracter == ' ' and actual.izquierda.caracter != ' ':
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    resta_abajo = unidadcivil.x -actual.abajo.x
                    resta_actual = unidadcivil.y - actual.y
                    resta_derecha = unidadcivil.y - actual.derecha.y
                    if abs(resta_derecha) > abs(resta_actual):
                        if abs(resta_abajo)< abs(resta_arriba):
                            actual = actual.abajo
                            actual.caracter = 'P'
                        else:
                            actual = actual.arriba
                            actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #?VERIFICACION ARRIBA-IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.arriba.caracter == ' ' and actual.abajo.caracter != ' ':
                    resta_arriba = unidadcivil.x - actual.arriba.x
                    resta_izquierda = unidadcivil.y -actual.izquierda.y
                    resta_actual = unidadcivil.x - actual.x
                    resta_derecha = unidadcivil.y - actual.derecha.y
                    if abs(resta_arriba) > abs(resta_actual):
                        if abs(resta_izquierda)< abs(resta_derecha):
                            actual = actual.izquierda
                            actual.caracter = 'P'
                        else:
                            actual = actual.derecha
                            actual.caracter = 'P'
                    else:
                        actual = actual.arriba
                        actual.caracter = 'P'
                #*VERIFICACION ABAJO-IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ' and actual.arriba.caracter != ' ':
                    resta_abajo = unidadcivil.x - actual.abajo.x
                    resta_izquierda = unidadcivil.y -actual.izquierda.y
                    resta_actual = unidadcivil.x - actual.x
                    resta_derecha = unidadcivil.y - actual.derecha.y
                    if abs(resta_abajo) > abs(resta_actual):
                        if abs(resta_izquierda)< abs(resta_derecha):
                            actual = actual.izquierda
                            actual.caracter = 'P'
                        else:
                            actual = actual.derecha
                            actual.caracter = 'P'
                    else:
                        actual = actual.abajo
                        actual.caracter = 'P'
                elif actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.derecha.caracter != ' ':
                    break
                else:
                    break
            print('El robot se encuentra en X: ' + str(actual.x) + ' , Y: ' + str(actual.y))

        if actual == unidadcivil:
            messagebox.showinfo("Success","Mision cumplida!, Logramos encontrar la Unidad Civil en la zona")
            self.GraficarMatrizRescate(matriz_aux, ciudad.nombre, robot,unidadcivil)
        else:
            messagebox.showinfo("Error","No se pudo realizar la mision :(")
            self.GraficarMatrizRescate(matriz_aux, ciudad.nombre, robot,unidadcivil)


#TODO ----------------------------------------------------------------- METODO PARA MISION DE RECURSOS ----------------------------------------------------------------------
    def Mision_Recursos(self,nombrec,robot,xi,yi,xf,yf):
        #! VARIABLES PARA PODER ITERAR LA MISION
        ciudad = self.retornarNodo(nombrec)
        matriz_aux = MatrizDispersa()
        f = 1
        for i in range(int(ciudad.matriz.filas.tamanio)):
            c = 1
            for j in range(int(ciudad.matriz.columnas.tamanio)):
                matriz_aux.InsertarNodo(ciudad.matriz.retornarNodo(f,c).x,ciudad.matriz.retornarNodo(f,c).y,ciudad.matriz.retornarNodo(f,c).caracter,ciudad.matriz.retornarNodo(f,c).capacidad)
                c+=1
            f+=1

        entrada = matriz_aux.retornarNodo(xi,yi)
        recurso = matriz_aux.retornarNodo(xf,yf)
        capinicial = int(robot.capacidad)
        aux = capinicial

        #INICIA LA BUSQUEDA
        actual: NodoCelda = entrada
        while(actual != recurso):
            #& ----------VERIFICAR NULOS----------------
            #^VERIFICACION IZQUIERDA
            if actual.izquierda == None:
                #& ----------VERIFICAR SI EL SIGUIENTE ES UN RECURSO----------------
                #~VERIFICACION DERECHA
                if actual.derecha.caracter == 'R':
                    if actual.derecha == recurso:
                        actual = actual.derecha
                #?VERIFICACION ABAJO
                elif actual.abajo.caracter == 'R':
                    if actual.abajo == recurso:
                        actual = actual.abajo
                #*VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'R':
                    if actual.arriba == recurso:
                        actual = actual.arriba
                #& ----------VERIFICAR SI EL SIGUIENTE ES UNA UNIDAD MILITAR----------------
                #~VERIFICACION DERECHA
                elif actual.derecha.caracter == 'M':
                    actual = actual.derecha
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    print(str(aux))
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #?VERIFICACION ABAJO
                elif actual.abajo.caracter == 'M':
                    actual = actual.abajo
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #*VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'M':
                    actual = actual.derecha
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #& ----------CAMINOS LIBRES DE 1 DIRECCION----------------
                #~VERIFICACION DERECHA
                elif actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.derecha.caracter == ' ':
                        actual = actual.derecha
                        actual.caracter = 'P'
                #?VERIFICACION ABAJO
                elif actual.derecha.caracter != ' ' and actual.arriba.caracter != ' ' and actual.abajo.caracter == ' ':
                        actual = actual.abajo
                        actual.caracter = 'P'
                #*VERIFICACION ARRIBA
                elif actual.derecha.caracter != ' ' and actual.abajo.caracter != ' ' and actual.arriba.caracter == ' ':
                        actual = actual.arriba
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 2 DIRECCIONES----------------
                #~VERIFICACION ARRIBA-ABAJO
                elif actual.arriba.caracter == ' ' and actual.abajo.caracter == ' ' and actual.derecha.caracter != ' ':
                    resta_arriba = recurso.x - actual.arriba.x
                    resta_abajo = recurso.x - actual.abajo.x
                    if abs(resta_arriba) > abs(resta_abajo):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.arriba
                        actual.caracter = 'P'
                #?VERIFICACION DERECHA-ARRIBA
                elif actual.derecha.caracter == ' ' and actual.arriba.caracter == ' ' and actual.abajo.caracter != ' ':
                    resta_actualx = recurso.x - actual.x
                    resta_arriba = recurso.x - actual.arriba.x
                    if abs(resta_arriba) < abs(resta_actualx):
                        actual = actual.arriba
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #!VERIFICACION DERECHA-ABAJO
                elif actual.derecha.caracter == ' ' and actual.abajo.caracter == ' '  and actual.arriba.caracter != ' ':
                    resta_actualx = recurso.x - actual.x
                    resta_abajo = recurso.x - actual.abajo.x
                    if abs(resta_abajo) < abs(resta_actualx):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 3 DIRECCIONES----------------
                #^VERIFICACION ARRIBA-ABAJO-DERECHA
                elif actual.derecha.caracter == ' ' and actual.abajo.caracter == ' ' and actual.arriba.caracter == ' ':
                    resta_arriba = recurso.x - actual.arriba.x
                    resta_abajo = recurso.x -actual.abajo.x
                    resta_actual = recurso.y - actual.y
                    resta_derecha = recurso.y - actual.derecha.y
                    if abs(resta_derecha) > abs(resta_actual):
                        if abs(resta_abajo)< abs(resta_arriba):
                            actual = actual.abajo
                            actual.caracter = 'P'
                        else:
                            actual = actual.arriba
                            actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                elif actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.derecha.caracter != ' ':
                    break
                else:
                    break
            #~VERIFICACION DERECHA
            elif actual.derecha == None:
                #& ----------VERIFICAR SI EL SIGUIENTE ES UN RECURSO----------------
                #^VERIFICACION IZQUIERDA
                if actual.izquierda.caracter == 'R':
                    if actual.izquierda == recurso:
                        actual = actual.izquierda
                #?VERIFICACION ABAJO
                elif actual.abajo.caracter == 'R':
                    if actual.abajo == recurso:
                        actual = actual.abajo
                #*VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'R':
                    if actual.arriba == recurso:
                        actual = actual.arriba
                #& ----------VERIFICAR SI EL SIGUIENTE ES UNA UNIDAD MILITAR----------------
                #^VERIFICACION IZQUIERDA
                elif actual.izquierda.caracter == 'M':
                    actual = actual.izquierda
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #?VERIFICACION ABAJO
                elif actual.abajo.caracter == 'M':
                    actual = actual.abajo
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #*VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'M':
                    actual = actual.derecha
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #& ----------CAMINOS LIBRES DE 1 DIRECCION----------------
                #^VERIFICACION IZQUIERDA
                elif actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.izquierda.caracter == ' ':
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #?VERIFICACION ABAJO
                elif actual.arriba.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.abajo.caracter == ' ':
                        actual = actual.abajo
                        actual.caracter = 'P'
                #*VERIFICACION ARRIBA
                elif actual.izquierda.caracter != ' ' and actual.abajo.caracter != ' ' and actual.arriba.caracter == ' ':
                        actual = actual.arriba
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 2 DIRECCIONES----------------
                #~VERIFICACION ARRIBA-ABAJO
                elif actual.arriba.caracter == ' ' and actual.abajo.caracter == ' ' and actual.izquierda.caracter != ' ':
                    resta_arriba = recurso.x - actual.arriba.x
                    resta_abajo = recurso.x - actual.abajo.x
                    if abs(resta_arriba) > abs(resta_abajo):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.arriba
                        actual.caracter = 'P'
                #*VERIFICACION IZQUIERDA-ARRIBA
                elif actual.izquierda.caracter == ' ' and actual.arriba.caracter == ' ' and actual.abajo.caracter != ' ':
                    resta_actualx = recurso.x - actual.x
                    resta_arriba = recurso.x - actual.arriba.x
                    if abs(resta_arriba) < abs(resta_actualx):
                        actual = actual.arriba
                        actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #TODO VERIFICACION IZQUIERDA-ABAJO
                elif actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ' and actual.arriba.caracter != ' ':
                    resta_actualx = recurso.x - actual.x
                    resta_abajo = recurso.x - actual.abajo.x
                    if abs(resta_abajo) < abs(resta_actualx):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 3 DIRECCIONES----------------
                #~VERIFICACION ARRIBA-ABAJO-IZQUIERDA
                elif actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ' and actual.arriba.caracter == ' ':
                    resta_arriba = recurso.x - actual.arriba.x
                    resta_abajo = recurso.x -actual.abajo.x
                    resta_actual = recurso.y - actual.y
                    resta_izquierda = recurso.y - actual.izquierda.y
                    if abs(resta_izquierda) > abs(resta_actual):
                        if abs(resta_abajo)< abs(resta_arriba):
                            actual = actual.abajo
                            actual.caracter = 'P'
                        else:
                            actual = actual.arriba
                            actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                elif actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.izquierda.caracter != ' ':
                    
                    break
                else:
                    
                    break
            #*VERIFICACION ARRIBA
            elif actual.arriba == None:
                #& ----------VERIFICAR SI EL SIGUIENTE ES UN RECURSO----------------
                #~VERIFICACION DERECHA
                if actual.derecha.caracter == 'R':
                    if actual.derecha == recurso:
                        actual = actual.derecha
                #^VERIFICACION IZQUIERDA
                elif actual.izquierda.caracter == 'R':
                    if actual.izquierda == recurso:
                        actual = actual.izquierda
                #?VERIFICACION ABAJO
                elif actual.abajo.caracter == 'R':
                    if actual.abajo == recurso:
                        actual = actual.abajo
                #& ----------VERIFICAR SI EL SIGUIENTE ES UNA UNIDAD MILITAR----------------
                #~VERIFICACION DERECHA
                elif actual.derecha.caracter == 'M':
                    actual = actual.derecha
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #^VERIFICACION IZQUIERDA
                elif actual.izquierda.caracter == 'M':
                    actual = actual.izquierda
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #?VERIFICACION ABAJO
                elif actual.abajo.caracter == 'M':
                    actual = actual.abajo
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #& ----------CAMINOS LIBRES DE 1 DIRECCION----------------
                #~VERIFICACION DERECHA
                elif actual.izquierda.caracter != ' ' and actual.abajo.caracter != ' ' and actual.derecha.caracter == ' ':
                        actual = actual.derecha
                        actual.caracter = 'P'
                #^VERIFICACION IZQUIERDA
                elif actual.derecha.caracter != ' ' and actual.abajo.caracter != ' ' and actual.izquierda.caracter == ' ':
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #?VERIFICACION ABAJO
                elif actual.derecha.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.abajo.caracter == ' ':
                        actual = actual.abajo
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 2 DIRECCIONES----------------
                #^VERIFICACION IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.abajo.caracter != ' ':
                    resta_derecha = recurso.y - actual.derecha.y
                    resta_izquierda = recurso.y - actual.izquierda.y
                    if abs(resta_derecha) > abs(resta_izquierda):
                        actual = actual.izquierda
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #!VERIFICACION DERECHA-ABAJO
                elif actual.derecha.caracter == ' ' and actual.abajo.caracter == ' ' and actual.izquierda.caracter != ' ' :
                    resta_actualx = recurso.x - actual.x
                    resta_abajo = recurso.x - actual.abajo.x
                    if abs(resta_abajo) < abs(resta_actualx):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #TODO VERIFICACION IZQUIERDA-ABAJO
                elif actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ' and actual.derecha.caracter != ' ' :
                    resta_actualx = recurso.x - actual.x
                    resta_abajo = recurso.x - actual.abajo.x
                    if abs(resta_abajo) < abs(resta_actualx):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 3 DIRECCIONES----------------
                #*VERIFICACION ABAJO-IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ':
                    resta_abajo = recurso.x - actual.abajo.x
                    resta_izquierda = recurso.y -actual.izquierda.y
                    resta_actual = recurso.x - actual.x
                    resta_derecha = recurso.y - actual.derecha.y
                    if abs(resta_abajo) > abs(resta_actual):
                        if abs(resta_izquierda)< abs(resta_derecha):
                            actual = actual.izquierda
                            actual.caracter = 'P'
                        else:
                            actual = actual.derecha
                            actual.caracter = 'P'
                    else:
                        actual = actual.abajo
                        actual.caracter = 'P'
                elif actual.abajo.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.derecha.caracter != ' ':
                    
                    break
                else:
                    
                    break
            #?VERIFICACION ABAJO
            elif actual.abajo == None:
                #& ----------VERIFICAR SI EL SIGUIENTE ES UN RECURSO----------------
                #~VERIFICACION DERECHA
                if actual.derecha.caracter == 'R':
                    if actual.derecha == recurso:
                        actual = actual.derecha
                #^VERIFICACION IZQUIERDA
                elif actual.izquierda.caracter == 'R':
                    if actual.izquierda == recurso:
                        actual = actual.izquierda
                #*VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'R':
                    if actual.arriba == recurso:
                        actual = actual.arriba
                #& ----------VERIFICAR SI EL SIGUIENTE ES UNA UNIDAD MILITAR----------------
                #~VERIFICACION DERECHA
                elif actual.derecha.caracter == 'M':
                    actual = actual.derecha
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #^VERIFICACION IZQUIERDA
                elif actual.izquierda.caracter == 'M':
                    actual = actual.izquierda
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #*VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'M':
                    actual = actual.arriba
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #& ----------CAMINOS LIBRES DE 1 DIRECCION----------------
                #~VERIFICACION DERECHA
                elif actual.izquierda.caracter != ' ' and actual.arriba.caracter != ' '  and actual.derecha.caracter == ' ':
                        actual = actual.derecha
                        actual.caracter = 'P'
                #^VERIFICACION IZQUIERDA
                elif actual.derecha.caracter != ' ' and actual.arriba.caracter != ' ' and  actual.izquierda.caracter == ' ':
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #*VERIFICACION ARRIBA
                elif actual.derecha.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.arriba.caracter == ' ':
                        actual = actual.arriba
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 2 DIRECCIONES----------------
                #^VERIFICACION IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.arriba.caracter != ' ':
                    resta_derecha = recurso.y - actual.derecha.y
                    resta_izquierda = recurso.y - actual.izquierda.y
                    if abs(resta_derecha) > abs(resta_izquierda):
                        actual = actual.izquierda
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #?VERIFICACION DERECHA-ARRIBA
                elif actual.derecha.caracter == ' ' and actual.arriba.caracter == ' ' and actual.izquierda.caracter != ' ':
                    resta_actualx = recurso.x - actual.x
                    resta_arriba = recurso.x - actual.arriba.x
                    if abs(resta_arriba) < abs(resta_actualx):
                        actual = actual.arriba
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #*VERIFICACION IZQUIERDA-ARRIBA
                elif actual.izquierda.caracter == ' ' and actual.arriba.caracter == ' ' and actual.derecha.caracter != ' ':
                    resta_actualx = recurso.x - actual.x
                    resta_arriba = recurso.x - actual.arriba.x
                    if abs(resta_arriba) < abs(resta_actualx):
                        actual = actual.arriba
                        actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 3 DIRECCIONES----------------
                #?VERIFICACION ARRIBA-IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.arriba.caracter == ' ':
                    resta_arriba = recurso.x - actual.arriba.x
                    resta_izquierda = recurso.y -actual.izquierda.y
                    resta_actual = recurso.x - actual.x
                    resta_derecha = recurso.y - actual.derecha.y
                    if abs(resta_arriba) > abs(resta_actual):
                        if abs(resta_izquierda)< abs(resta_derecha):
                            actual = actual.izquierda
                            actual.caracter = 'P'
                        else:
                            actual = actual.derecha
                            actual.caracter = 'P'
                    else:
                        actual = actual.arriba
                        actual.caracter = 'P'
                elif actual.arriba.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.derecha.caracter != ' ':
                    
                    break
                else:
                    
                    break
            #TODO SIN RESTRICCION DE NULOS
            else:
                #& ----------VERIFICAR SI EL SIGUIENTE ES UN RECURSO----------------
                #~VERIFICACION DERECHA
                if actual.derecha.caracter == 'R':
                    if actual.derecha == recurso:
                        actual = actual.derecha
                #^VERIFICACION IZQUIERDA
                elif actual.izquierda.caracter == 'R':
                    if actual.izquierda == recurso:
                        actual = actual.izquierda
                #?VERIFICACION ABAJO
                elif actual.abajo.caracter == 'R':
                    if actual.abajo == recurso:
                        actual = actual.abajo
                #*VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'R':
                    if actual.arriba == recurso:
                        actual = actual.arriba
                #& ----------VERIFICAR SI EL SIGUIENTE ES UNA UNIDAD MILITAR----------------
                #~VERIFICACION DERECHA
                elif actual.derecha.caracter == 'M':
                    actual = actual.derecha
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    print('Capacidad inicial: ' + str(aux))
                    print('Capacidad Militar: ' + str(umilitar.capacidad))
                    aux = aux - umilitar.capacidad
                    print('Capacidad final: '+str(aux))
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #^VERIFICACION IZQUIERDA
                elif actual.izquierda.caracter == 'M':
                    actual = actual.izquierda
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #?VERIFICACION ABAJO
                elif actual.abajo.caracter == 'M':
                    actual = actual.abajo
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #*VERIFICACION ARRIBA
                elif actual.arriba.caracter == 'M':
                    actual = actual.arriba
                    umilitar = matriz_aux.retornarNodo(actual.x,actual.y)
                    aux = aux - umilitar.capacidad
                    if aux < 0:
                        robot.capacidad = 0
                        messagebox.showinfo("Error","No se pudo realizar la mision ya que la unidad militar x: " + str(umilitar.x) + ", y: " + str(umilitar.y) + " derrotó al robot " + str(robot.nombre) + ".")
                        break
                    actual.caracter = 'MP'
                #& ----------CAMINOS LIBRES DE 1 DIRECCION----------------
                #~VERIFICACION DERECHA
                elif actual.izquierda.caracter != ' ' and actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.derecha.caracter == ' ':
                        actual = actual.derecha
                        actual.caracter = 'P'
                #^VERIFICACION IZQUIERDA
                elif actual.derecha.caracter != ' ' and actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.izquierda.caracter == ' ':
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #?VERIFICACION ABAJO
                elif actual.derecha.caracter != ' ' and actual.arriba.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.abajo.caracter == ' ':
                        actual = actual.abajo
                        actual.caracter = 'P'
                #*VERIFICACION ARRIBA
                elif actual.derecha.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.abajo.caracter != ' ' and actual.arriba.caracter == ' ':
                        actual = actual.arriba
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 2 DIRECCIONES----------------
                #~VERIFICACION ARRIBA-ABAJO
                elif actual.arriba.caracter == ' ' and actual.abajo.caracter == ' ' and actual.izquierda.caracter != ' ' and actual.derecha.caracter != ' ':
                    resta_arriba = recurso.x - actual.arriba.x
                    resta_abajo = recurso.x - actual.abajo.x
                    if abs(resta_arriba) > abs(resta_abajo):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.arriba
                        actual.caracter = 'P'
                #^VERIFICACION IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ':
                    resta_derecha = recurso.y - actual.derecha.y
                    resta_izquierda = recurso.y - actual.izquierda.y
                    if abs(resta_derecha) > abs(resta_izquierda):
                        actual = actual.izquierda
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #?VERIFICACION DERECHA-ARRIBA
                elif actual.derecha.caracter == ' ' and actual.arriba.caracter == ' ' and actual.izquierda.caracter != ' ' and actual.abajo.caracter != ' ':
                    resta_actualx = recurso.x - actual.x
                    resta_arriba = recurso.x - actual.arriba.x
                    if abs(resta_arriba) < abs(resta_actualx):
                        actual = actual.arriba
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #*VERIFICACION IZQUIERDA-ARRIBA
                elif actual.izquierda.caracter == ' ' and actual.arriba.caracter == ' ' and actual.derecha.caracter != ' ' and actual.abajo.caracter != ' ':
                    resta_actualx = recurso.x - actual.x
                    resta_arriba = recurso.x - actual.arriba.x
                    if abs(resta_arriba) < abs(resta_actualx):
                        actual = actual.arriba
                        actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #!VERIFICACION DERECHA-ABAJO
                elif actual.derecha.caracter == ' ' and actual.abajo.caracter == ' ' and actual.izquierda.caracter != ' ' and actual.arriba.caracter != ' ':
                    resta_actualx = recurso.x - actual.x
                    resta_abajo = recurso.x - actual.abajo.x
                    if abs(resta_abajo) < abs(resta_actualx):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #TODO VERIFICACION IZQUIERDA-ABAJO
                elif actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ' and actual.derecha.caracter != ' ' and actual.arriba.caracter != ' ':
                    resta_actualx = recurso.x - actual.x
                    resta_abajo = recurso.x - actual.abajo.x
                    if abs(resta_abajo) < abs(resta_actualx):
                        actual = actual.abajo
                        actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #& ----------CAMINOS LIBRES DE 3 DIRECCIONES----------------
                #~VERIFICACION ARRIBA-ABAJO-IZQUIERDA
                elif actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ' and actual.arriba.caracter == ' ' and actual.derecha.caracter != ' ':
                    resta_arriba = recurso.x - actual.arriba.x
                    resta_abajo = recurso.x -actual.abajo.x
                    resta_actual = recurso.y - actual.y
                    resta_izquierda = recurso.y - actual.izquierda.y
                    if abs(resta_izquierda) > abs(resta_actual):
                        if abs(resta_abajo)< abs(resta_arriba):
                            actual = actual.abajo
                            actual.caracter = 'P'
                        else:
                            actual = actual.arriba
                            actual.caracter = 'P'
                    else:
                        actual = actual.izquierda
                        actual.caracter = 'P'
                #^VERIFICACION ARRIBA-ABAJO-DERECHA
                elif actual.derecha.caracter == ' ' and actual.abajo.caracter == ' ' and actual.arriba.caracter == ' ' and actual.izquierda.caracter != ' ':
                    resta_arriba = recurso.x - actual.arriba.x
                    resta_abajo = recurso.x -actual.abajo.x
                    resta_actual = recurso.y - actual.y
                    resta_derecha = recurso.y - actual.derecha.y
                    if abs(resta_derecha) > abs(resta_actual):
                        if abs(resta_abajo)< abs(resta_arriba):
                            actual = actual.abajo
                            actual.caracter = 'P'
                        else:
                            actual = actual.arriba
                            actual.caracter = 'P'
                    else:
                        actual = actual.derecha
                        actual.caracter = 'P'
                #?VERIFICACION ARRIBA-IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.arriba.caracter == ' ' and actual.abajo.caracter != ' ':
                    resta_arriba = recurso.x - actual.arriba.x
                    resta_izquierda = recurso.y -actual.izquierda.y
                    resta_actual = recurso.x - actual.x
                    resta_derecha = recurso.y - actual.derecha.y
                    if abs(resta_arriba) > abs(resta_actual):
                        if abs(resta_izquierda)< abs(resta_derecha):
                            actual = actual.izquierda
                            actual.caracter = 'P'
                        else:
                            actual = actual.derecha
                            actual.caracter = 'P'
                    else:
                        actual = actual.arriba
                        actual.caracter = 'P'
                #*VERIFICACION ABAJO-IZQUIERDA-DERECHA
                elif actual.derecha.caracter == ' ' and actual.izquierda.caracter == ' ' and actual.abajo.caracter == ' ' and actual.arriba.caracter != ' ':
                    resta_abajo = recurso.x - actual.abajo.x
                    resta_izquierda = recurso.y -actual.izquierda.y
                    resta_actual = recurso.x - actual.x
                    resta_derecha = recurso.y - actual.derecha.y
                    if abs(resta_abajo) > abs(resta_actual):
                        if abs(resta_izquierda)< abs(resta_derecha):
                            actual = actual.izquierda
                            actual.caracter = 'P'
                        else:
                            actual = actual.derecha
                            actual.caracter = 'P'
                    else:
                        actual = actual.abajo
                        actual.caracter = 'P'
                elif actual.arriba.caracter != ' ' and actual.abajo.caracter != ' ' and actual.izquierda.caracter != ' ' and actual.derecha.caracter != ' ':
                    break
                else:
                    break
            print('El robot se encuentra en X: ' + str(actual.x) + ' , Y: ' + str(actual.y))
        if actual == recurso:
            messagebox.showinfo("Success","Mision cumplida!, Logramos extraer los recursos de la ciudad")
            self.GraficarMatrizExtraccionRecursos(matriz_aux,nombrec,robot,recurso,capinicial,aux)
        else:
            messagebox.showinfo("Fail","No se pudo completar la mision :(")
            self.GraficarMatrizExtraccionRecursos(matriz_aux,nombrec,robot,recurso,capinicial,aux)

        robot.capacidad = aux

'''
    def Rescate(self, celda, destino):
        contador = 0
        Camino = Pila()
        if celda.izquierda == destino:
            Camino.Apilar(celda)
            contador += 1
            return Camino
        elif celda.derecha == destino:
            Camino.Apilar(celda)
            contador += 1
            return Camino
        elif celda.abajo == destino:
            Camino.Apilar(celda)
            contador += 1
            return Camino
        elif celda.arriba == destino:
            Camino.Apilar(celda)
            contador += 1
        elif celda.arriba.caracter != ' ' and celda.abajo.caracter != ' ' and celda.derecha.caracter == ' ':
            Camino.Apilar(Mover('d',celda))
            contador += 1
        elif celda.derecha.caracter != ' ' and celda.arriba.caracter != ' ' and celda.abajo.caracter == ' ':
            Camino.Apilar(Mover('ab',celda))
            contador += 1
        elif celda.derecha.caracter != ' ' and celda.abajo.caracter != ' ' and celda.arriba.caracter == ' ':
            Camino.Apilar(Mover('ar',celda))
            contador += 1

        #!VERIFICACION ARRIBA-ABAJO
        elif celda.arriba.caracter == ' ' and celda.abajo.caracter == ' ' and celda.derecha.caracter != ' ':
            contador = 0
            if celda.abajo.caracter == ' ':
                Camino.Apilar(Mover('ab',celda))
                contador += 1
                if celda.
            elif celda.arriba.caracter == ' ':
                Camino.Apilar(Mover('ar',celda))
                contador += 1
            else:
                

        #?VERIFICACION DERECHA-ARRIBA
        elif celda.derecha.caracter == ' ' and celda.arriba.caracter == ' ' and celda.abajo.caracter != ' ':
            resta_actualx = unidadcivil.x - actual.x
            resta_arriba = unidadcivil.x - actual.arriba.x
            if abs(resta_arriba) < abs(resta_actualx):
                actual = actual.arriba
                actual.caracter = 'P'
            else:
                actual = actual.derecha
                actual.caracter = 'P'
        #!VERIFICACION DERECHA-ABAJO
        elif celda.derecha.caracter == ' ' and celda.abajo.caracter == ' '  and celda.arriba.caracter != ' ':
            resta_actualx = unidadcivil.x - actual.x
            resta_abajo = unidadcivil.x - actual.abajo.x
            if abs(resta_abajo) < abs(resta_actualx):
                actual = actual.abajo
                actual.caracter = 'P'
            else:
                actual = actual.derecha
                actual.caracter = 'P'

    def Mover(self, pos, celda):
        if pos == 'd':
            celda = celda.derecha
            return celda
        elif pos == 'i':
            celda = celda.izquierda
            return celda
        elif pos == 'ab':
            celda = celda.abajo
            return celda
        elif pos == 'ar':
            celda = celda.arriba
            return celda

'''

    def __len__(self):
        return self.tamanio