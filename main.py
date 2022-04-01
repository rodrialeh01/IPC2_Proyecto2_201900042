#IMPORTANDO LIBRERIAS
#-------------TKINTER-------------
import tkinter as tk
from tkinter import Button
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
#-------------PILLOW--------------
from PIL import ImageTk, Image
#---------------OS----------------
import os
#-----------ELEMENT-TREE----------
from xml.etree import ElementTree as et

#IMPORTANDO CLASES
from Estructuras.ListaCiudades import ListaCiudades
from Estructuras.ListaRobots import ListaRobots
from Estructuras.MatrizDispersa import MatrizDispersa
from Estructuras.ListaRecursos import ListaRecursos
from Estructuras.ListaUCiviles import ListaUCiviles
from Estructuras.ListaEntradas import ListaEntradas

#VARIABLES GLOBALES DE LAS LISTAS
Lista_Ciudades = ListaCiudades()
Lista_Robots = ListaRobots()


#VENTANA
ventana = tk.Tk()
ventana.title('Chapin-Warriors App')
ventana.geometry('1250x690')
ventana.resizable(0,0)
ventana.config(bg='#C8881F')
ventana.iconbitmap('icono.ico')

#LABEL
labelprincipal = Label(ventana, text='Chapin-Warriors', font='CenturyGothic 20 bold', fg='white', bg='#C8881F')
labelprincipal.place(x=110,y=25)

#IMAGEN DE LOGO
imagen = ImageTk.PhotoImage(Image.open('icono.ico').resize((70,70)))
ilabel = Label(image=imagen, bg='#C8881F')
ilabel.place(x=30, y=10)

#METODO PARA LEER UN ARCHIVO XML
def ProcesarArchivo(ruta):
    global Lista_Ciudades
    global Lista_Robots
    if ruta != "":
            archivo = et.parse(ruta)
            root = archivo.getroot()
            for i in range(len(root)):
                if root[i].tag == "listaCiudades":
                    for element in root[i]:
                        if Lista_Ciudades.verificarNombre(str(element[0].text)) == False:
                            Lista_Ciudades.InsertarCiudad(element[0].text,int(element[0].attrib.get('filas')),int(element[0].attrib.get('columnas')))
                            contador = 1
                            c = 1
                            cc = 1
                            ce = 1
                            for subelement in element:
                                if subelement.tag == "fila":
                                    contadorc = 1
                                    contenido = subelement.text.split('"')
                                    for caracter in contenido[1]:
                                        Lista_Ciudades.cola.matriz.InsertarNodo(int(subelement.attrib.get('numero')),contadorc,caracter,0)
                                        if caracter == 'R':
                                            Lista_Ciudades.cola.recursos.InsertarNodo(int(c),int(subelement.attrib.get('numero')),int(contadorc))
                                            c += 1
                                        elif caracter == 'C':
                                            Lista_Ciudades.cola.civiles.InsertarNodo(int(cc),int(subelement.attrib.get('numero')),int(contadorc))
                                            cc +=1
                                        elif caracter == 'E':
                                            Lista_Ciudades.cola.entradas.InsertarNodo(int(ce), int(subelement.attrib.get('numero')), int(contadorc))
                                            ce += 1
                                        contadorc+=1
                                elif subelement.tag == "unidadMilitar":
                                    celda = Lista_Ciudades.retornarNodo(str(element[0].text)).matriz.retornarNodo(int(subelement.attrib.get('fila')),int(subelement.attrib.get('columna')))
                                    capacidad = int(subelement.text)
                                    celda.caracter = 'M'
                                    celda.capacidad = capacidad
                                    contador += 1
                        else:
                            nodo = Lista_Ciudades.retornarNodo(str(element[0].text))
                            nodo.filas = int(element[0].attrib.get('filas'))
                            nodo.columnas = int(element[0].attrib.get('columnas'))
                            nodo.matriz = MatrizDispersa()
                            nodo.recursos = ListaRecursos()
                            nodo.civiles = ListaUCiviles()
                            nodo.entradas = ListaEntradas()
                            contador = 1
                            c = 1
                            cc = 1
                            ce = 1
                            for subelement in element:
                                if subelement.tag == "fila":
                                    contadorc = 1
                                    contenido = subelement.text.split('"')
                                    for caracter in contenido[1]:
                                        nodo.matriz.InsertarNodo(int(subelement.attrib.get('numero')),contadorc,caracter,0)
                                        if caracter == 'R':
                                            nodo.recursos.InsertarNodo(int(c),int(subelement.attrib.get('numero')),int(contadorc))
                                            c += 1
                                        elif caracter == 'C':
                                            nodo.civiles.InsertarNodo(int(cc),int(subelement.attrib.get('numero')),int(contadorc))
                                            cc += 1
                                        elif caracter == 'E':
                                            nodo.entradas.InsertarNodo(int(ce), int(subelement.attrib.get('numero')), int(contadorc))
                                            ce += 1
                                        contadorc+=1
                                elif subelement.tag == "unidadMilitar":
                                    celda = nodo.matriz.retornarNodo(int(subelement.attrib.get('fila')),int(subelement.attrib.get('columna')))
                                    capacidad = int(subelement.text)
                                    celda.caracter = 'M'
                                    celda.capacidad = capacidad
                                    contador += 1
                elif root[i].tag == "robots":
                    for element in root[i]:
                        for subelement in element:
                            if subelement.attrib.get('tipo') == "ChapinFighter":
                                cap = int(subelement.attrib.get('capacidad'))
                                if Lista_Robots.verificarNombre(subelement.text) == False:
                                    Lista_Robots.agregarNodo(str(subelement.attrib.get('tipo')),str(subelement.text),cap)
                                else:
                                    Lista_Robots.RetornarRobot(subelement.text).capacidad = cap 
                            elif subelement.attrib.get('tipo') == "ChapinRescue":
                                if Lista_Robots.verificarNombre(subelement.text) == False:
                                    Lista_Robots.agregarNodo(str(subelement.attrib.get('tipo')),str(subelement.text),0)


