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


import config as cf
from DISClib.ADT import list as lt
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

    catalog['artists'] = lt.newList(cmpfunction=compareartist)
    catalog['artworks'] = lt.newList(cmpfunction=compareartworks)
    return catalog

def addArtwork(catalog, artwork):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['artworks'], artwork)

def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)

def getLast3Artists(catalog):
    artists = catalog['artists']
    sublista = lt.subList(artists, (len(artists))-3, (len(artists))-1)
    print(lt.size(sublista))
    return sublista


def lastThreeArtworks(catalog):
    artworks = catalog['artworks']
    sublista = lt.subList(artworks, (len(artworks))-3, (len(artworks))-1)
    print(lt.size(sublista))
    return sublista

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

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