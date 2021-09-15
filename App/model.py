"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import datetime
import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as inser
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None}

    TipoDeLista= input('¿Cómo desea guardar el catálogo del museo?(ll = Linked_list, al = Array_List))  ')
    if TipoDeLista == 'll':
        catalog['artists'] = lt.newList('SINGLE_LINKED', cmpfunction=compareartist)
        catalog['artworks'] = lt.newList('SINGLE_LINKED', cmpfunction=compareartworks)
    elif TipoDeLista == 'al':
        catalog['artists'] = lt.newList('ARRAY_LIST', cmpfunction=compareartist)
        catalog['artworks'] = lt.newList('ARRAY_LIST', cmpfunction=compareartworks)
    else:
        return 'Error'
    return catalog

def addArtwork(catalog, artwork):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['artworks'], artwork)

def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)

def getLast3Artists(catalog):
    artists = catalog['artists']
    sublista = lt.subList(artists, (len(artists))-3, 3)
    return sublista


def lastThreeArtworks(catalog):
    artworks = catalog['artworks']
    sublista = lt.subList(artworks, (len(artworks))-3, 3)
    return sublista

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    :
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """

    strdateArt1= artwork1['DateAcquired']
    if len(strdateArt1) == 0:
        return False
    year1=int(strdateArt1[0]+strdateArt1[1]+strdateArt1[2]+strdateArt1[3])
    month1=int(strdateArt1[5]+strdateArt1[6])
    day1=int(strdateArt1[8]+strdateArt1[9])
    dateArt1=datetime.datetime(year1,month1,day1)

    strdateArt2= artwork2['DateAcquired']
    if len(strdateArt2) == 0:
        return False
    year2=int(strdateArt2[0]+strdateArt2[1]+strdateArt2[2]+strdateArt2[3])
    month2=int(strdateArt2[5]+strdateArt2[6])
    day2=int(strdateArt2[8]+strdateArt2[9])
    dateArt2=datetime.datetime(year2,month2,day2)

    if dateArt1 < dateArt2:
        return True
    else:
        return False 
    



def compareartist(artistname1, artist):
    if artistname1['ConstituentID'] > artist['ConstituentID']:
        return 1
    elif artistname1['ConstituentID'] == artist['ConstituentID']:
        return 0
    else:
        return -1

def compareartworks(artworkname1,artwork):
    if artworkname1['ObjectID'] > artwork['ObjectID']:
        return 1
    elif artworkname1['ObjectID'] == artwork['ObjectID']:
        return 0
    else:
        return -1
# Funciones de ordenamiento

def sortArtworksDateAcquired(catalog, size):
    sub_list = lt.subList(catalog['artworks'], 1, size)
    sub_list = sub_list.copy()
    TipoDeOrdenamiento = input("¿Qué tipo de ordenamiento desea utilizar? \n'is':para InsertionSort \n 'ms': para MergeSort \n 'qs': para QuickSort \n 'sa': Para ShellSort ")
    start_time = time.process_time()
    if TipoDeOrdenamiento == 'is':
        sorted_list = inser.sort(sub_list, cmpArtworkByDateAcquired)
    elif TipoDeOrdenamiento == 'ms':
        sorted_list = ms.sort(sub_list, cmpArtworkByDateAcquired)
    elif TipoDeOrdenamiento == 'qs':
        sorted_list = qs.sort(sub_list, cmpArtworkByDateAcquired)
    elif TipoDeOrdenamiento == 'sa':
        sorted_list = sa.sort(sub_list, cmpArtworkByDateAcquired)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