#ABRE UNA VENTANA PARA ELEGIR EL ARCHIVO
def Ruta():
    ruta = filedialog.askopenfilename(title='Cargar Archivo', filetypes = (("Text files", "*.xml*"), ("all files", "*.*")))
    return ruta

#FUNCION PARA PODER CARGAR UN ARCHIVO Y REALIZAR LAS OPERACIONES CORRESPONDIENTES
def CargarArchivo():
    ruta = Ruta()
    try:
        if ruta != "":
            ProcesarArchivo(ruta)
            agregar()
            messagebox.showinfo("Exito","Se cargó el archivo")
        else:
            messagebox.showinfo("Error","No se cargó ningun archivo")
    except:
        messagebox.showinfo("Error","Hubo un error al procesar el archivo")

#BOTON DE CARGAR ARCHIVO
botoncargar = Button(ventana,text='Cargar Archivo', font='arial 15', bg="white", command=CargarArchivo)
botoncargar.place(x=1050,y=25)

#LABEL DE SELECCIONAR UNA CIUDAD
label1 = Label(ventana, text='Selecciona una ciudad:', font='CenturyGothic 15', fg='black', bg='#C8881F')
label1.place(x=40,y=100)

#COMBOBOX DE CIUDADES
cociudades = ttk.Combobox(state='readonly')
cociudades.place(x=40,y=140)

#METODO PARA AGREGAR NOMBRES DE CIUDADES AL COMBOBOX
def agregar():
    global Lista_Ciudades
    mostrar = []
    a = Lista_Ciudades.cabeza
    while a != None:
        mostrar.append(str(a.nombre))
        a = a.siguiente
    cociudades['values']= mostrar
    cociudades.config(font='arial 12')

