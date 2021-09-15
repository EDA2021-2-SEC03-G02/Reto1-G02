"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import sys


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")

def initCatalog():
    """
    Inicializa el catalogo de obras
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga las obras en la estructura de datos
    """
    controller.loadData(catalog)

def Last3Artists(catalog):
    return controller.getLast3Artists(catalog)

def Last3Artworks(catalog):
    return controller.getLast3Artworks(catalog)


def printSortResultsArtworks(ord_artworks, sample=10):
    size = lt.size(ord_artworks)
    if size>sample:
        print("Las primeras", sample, "obras ordenadas son:")
        i = 1
        while i <= sample:
            artwork = lt.getElement(ord_artworks,i)
            print("Identificador único de la obra: " + artwork["ObjectID"] + " Día de adquisición: " + artwork["DateAcquired"] )
            i += 1
    pass

catalog = None
a=None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una  opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        print("Los últimos 3 artistas son: ")
        a=lt.newList()
        a=Last3Artists(catalog)
        print(a)
        print("Las últimas 3 obras son: ")
        a=lt.newList()
        a1=Last3Artworks(catalog)
        print(a1)
    elif int(inputs[0]) == 2:
        pass
    elif int(inputs[0])== 3:
        size = int(input("Indique tamaño de la muestra: "))
        if size > lt.size(catalog["artworks"]):
            print("Elija un tamaño válido, menor o igual a la cantidad total de obras")
        else:
            result = controller.sortArtworksDateAcquired(catalog, size) 
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
            printSortResultsArtworks(result[1])
    else:
        sys.exit(0)
sys.exit(0)
