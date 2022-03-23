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
ventana.geometry('1250x690')
ventana.resizable(0,0)
ventana.config(bg='#C8881F')
ventana.iconbitmap('icono.ico')

#LABEL
labelprincipal = Label(ventana, text='Chapin-Warriors', font='CenturyGothic 20 bold', fg='white', bg='#C8881F')
labelprincipal.place(x=110,y=25)

#IMAGEN DE LOGO
imagen = ImageTk.PhotoImage(Image.open('icono.ico').resize((60,60)))
ilabel = Label(image=imagen, bg='#C8881F')
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
                        c = 1
                        for subelement in element:
                            if subelement.tag == "fila":
                                print('**************************')
                                print('Fila No.' + subelement.attrib.get('numero'))
                                print('Contenido: ' + str(subelement.text))
                                contadorc = 1
                                contenido = subelement.text.split('"')
                                for caracter in contenido[1]:
                                    Lista_Ciudades.cola.matriz.InsertarNodo(int(subelement.attrib.get('numero')),contadorc,caracter,0)
                                    if caracter == 'R':
                                        Lista_Ciudades.cola.recursos.InsertarNodo(int(c),int(subelement.attrib.get('numero')),int(contadorc))
                                        c += 1
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

label1 = Label(ventana, text='Selecciona una ciudad:', font='CenturyGothic 15', fg='black', bg='#C8881F')
label1.place(x=40,y=100)


#COMBOBOX DE CIUDADES
cociudades = ttk.Combobox(state='readonly')
cociudades.place(x=40,y=140)

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
        messagebox.showinfo("Exito","Si existe la Ciudad y tiene" + str(Lista_Ciudades.retornarNodo(cociudades.get()).filas) + ' filas y '+ str(Lista_Ciudades.retornarNodo(cociudades.get()).columnas) + ' columnas')
        MostrarTR()
        Lista_Ciudades.GraficarMatriz(Lista_Ciudades.retornarNodo(cociudades.get()))
        CargarImagen()
        labels()
        lb()
    elif cociudades.get() == "":
        messagebox.showinfo("Error","No ha seleccionado ninguna opcion")
    else:
        messagebox.showinfo("Error","No existe :(")

def lb():
    global Lista_Ciudades
    global cociudades
    labelmap = Label(ventana, text='Mapa de la ciudad de ' + str(Lista_Ciudades.retornarNodo(cociudades.get()).nombre) + ':', font='CenturyGothic 15', fg='black', bg='#C8881F')
    labelmap.place(x=350,y=60)


def CargarImagen():
    global imgCargar
    global imlabel
    imgCargar=ImageTk.PhotoImage(Image.open('MapasGenerados/Matriz_'+cociudades.get()+'.png').resize((850,550)))
    imlabel = Label(image=imgCargar)
    imlabel.place(x=350, y=100)

botonverc = Button(ventana,text='Mostrar Ciudad', font='CenturyGothic 11', bg="white", command=MostrarCiudad)
botonverc.place(x=40,y=190)

corobotst = None

#COMBOBOX DE TIPOS DE ROBOTS
def MostrarTR():
    global corobotst
    label3 = Label(ventana, text='Selecciona un tipo de robot:', font='CenturyGothic 15', fg='black', bg='#C8881F')
    label3.place(x=40,y=240)

    corobotst = ttk.Combobox(state='readonly')
    corobotst.place(x=40,y=280)
    corobotst['values']= ['ChapinFighter', 'ChapinRescue']
    corobotst.config(font='arial 12')
    bot1()
botonr2 = None
botonr3 = None
def tipoR():
    global corobotst
    global Lista_Ciudades
    global cociudades
    global botonr3
    global botonr2
    if corobotst.get()=="ChapinFighter":
        RobotS(corobotst.get())
        bot2()
    elif corobotst.get()=="ChapinRescue":
        if Lista_Ciudades.retornarNodo(cociudades.get()).matriz.civiles('C') == True:
            RobotS(corobotst.get())
            bot3()
        else:
            messagebox.showinfo("Error","No existen unidades civiles en esta ciudad")
    elif corobotst.get()=="":
        messagebox.showinfo("Error","No ha seleccionado ninguna opcion")
    else:
        messagebox.showinfo("Error","Seleccione una opcion correcta")

def bot1():
    botonr1 = Button(ventana,text='Elegir Tipo', font='CenturyGothic 11', bg="white", command=tipoR)
    botonr1.place(x=40,y=320)

corobot = None
def RobotS(tipo):
    global corobot
    label2 = Label(ventana, text='Selecciona un Robot:', font='CenturyGothic 15', fg='black', bg='#C8881F')
    label2.place(x=40,y=360)

    corobot = ttk.Combobox(state='readonly')
    corobot.place(x=40,y=400)
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
        if Lista_Robots.RetornarRobot(corobot.get()).tipo == 'ChapinFighter':
            prueba = messagebox.askyesno(title="Robot de Combate", message="El robot seleccionado contiene la capacidad de "+str(Lista_Robots.RetornarRobot(corobot.get()).capacidad) + " unidades\n Desea continuar con la mision?")
            if prueba == True:
                print('Holi')
        elif Lista_Robots.RetornarRobot(corobot.get()).tipo == 'ChapinRescue':
            recursos()
            messagebox.showinfo("Exito","Si existe el Robot")
    elif corobot.get() == "":
        messagebox.showinfo("Error","No ha seleccionado ninguna opcion")
    else:
        messagebox.showinfo("Error","No existe :(")

def bot2():
    botonr2 = Button(ventana,text='Seleccionar', font='CenturyGothic 11', bg="white", command=MostrarRobot)
    botonr2.place(x=40,y=440)

def recursos():
    global Lista_Ciudades
    global cociudades
    label2 = Label(ventana, text='Selecciona un recurso:', font='CenturyGothic 15', fg='black', bg='#C8881F')
    label2.place(x=40,y=500)
    coresources = ttk.Combobox(state='readonly')
    coresources.place(x=40,y=550)
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

def bot3():
    botonr3 = Button(ventana,text='Seleccionar', font='CenturyGothic 11', bg="white", command=MostrarRobot)
    botonr3.place(x=40,y=440)

def bot4():
    botonr4 = Button(ventana,text='Realizar Mision', font='CenturyGothic 11', bg="white", command=MostrarRobot)
    botonr4.place(x=40,y=600)

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