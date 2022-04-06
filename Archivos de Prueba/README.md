# Archivos de Prueba
Los archivos deben de ser de tipo XML para que funcione en el programa y debe de contener la siguiente estructura:
* configuracion
    * listaCiudades
        * ciudad
            * nombre(Se añade el nombre de la ciudad, junto con la cantidad de fiulas y columnas): Nombre de la Ciudad
            * fila(Se añade el numero de fila): Se añade dentro la estructura de la fila donde debe contener:
                * 'E': Entrada
                * '*': Intransitable
                * ' ': Transitable
                * 'C': Unidad Civil
                * 'R': Recurso
            * unidadMilitar(Se añade el numero de fila y el numero de columna): Numero de capacidad
    * robots
        * robot
            * nombre(Se añade el tipo de robot y la capacidad si es necesario): Nombre del Robot