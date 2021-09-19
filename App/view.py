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

def printObrasXMedioArtista(lista):
    print("Las obras creadas con la téncia más popular del artista son: ")
    for obra in lista:
        print("Nombre de la obra: " + obra["Title"] + "Fecha de creación: " + obra["Date"] + "Medio/Técnica: " + obra["Medium"] + "Dimensiones: " + obra["Dimensions"])
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
    elif int(inputs[0]) == 4:
        nombre = input("Indique el nombre del artista del cual desea conocer cuál fue su técnica más usada")
        total_obras = controller.total_obras(catalog, nombre)
        print("El artista " + str(nombre) + "produjo un total de " +str(total_obras) + "obras")
        lista_obras_artista = controller.lista_total_tecnicas(catalog, nombre)
        lista_obras_artista_f = lista_obras_artista[0]
        print(lista_obras_artista[1])
        mas_frecuente = controller.tecnica_mas_utilizada(lista_obras_artista_f)
        mas_frecuente_f = mas_frecuente[0]
        lista_mega_final = controller.lista_tecnicas_mas_usadas(lista_obras_artista_f, mas_frecuente_f)
        print("El total de medios utilizados por el artista fue de: " + str(mas_frecuente[1]))
        printObrasXMedioArtista(lista_mega_final)
    else:
        sys.exit(0)
sys.exit(0)

