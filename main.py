from xml.etree import ElementTree as et
from Estructuras.ListaCiudades import ListaCiudades

Lista_Ciudades = ListaCiudades()
def ProcesarArchivo(ruta):
    if ruta != "":
            archivo = et.parse(ruta)
            root = archivo.getroot()
            for i in range(len(root)):
                if root[i].tag == "listaCiudades":
                    for element in root[i]:
                        print('Nombre: ' + str(element[0].text))
                        print('Cantidad de Filas: ' + str(element[0].attrib.get('filas')))
                        print('Cantidad de Columnas: ' + str(element[0].attrib.get('columnas')))
                        Lista_Ciudades.InsertarCiudad(element[0].text,element[0].attrib.get('filas'),element[0].attrib.get('columnas'))
                        contador = 1
                        for subelement in element:
                            if subelement.tag == "fila":
                                print('**************************')
                                print('Fila No.' + subelement.attrib.get('numero'))
                                print('Contenido: ' + str(subelement.text))
                                contadorc = 1
                                contenido = subelement.text.split('"')
                                for caracter in contenido[1]:
                                    Lista_Ciudades.cola.matriz.InsertarNodo(int(subelement.attrib.get('numero')),contadorc,caracter)
                                    contadorc+=1
                            elif subelement.tag == "unidadMilitar":
                                print('--------------------------')
                                print('Unidad Militar No.'  + str(contador))
                                print('Fila No.' + str(subelement.attrib.get('fila')))
                                print('Columna No. ' + str(subelement.attrib.get('columna')))
                                print('Capacidad: ' + str(subelement.text))
                                Lista_Ciudades.cola.matriz.InsertarNodo(int(subelement.attrib.get('fila')),int(subelement.attrib.get('columna')),'M')
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

ProcesarArchivo('Archivos de Prueba\Prueba1.xml')