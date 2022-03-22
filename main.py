import tkinter as tk
from tkinter import Button
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

from xml.etree import ElementTree as et
from Estructuras.ListaCiudades import ListaCiudades
from Estructuras.ListaRobots import ListaRobots

Lista_Ciudades = ListaCiudades()
Lista_Robots = ListaRobots()

#VENTANA
ventana = tk.Tk()
ventana.title('Chapin-Warriors App')
ventana.geometry('1250x680')
ventana.resizable(0,0)
ventana.config(bg='#9A0219')
ventana.iconbitmap('icono.ico')

#LABEL
labelprincipal = Label(ventana, text='Chapin-Warriors', font='CenturyGothic 20 bold', fg='white', bg='#9A0219')
labelprincipal.place(x=110,y=25)

#IMAGEN DE LOGO
imagen = ImageTk.PhotoImage(Image.open('icono.ico').resize((60,60)))
ilabel = Label(image=imagen, bg='#9A0219')
ilabel.place(x=50, y=10)

#-------------------------------------------------------------------------
def ProcesarArchivo(ruta):
    global Lista_Ciudades
    global Lista_Robots
    if ruta != "":
            archivo = et.parse(ruta)
            root = archivo.getroot()
            for i in range(len(root)):
                if root[i].tag == "listaCiudades":
                    for element in root[i]:
                        print('Nombre: ' + str(element[0].text))
                        print('Cantidad de Filas: ' + str(element[0].attrib.get('filas')))
                        print('Cantidad de Columnas: ' + str(element[0].attrib.get('columnas')))
                        Lista_Ciudades.InsertarCiudad(element[0].text,int(element[0].attrib.get('filas')),int(element[0].attrib.get('columnas')))
                        contador = 1
                        for subelement in element:
                            if subelement.tag == "fila":
                                print('**************************')
                                print('Fila No.' + subelement.attrib.get('numero'))
                                print('Contenido: ' + str(subelement.text))
                                contadorc = 1
                                contenido = subelement.text.split('"')
                                for caracter in contenido[1]:
                                    Lista_Ciudades.cola.matriz.InsertarNodo(int(subelement.attrib.get('numero')),contadorc,caracter,0)
                                    contadorc+=1
                            elif subelement.tag == "unidadMilitar":
                                print('--------------------------')
                                print('Unidad Militar No.'  + str(contador))
                                print('Fila No.' + str(subelement.attrib.get('fila')))
                                print('Columna No. ' + str(subelement.attrib.get('columna')))
                                print('Capacidad: ' + str(subelement.text))
                                capacidad = int(subelement.text)
                                Lista_Ciudades.cola.matriz.InsertarNodo(int(subelement.attrib.get('fila')),int(subelement.attrib.get('columna')),'M',capacidad)
                                contador += 1

                elif root[i].tag == "robots":
                    print('----------------------------------------------')
                    for element in root[i]:
                        for subelement in element:
                            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                            print('Nombre: ' + str(subelement.text))
                            print('Tipo: ' + str(subelement.attrib.get('tipo')))
                            if subelement.attrib.get('tipo') == "ChapinFighter":
                                print('Capacidad: '+str(subelement.attrib.get('capacidad')))
                                cap = int(subelement.attrib.get('capacidad'))
                                Lista_Robots.agregarNodo(str(subelement.attrib.get('tipo')),str(subelement.text),cap)
                            elif subelement.attrib.get('tipo') == "ChapinRescue":
                                Lista_Robots.agregarNodo(str(subelement.attrib.get('tipo')),str(subelement.text),0)

#ABRE UNA VENTANA PARA ELEGIR EL ARCHIVO
def Ruta():
    ruta = filedialog.askopenfilename(title='Cargar Archivo', filetypes = (("Text files", "*.xml*"), ("all files", "*.*")))
    return ruta

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

botoncargar = Button(ventana,text='Cargar Archivo', font='arial 15', bg="white", command=CargarArchivo)
botoncargar.place(x=1050,y=25)