namemat = ''
imgCargar = None
imlabel = None

#METODO PARA ABRIR LA IMAGEN CREADA DEL MAPA
def AbrirImagen():
    global cociudades
    os.startfile('MapasGenerados\Matriz_'+cociudades.get()+'.png')

#BOTON PARA ABRIR LA IMAGEN
botveri = Button(ventana,text='Abrir Imagen',state= DISABLED, font='CenturyGothic 11', bg="white", command=AbrirImagen)
botveri.place(x=170,y=190)

#METODO PARA MOSTRAR EL MAPA DE LA CIUDAD EN LA VENTANA Y REALIZAR SIGUIENTES OPERACIONES
def MostrarCiudad():
    global Lista_Ciudades
    global cociudades
    global botveri
    if Lista_Ciudades.retornarNodo(cociudades.get()) != None:
        #messagebox.showinfo("Exito","Si existe la Ciudad y tiene" + str(Lista_Ciudades.retornarNodo(cociudades.get()).filas) + ' filas y '+ str(Lista_Ciudades.retornarNodo(cociudades.get()).columnas) + ' columnas')
        MostrarTR()
        Lista_Ciudades.GraficarMatriz(Lista_Ciudades.retornarNodo(cociudades.get()))
        CargarImagen()
        labels()
        lb()
        botveri['state'] = NORMAL
    elif cociudades.get() == "":
        messagebox.showinfo("Error","No ha seleccionado ninguna opcion")
    else:
        messagebox.showinfo("Error","No existe :(")

#METODO PARA MOSTRAR EL LABEL DE MAPA DE LA CIUDAD
def lb():
    global Lista_Ciudades
    global cociudades
    labelmap = Label(ventana, text='Mapa de la ciudad generado con ChapinEyes:', font='CenturyGothic 15', fg='black', bg='#C8881F')
    labelmap.place(x=350,y=60)

#METODO PARA MOSTRAR EL MAPA EN LA VENTANA
def CargarImagen():
    global imgCargar
    global imlabel
    imgCargar=ImageTk.PhotoImage(Image.open('MapasGenerados/Matriz_'+cociudades.get()+'.png').resize((850,550)))
    imlabel = Label(image=imgCargar)
    imlabel.place(x=350, y=100)

#BOTON DE MOSTRAR CIUDAD
botonverc = Button(ventana,text='Mostrar Ciudad', font='CenturyGothic 11', bg="white", command=MostrarCiudad)
botonverc.place(x=40,y=190)

corobotst = None

#COMBOBOX DE TIPOS DE ROBOTS
def MostrarTR():
    global corobotst
    label3 = Label(ventana, text='Selecciona una mision:', font='CenturyGothic 15', fg='black', bg='#C8881F')
    label3.place(x=40,y=240)

    corobotst = ttk.Combobox(state='readonly')
    corobotst.place(x=40,y=280)
    corobotst['values']= ['Mision de Extraccion de Recursos(ChapinFighter)', 'Mision de Rescate(ChapinRescue)']
    corobotst.config(font='arial 12')
    bot1()

botonr2 = None
botonr3 = None

#LABEL DE SELECCIONAR UN RECURSO
l2 = Label(text='Selecciona un recurso:', font='CenturyGothic 15', fg='black', bg='#C8881F')
#COMBOBOX DE LOS RECURSOS
coresources = ttk.Combobox(state='readonly')
#BOTON PARA REALIZAR LA MISION DE RECURSOS
botonr4 = Button(ventana,text='Seleccionar', font='CenturyGothic 11', bg="white")

