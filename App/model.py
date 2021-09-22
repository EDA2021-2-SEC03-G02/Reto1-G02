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
import operator
import math
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
        return True
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

def compareartworksmedium(artwork1,artwork2):
    if artwork1['Medium'] > artwork2['Medium']:
        return 1
    elif artwork1['Medium'] == artwork2['Medium']:
        return 0
    else:
        return -1
        
def compareartworkdepartment(artwork1,artwork2):
    if artwork1['Department'] > artwork2['Department']:
        return 1
    elif artwork1['Department'] == artwork2['Department']:
        return 0
    else:
        return -1

def compareArtistsYearBorn(artist1, artist2):
    a = int(artist1["BeginDate"])
    b = int(artist2["BeginDate"])
    if a < b:
        return 1
    else:
        return 0
    """a = int(artist1["BeginDate"])
    b = int(artist2["BeginDate"])
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1"""

# Funciones de ordenamiento

def sortArtworksDateAcquired(catalog, anio1, anio2, mes1, mes2, dia1, dia2):
    sublist  =  lt.newList(cmpfunction=compareartworks)
    strdateArt1=None
    obras =catalog["artworks"]
    dateArt1=datetime.datetime(int(anio1),int(mes1),int(dia1))
    dateArt2=datetime.datetime(int(anio2),int(mes2),int(dia2))
    for artwork in lt.iterator(obras):
        strdateArt1 = artwork['DateAcquired']
        if len(strdateArt1) == 0:
            year=1
            month=1
            day=1
        else:
            year=int(strdateArt1[0]+strdateArt1[1]+strdateArt1[2]+strdateArt1[3])
            month= int(strdateArt1[5]+strdateArt1[6])
            day= int(strdateArt1[8]+strdateArt1[9])
        dateArt3=datetime.datetime(year,month,day)
        if (dateArt3>= dateArt1) and (dateArt3<= dateArt2):
            lt.addLast(sublist, artwork)
            print('aaaa')
                     
    sub_list = sublist.copy()
    start_time = time.process_time()
    sorted_list = ms.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    print(str(sorted_list))

    purchaseList = lt.newList(cmpfunction=compareartworks)
    for artwork in lt.iterator(sorted_list):
        if "Purchase" in artwork["CreditLine"]:
            lt.addLast(purchaseList, artwork)
    listFirst3 = sorted_list.copy()
    print(listFirst3)
    if len(listFirst3)>2:
        first3= lt.subList(listFirst3,0,3)
        last3 = lt.subList(listFirst3, len(listFirst3)-3, 3)
    else:
        first3= lt.subList(listFirst3)
        last3 = lt.subList(listFirst3)  
                    
                       
    numPurchase = len(purchaseList)
    num = len(sorted_list)
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, num, numPurchase, first3, last3


#Funciones para requerimiento 3

def buscar_artista_constituentID(catalog, nombre):
    artistas = catalog["artists"]
    for artist in lt.iterator(artistas):
        if (str(nombre)) == (str(artist["DisplayName"])):
            return artist["ConstituentID"]
#LISTOOOOOO

def total_obras(catalog, nombre):
    id = buscar_artista_constituentID(catalog, nombre)
    obras = catalog["artworks"]
    contador = 0
    for obra in lt.iterator(obras):
        cadena = obra["ConstituentID"]
        cadena = cadena.replace("[","")
        cadena = cadena.replace("]","") 
        lista = cadena.split(",")
        for numero in lista:
            if str(id) == numero:
                contador += 1
    return contador
#LISTOOOOO

def lista_total_tecnicas(catalog, nombre):
    id = buscar_artista_constituentID(catalog, nombre)
    obras = catalog["artworks"]
    lista = lt.newList('ARRAY_LIST', cmpfunction=compareartworks)
    for obra in lt.iterator(obras):
        cadena = obra["ConstituentID"]
        cadena = cadena.replace("[","")
        cadena = cadena.replace("]","") 
        lista_nueva = cadena.split(",")
        for numero in lista_nueva:
            if str(id) == numero:
                lt.addLast(lista, obra)
    return lista, lt.size(lista)
#LISTOOOOOOO

def tecnica_mas_utilizada(lista):
    #ordenar por medio
    ms.sort(lista, compareartworksmedium)
    maxima = ""
    contadorM = -1
    actual = 0
    x = lt.getElement(lista, 1)
    actualO = x["Medium"]
    tecnicas = 1
    #revisar medio por medio con 4 variables: actual, contador actual, maximo, contador maximo
    for obra in lt.iterator(lista):
        if obra["Medium"] == actualO:
            actual += 1
            actualO = obra["Medium"]
        else:
            tecnicas += 1
            if actual>contadorM:
                maxima = actualO
                contadorM = actual
            actual = 1
            actualO = obra["Medium"]
    if actual>contadorM:
        maxima = actualO
        contadorM = actual
    return maxima, tecnicas
#LISTOOOOOO

def lista_tecnicas_mas_usadas(lista, tecnica):
    x = lt.newList(cmpfunction=compareartworks)
    for obra in lt.iterator(lista):
        if obra["Medium"] == tecnica:
            lt.addLast(x, obra)
    return x
#LISTOOOOOO

#Req 4
def ClasificaconPorNacionalidades(catalog):

    obras =catalog["artworks"]
    artistas = catalog["artists"]
    idArtistas = lt.newList(cmpfunction=compareartworks)
    for artwork in lt.iterator(obras):
        lt.addLast(idArtistas, artwork['ConstituentID'])         
    print(idArtistas)
    diccPaises={}
    i=0
    for artista in lt.iterator(artistas):
        while i < len(idArtistas):
            if artista['ConstituentID'] in idArtistas[i]:
                if artista["Nationality"] not in diccPaises:
                   diccPaises[artista["Nationality"]]=1
                else:
                   diccPaises[artista["Nationality"]]+=1    
            i+=1

    print(str(diccPaises))            

    aaaa=""

    return aaaa



    
    

    