label1 = Label(ventana, text='Selecciona una ciudad:', font='CenturyGothic 15', fg='white', bg='#9A0219')
label1.place(x=40,y=150)

#COMBOBOX DE CIUDADES
cociudades = ttk.Combobox(state='readonly')
cociudades.place(x=40,y=190)

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
def MostrarCiudad():
    global Lista_Ciudades
    global cociudades
    if Lista_Ciudades.retornarNodo(cociudades.get()) != None:
        messagebox.showinfo("Exito","Si existe la Ciudad y tiene" + str(Lista_Ciudades.retornarNodo(cociudades.get()).filas) + ' filas y '+ str(Lista_Ciudades.retornarNodo(cociudades.get()).columnas))
        MostrarTR()
        Lista_Ciudades.GraficarMatriz(Lista_Ciudades.retornarNodo(cociudades.get()))
        CargarImagen()
    elif cociudades.get() == "":
        messagebox.showinfo("Error","No ha seleccionado ninguna opcion")
    else:
        messagebox.showinfo("Error","No existe :(")

def CargarImagen():
    global imgCargar
    global imlabel
    imgCargar=ImageTk.PhotoImage(Image.open('MapasGenerados/Matriz_'+cociudades.get()+'.png').resize((850,550)))
    imlabel = Label(image=imgCargar)
    imlabel.place(x=350, y=100)

botonverc = Button(ventana,text='Mostrar Ciudad', font='CenturyGothic 11', bg="white", command=MostrarCiudad)
botonverc.place(x=40,y=250)

corobotst = None

#COMBOBOX DE TIPOS DE ROBOTS
def MostrarTR():
    global corobotst
    label3 = Label(ventana, text='Selecciona un tipo de robot:', font='CenturyGothic 15', fg='white', bg='#9A0219')
    label3.place(x=40,y=300)

    corobotst = ttk.Combobox(state='readonly')
    corobotst.place(x=40,y=340)
    corobotst['values']= ['ChapinFighter', 'ChapinRescue']
    corobotst.config(font='arial 12')
    bot1()

def tipoR():
    global corobotst
    if corobotst.get()=="ChapinFighter":
        RobotS(corobotst.get())
        bot2()
    elif corobotst.get()=="ChapinRescue":
        RobotS(corobotst.get())
        bot3()
    elif corobotst.get()=="":
        messagebox.showinfo("Error","No ha seleccionado ninguna opcion")
    else:
        messagebox.showinfo("Error","Seleccione una opcion correcta")

def bot1():
    botonr1 = Button(ventana,text='Elegir Tipo', font='CenturyGothic 11', bg="white", command=tipoR)
    botonr1.place(x=40,y=380)

corobot = None
def RobotS(tipo):
    global corobot
    label2 = Label(ventana, text='Selecciona un Robot:', font='CenturyGothic 15', fg='white', bg='#9A0219')
    label2.place(x=40,y=420)

    corobot = ttk.Combobox(state='readonly')
    corobot.place(x=40,y=460)
    agregarR(tipo)

def agregarR(tipo):
    global Lista_Robots
    global corobot
    a = Lista_Robots.cabeza
    corobot['values']= Lista_Robots.RetornarRobots(tipo)
    corobot.config(font='arial 12')

def MostrarRobot():
    global corobot
    global Lista_Robots
    if Lista_Robots.RetornarRobot(corobot.get()) != None:
        messagebox.showinfo("Exito","Si existe el Robot")
    elif corobot.get() == "":
        messagebox.showinfo("Error","No ha seleccionado ninguna opcion")
    else:
        messagebox.showinfo("Error","No existe :(")

def bot2():
    botonr2 = Button(ventana,text='Realizar Mision de Rescate', font='CenturyGothic 11', bg="white", command=MostrarRobot)
    botonr2.place(x=40,y=500)

def bot3():
    botonr3 = Button(ventana,text='Realizar Mision de Extraccion de Recursos', font='CenturyGothic 11', bg="white", command=MostrarRobot)
    botonr3.place(x=40,y=500)

ventana.mainloop()