#LABEL DE SELECCIONAR UNA UNIDAD CIVIL
lc = Label(text='Selecciona una Unidad Civil:', font='CenturyGothic 15', fg='black', bg='#C8881F')
#COMBOBOX DE LOS RECURSOS
cocivil = ttk.Combobox(state='readonly')
#BOTON PARA REALIZAR LA MISION DE RECURSOS
botonciv = Button(ventana,text='Seleccionar', font='CenturyGothic 11', bg="white")
#LABEL DE SELECCIONAR UNA ENTRADA
le = Label(text='Selecciona donde empieza la mision:', font='CenturyGothic 12', fg='black', bg='#C8881F')
#COMBOBOX DE LAS ENTRADAS
costart = ttk.Combobox(state='readonly')
#BOTON DE INICIAR LA MISION
botstart = Button(ventana,text='Iniciar la Mision', font='CenturyGothic 11', bg='white')

#METODO PARA MOSTRAR LAS OPCIONES DE ROBOT DISPONIBLES Y REALIZAR LAS OPERACIONES CORRESPONDIENTES
def tipoR():
    global corobotst
    global Lista_Ciudades
    global Lista_Robots
    global cociudades
    global l2
    global coresources
    global botonr3
    global botonr2
    global botonr4
    global lc
    global le
    global costart
    global botstart
    global cocivil
    global botonciv
    if corobotst.get()=="Mision de Extraccion de Recursos(ChapinFighter)":
        if len(Lista_Ciudades.retornarNodo(cociudades.get()).recursos) >0:
            if Lista_Robots.CantidadporTipo('ChapinFighter') == 0:
                messagebox.showinfo("Error","No se puede realizar misiones de extracción de recursos porque no cuenta con robots de tipo: ChapinFighter.")
            elif Lista_Robots.CantidadporTipo('ChapinFighter') == 1:
                if len(Lista_Ciudades.retornarNodo(cociudades.get()).recursos) == 0:
                    messagebox.showinfo("Error","No se puede realizar misiones de extracción de recursos porque esta ciudad no cuenta con recursos.")
                elif len(Lista_Ciudades.retornarNodo(cociudades.get()).recursos) == 1:
                    mre = messagebox.askyesno("Success","Solo existe el recurso con ID: " + str(Lista_Ciudades.retornarNodo(cociudades.get()).recursos.cabeza.id))
                    if mre == True:
                        print('OLI')
                elif len(Lista_Ciudades.retornarNodo(cociudades.get()).recursos) > 1:
                    recursos()
            else:
                RobotS('ChapinFighter')
                bot2()
            lc.place_forget()
            le.place_forget()
            cocivil.place_forget()
            costart.place_forget()
            botonciv.place_forget()
            botstart.place_forget()  
        else:
            messagebox.showinfo("Error","No existen recursos en esta ciudad")
    elif corobotst.get()=="Mision de Rescate(ChapinRescue)":
        if len(Lista_Ciudades.retornarNodo(cociudades.get()).civiles) > 0:
            if Lista_Robots.CantidadporTipo('ChapinRescue') == 0:
                messagebox.showinfo("Error","No se puede realizar misiones de extracción de recursos porque no cuenta con robots de tipo: ChapinRescue.")
            elif Lista_Robots.CantidadporTipo('ChapinRescue') == 1:
                if len(Lista_Ciudades.retornarNodo(cociudades.get()).civiles) == 0:
                    messagebox.showinfo("Error","No se puede realizar misiones de rescate porque esta ciudad no cuenta con Unidades Civiles")
                elif len(Lista_Ciudades.retornarNodo(cociudades.get()).civiles) == 1:
                    mciv = messagebox.askyesno("Success","Solo existe la unidad civil con ID: " + str(Lista_Ciudades.retornarNodo(cociudades.get()).civiles.cabeza.id))
                    if mciv == True:
                        print('OLIS')
                elif len(Lista_Ciudades.retornarNodo(cociudades.get()).civiles) > 1:
                    civiles()
            else:
                RobotS('ChapinRescue')
                bot3()
            l2.place_forget()
            le.place_forget()
            coresources.place_forget()
            costart.place_forget()
            botonr4.place_forget()   
            botstart.place_forget()  
        else:
            messagebox.showinfo("Error","No existen unidades civiles en esta ciudad")
    elif corobotst.get()=="":
        messagebox.showinfo("Error","No ha seleccionado ninguna opcion")
    else:
        messagebox.showinfo("Error","Seleccione una opcion correcta")