#Funciones para requerimiento 1
def sublistaRangoArtistas(catalog, year1, year2):
    artistas = catalog["artists"]
    artistas = ms.sort(artistas, compareArtistsYearBorn)
    sublist = lt.newList(cmpfunction=compareartist)
    for artist in lt.iterator(artistas):
        year = int(artist["BeginDate"])
        if year !=0:   
            if year >= year1 and year <= year2:
                lt.addLast(sublist, artist)
    return sublist, lt.size(sublist)


def ArtistasNacimientoPrimeros3(lista):
    sublista = lt.subList(lista, 1, 3)
    return sublista

def ArtistasNacimientoUltimos3(lista):
    sublista = lt.subList(lista, lt.size(lista)-3, 3)
    return sublista


#Funciones para requerimiento 1

def ListaPorDepto(catalog, depto):
    obras = catalog["artworks"]
    obras_ordenadas = ms.sort(obras, compareartworkdepartment)
    sublist = lt.newList(cmpfunction=compareartworks)
    for obra in lt.iterator(obras_ordenadas):
        if obra["Department"] == depto:
            lt.addLast(sublist, obra)
    for x in lt.iterator(obras_ordenadas):
        if x["Depth (cm)"] == "":
            respuesta = "NO"
        else:
            respuesta = x["Depth (cm)"]
        if x["Diameter (cm)"] == "":
            y = "NO"
        else: 
            y = x["Diameter (cm)"]
        if x["Height (cm)"] == "":
            z = "NO"
        else: 
            z = x["Height (cm)"]
        if x["Length (cm)"] == "":
            a = "NO"
        else: 
            a = x["Length (cm)"]

        if x["Width (cm)"] == "":
            b = "NO"
        else: 
            b = x["Width (cm)"]
        print("Profundidad: " +respuesta + "---Diametro: "+ y + "---Height: " + z+ "---Length: "+a+"---Width (cm): "+b)

    return obra, lt.size(sublist)

def CalcularCostoEnvioObra(obra):
    final = 0
    peso = 0
    if obra["Weight (kg)"] !="":
        peso = float(obra["Weight (kg)"])
    costo_k = peso*72
    costo = 43
    #Cuando se tiene diametro
    if obra["Diameter (cm)"] != "0" and obra["Diameter (cm)"] != "":
        diametro = float(obra["Diameter (cm)"])
        #Diametro con altura, como un cilindro
        if obra["Height (cm)"] != "0" and obra["Height (cm)"] != "": 
            altura = float(obra["Height (cm)"])
            volumen = (2*math.pi*((diametro/2)**2))*(altura)
            costo = (9/125000)*volumen
            #(72usd/m^3 es equivalente a (9/125000)/cm^3)
        #Diametro solo, entonces círculo
        else:
            area = (2*math.pi*((diametro/2)**2))
            costo = (9/1250)*area
            #(72usd/m^2 es equivalente a (9/1250)/cm^2)
    else:
        #Hay Profundidad, volumen
        if obra["Depth (cm)"] != "0" and obra["Depth (cm)"] != "":
            profundidad = float(obra["Depth (cm)"])
            height = float(obra["Height (cm)"])
            length = float(obra["Length (cm)"])
            width = float(obra["Width (cm)"])
            #Caso 1: Se se tiene height y length, pero no width
            if (obra["Height (cm)"] != "0" and obra["Height (cm)"] != "") and (obra["Length (cm)"] != "0" and obra["Length (cm)"] != "") and (obra["Width (cm)"] == "0" or obra["Width (cm)"] == ""):
                volumen = profundidad*height*length
                costo = (9/125000)*volumen
            #Caso 2: Si se tiene height y width, pero no length
            elif (obra["Height (cm)"] != "0" and obra["Height (cm)"] != "") and (obra["Length (cm)"] == "0" or obra["Length (cm)"] == "") and (obra["Width (cm)"] != "0" and obra["Width (cm)"] != ""):
                volumen = profundidad*height*width
                costo = (9/125000)*volumen
            #Caso 3: Si se tiene length y width, pero no height
            else:
                volumen = profundidad*length*width
                costo = (9/125000)*volumen
        #No hay profundidad, solo área
        else:
            height = float(obra["Height (cm)"])
            length = float(obra["Length (cm)"])
            width = float(obra["Width (cm)"])
            #Caso 1: Se se tiene height y length, pero no width
            if (obra["Height (cm)"] != "0" and obra["Height (cm)"] != "") and (obra["Length (cm)"] != "0" and obra["Length (cm)"] != "") and (obra["Width (cm)"] == "0" or obra["Width (cm)"] == ""):
                area = height*length
                costo = (9/1250)*area
            #Caso 2: Si se tiene height y width, pero no length
            elif (obra["Height (cm)"] != "0" and obra["Height (cm)"] != "") and (obra["Length (cm)"] == "0" or obra["Length (cm)"] == "") and (obra["Width (cm)"] != "0" and obra["Width (cm)"] != ""):
                area = height*width
                costo = (9/1250)*area
            #Caso 3: Si se tiene length y width, pero no height
            else:
                area = length*width
                costo = (9/1250)*area
    if costo > costo_k:
        final = costo
    else:
        final = costo_k
    return final
    
    


        