#METODO PARA EL BOTON DE ELEGIR EL TIPO DE ROBOT
def bot1():
    botonr1 = Button(ventana,text='Elegir Tipo', font='CenturyGothic 11', bg="white", command=tipoR)
    botonr1.place(x=40,y=320)

corobot = None

#METODO PARA MOSTRAR LOS LABEL Y EL COMBOBOX DE SELECCIONAR UN ROBOT
def RobotS(tipo):
    global corobot
    label2 = Label(ventana, text='Selecciona un Robot:', font='CenturyGothic 15', fg='black', bg='#C8881F')
    label2.place(x=40,y=350)

    corobot = ttk.Combobox(state='readonly')
    corobot.place(x=40,y=380)
    agregarR(tipo)

#METODO PARA AGREGAR ROBOTS AL COMBOBOX
def agregarR(tipo):
    global Lista_Robots
    global corobot
    a = Lista_Robots.cabeza
    corobot['values']= Lista_Robots.RetornarRobots(tipo)
    corobot.config(font='arial 12')

#METODO PARA OPERACIONES CON EL ROBOT SELECCIONADO
def MostrarRobot():
    global corobot
    global cociudades
    global Lista_Robots
    global Lista_Ciudades
    if Lista_Robots.RetornarRobot(corobot.get()) != None:
        if Lista_Robots.RetornarRobot(corobot.get()).tipo == 'ChapinFighter':
            if len(Lista_Ciudades.retornarNodo(cociudades.get()).recursos) == 0:
                messagebox.showinfo("Error","No se puede realizar misiones de extracción de recursos porque esta ciudad no cuenta con recursos.")
            elif len(Lista_Ciudades.retornarNodo(cociudades.get()).recursos) == 1:
                mre = messagebox.askyesno("Success","Solo existe el recurso con ID: " + str(Lista_Ciudades.retornarNodo(cociudades.get()).recursos.cabeza.id))
                if mre == True:
                    print('OLI')
            elif len(Lista_Ciudades.retornarNodo(cociudades.get()).recursos) > 1:
                recursos()
        elif Lista_Robots.RetornarRobot(corobot.get()).tipo == 'ChapinRescue':
            if len(Lista_Ciudades.retornarNodo(cociudades.get()).civiles) == 0:
                messagebox.showinfo("Error","No se puede realizar misiones de rescate porque esta ciudad no cuenta con Unidades Civiles")
            elif len(Lista_Ciudades.retornarNodo(cociudades.get()).civiles) == 1:
                mciv = messagebox.askyesno("Success","Solo existe la unidad civil con ID: " + str(Lista_Ciudades.retornarNodo(cociudades.get()).civiles.cabeza.id))
                if mciv == True:
                    print('OLIS')
            elif len(Lista_Ciudades.retornarNodo(cociudades.get()).civiles) > 1:
                civiles()
    elif corobot.get() == "":
        messagebox.showinfo("Error","No ha seleccionado ninguna opcion")
    else:
        messagebox.showinfo("Error","No existe :(")

#METODO PARA MOSTRAR EL BOTON DE SELECCIONAR EL ROBOT
def bot2():
    botonr2 = Button(ventana,text='Seleccionar', font='CenturyGothic 11', bg="white", command=MostrarRobot)
    botonr2.place(x=40,y=410)

#METODO PARA MOSTRAR EL COMBOBOX DE RECURSOS
def recursos():
    global Lista_Ciudades
    global cociudades
    global corobot
    global coresources
    l2.place(x=40,y=450)
    coresources.place(x=40,y=480)
    contenido = []
    listar = Lista_Ciudades.retornarNodo(cociudades.get()).recursos
    actual = listar.cabeza
    while actual != None:
        a = 'Recurso ' + str(actual.id) + ' Coordenada(' + str(actual.x) + ',' + str(actual.y) + ')'
        contenido.append(a)
        actual = actual.siguiente
    coresources['values']= contenido
    coresources.config(font='arial 12')
    bot4()

#METODO PARA MOSTRAR EL COMBOBOX DE UNIDADES CIVILES
def civiles():
    global Lista_Ciudades
    global cociudades
    global cocivil
    
    lc.place(x=40,y=450)
    cocivil.place(x=40,y=480)
    contenido = []
    listac = Lista_Ciudades.retornarNodo(cociudades.get()).civiles
    actual = listac.cabeza
    while actual != None:
        a = 'Unidad Civil ' + str(actual.id) + ' Coordenada(' + str(actual.x) + ',' + str(actual.y) + ')'
        contenido.append(a)
        actual = actual.siguiente
    cocivil['values']= contenido
    cocivil.config(font='arial 12')
    bot5()

#METODO PARA MOSTRAR EL BOTON DE SELECCIONAR EL RECURSO
def bot3():
    botonr3 = Button(ventana,text='Seleccionar', font='CenturyGothic 11', bg="white", command=MostrarRobot)
    botonr3.place(x=40,y=410)

#METODO PARA OBTENER EL INDICE DEL COMBOBOX
def ObtenerRecurso():
    global coresources
    global Lista_Ciudades
    global Lista_Robots
    if Lista_Robots.CantidadporTipo('ChapinFighter') > 1:
        print('Indice: ' + str(coresources.current()))
        prueba = messagebox.askyesno(title="Robot de Combate", message="Mision de Extracción de Recursos\n\nDatos del Robot:\n     Nombre: "+str(Lista_Robots.RetornarRobot(corobot.get()).nombre) +"\n     Capacidad: "+str(Lista_Robots.RetornarRobot(corobot.get()).capacidad) +" unidades.\n\nDatos del recurso seleccionado:\n     Recurso " + str(int(coresources.current())+1) + "\n     Coordenada en X: " + str(Lista_Ciudades.retornarNodo(cociudades.get()).recursos.retornarNodo(int(coresources.current()) + 1).x) + '\n     Coordenada en Y:' + str(Lista_Ciudades.retornarNodo(cociudades.get()).recursos.retornarNodo(int(coresources.current()) + 1).y) + '\n¿Acepta continuar con la misión?')
        if prueba == True:
            print('Holi')
            Entradas()
    else:
        prueba = messagebox.askyesno(title="Robot de Combate", message="Mision de Extracción de Recursos\n\nDatos del Robot:\n     Nombre: "+str(Lista_Robots.cabeza.nombre) +"\n     Capacidad: "+str(Lista_Robots.cabeza.capacidad) +" unidades.\n\nDatos del recurso seleccionado:\n     Recurso " + str(int(coresources.current())+1) + "\n     Coordenada en X: " + str(Lista_Ciudades.retornarNodo(cociudades.get()).recursos.retornarNodo(int(coresources.current()) + 1).x) + '\n     Coordenada en Y:' + str(Lista_Ciudades.retornarNodo(cociudades.get()).recursos.retornarNodo(int(coresources.current()) + 1).y) + '\n¿Acepta continuar con la misión?')
        if prueba == True:
            print('Holi')
            Entradas()

#METODO PARA PEDIR DONDE INICIE EL ROBOT
def Entradas():
    global le
    global Lista_Ciudades
    global cociudades
    global costart
    le.place(x=40,y=560)
    costart.place(x=40,y=590)
    listae = Lista_Ciudades.retornarNodo(cociudades.get()).entradas
    actual = listae.cabeza
    aux = []
    while actual != None:
        aux.append('Entrada' + str(actual.id) + '  x= ' + str(actual.x) + ' , y= ' + str(actual.y))
        actual = actual.siguiente
    costart['values']= aux
    corobot.config(font='arial 12')
    bstart()

#METODO PARA UBICAR EL BOTON
def bot4():
    global botonr4
    botonr4.place(x=40,y=520)
    botonr4['command'] = ObtenerRecurso

def bot5():
    global botonciv
    botonciv.place(x=40,y=520)
    botonciv['command'] = Entradas

def startmision():
    global costart
    global cociudades
    global coresources
    global cocivil
    global Lista_Ciudades
    global corobotst
    if corobotst.get()=="Mision de Extraccion de Recursos(ChapinFighter)":
        entrada = Lista_Ciudades.retornarNodo(cociudades.get()).entradas.retornarNodo(int(costart.current()) + 1)
        recurso = Lista_Ciudades.retornarNodo(cociudades.get()).recursos.retornarNodo(int(coresources.current()) + 1)
        Lista_Ciudades.Mision_Recursos(cociudades.get(),Lista_Robots.RetornarRobot(corobot.get()),entrada.x,entrada.y,recurso.x,recurso.y)
        
    elif corobotst.get()=="Mision de Rescate(ChapinRescue)":
        entrada = Lista_Ciudades.retornarNodo(cociudades.get()).entradas.retornarNodo(int(costart.current()) + 1)
        civil = Lista_Ciudades.retornarNodo(cociudades.get()).civiles.retornarNodo(int(cocivil.current()) + 1)
        Lista_Ciudades.Mision_Rescate(cociudades.get(),entrada.x,entrada.y,civil.x,civil.y,Lista_Robots.RetornarRobot(corobot.get()))

def bstart():
    global botstart
    botstart.place(x=40,y=630)
    botstart['command'] = startmision

#----------------------------------METODO PARA MOSTRAR LA INFO DEL MAPA EN LA VENTANA---------------------------
def labels():
    lblc0 = Label(ventana, text='***', font='CenturyGothic 10', fg='black', bg='black')
    lblc0.place(x=400,y=5)

    lblc00 = Label(ventana, text='Intransitable', font='CenturyGothic 12 bold', fg='black', bg='#C8881F')
    lblc00.place(x=420,y=5)

    lblc1 = Label(ventana, text='***', font='CenturyGothic 10', fg='#54DA22', bg='#54DA22')
    lblc1.place(x=600,y=5)

    lblc10 = Label(ventana, text='Punto de Entrada', font='CenturyGothic 12 bold', fg='black', bg='#C8881F')
    lblc10.place(x=620,y=5)

    lblc2 = Label(ventana, text='***', font='CenturyGothic 10', fg='white', bg='white')
    lblc2.place(x=850,y=5)

    lblc20 = Label(ventana, text='Camino', font='CenturyGothic 12 bold', fg='black', bg='#C8881F')
    lblc20.place(x=870,y=5)

    lblc3 = Label(ventana, text='***', font='CenturyGothic 10', fg='#9A0219', bg='#9A0219')
    lblc3.place(x=400,y=30)

    lblc30 = Label(ventana, text='Unidad Militar', font='CenturyGothic 12 bold', fg='black', bg='#C8881F')
    lblc30.place(x=420,y=30)

    lblc4 = Label(ventana, text='***', font='CenturyGothic 10', fg='#326CD8', bg='#326CD8')
    lblc4.place(x=600,y=30)

    lblc40 = Label(ventana, text='Unidad Civil', font='CenturyGothic 12 bold', fg='black', bg='#C8881F')
    lblc40.place(x=620,y=30)

    lblc5 = Label(ventana, text='***', font='CenturyGothic 10', fg='#9699A0', bg='#9699A0')
    lblc5.place(x=850,y=30)

    lblc40 = Label(ventana, text='Recurso', font='CenturyGothic 12 bold', fg='black', bg='#C8881F')
    lblc40.place(x=870,y=30)

ventana.mainloop()