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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """ 
    Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    videos
    views
    pais
    category id
    categoria

    Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'views': None,
               'country': None,
               'category_id': None,
               'category': None
                }

    """
    A continuacion se crean indices por diferentes criterios
    para llegar a la informacion consultada.  Estos indices no
    replican informacion, solo referencian los libros de la lista
    creada en el paso anterior.
    """

    """
    Este indice crea una lista cuya llave es el id
    """
    catalog['videos'] = lt.newList("ARRAY_LIST", cmpfunction = comparevideo_id1)

    """
    Este indice crea un map cuya llave es el video id, los views, los likes, el country y el category_id
    """
    catalog['video_id'] = mp.newMap(800,
                                   maptype='PROBING',
                                   loadfactor=0.80,
                                   comparefunction=comparevideo_id1)
    
    catalog['views'] = mp.newMap(800,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=comparevideo_id1)

    catalog['likes'] = mp.newMap(5000,
                                maptype='CHAINING',
                                loadfactor=2.0,
                                comparefunction=comparevideo_id1)

    catalog['country'] = mp.newMap(5000,
                            maptype='CHAINING',
                            loadfactor=2.0,
                            comparefunction=comparepais)

    catalog['category_id'] = mp.newMap(5000,
                            maptype='CHAINING',
                            loadfactor=2.0,
                            comparefunction=comparecategoryid)
    """
    Este indice crea un lista cuya llave es la categoria
    """
    catalog['category'] = lt.newList("ARRAY_LIST", cmpfunction = comparevideo_id1)

    return catalog




# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    """
    Añade un video al final, de la lista recibida
    """
    lt.addLast(catalog['videos'], video)
    mp.put(catalog['video_id'], video['video_id'], video)


def addCategory(catalog, category):
    """
    Añade una categoria al final, de la lista recibida
    """
    lt.addLast(catalog['category'], category)


def addCountry(catalog, video):
    """
    Añade un pais al final, de la lista recibida
    """
    pais = video['country']
    contiene = mp.contains(catalog['country'], pais)

    if not contiene:
        videos_pais = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(videos_pais, video)
        mp.put(catalog['country'], pais, videos_pais)
    else:
        obtener = mp.get(catalog['country'], pais)
        valor = me.getValue(obtener)
        lt.addLast(valor, video)


def addCategory_id(catalog, video):
    """
    Añade un category_id al final, de la lista recibida
    """

    lt.addLast(catalog['category_id'], video)
    mp.put(catalog['category_id'], video['category_id'], video)





# FUNCIONES RETO 2











# Funciones utilizadas para comparar elementos dentro de una lista

def comparevideo_id1(video1, video2):

    """
    Devuelve verdadero (True) si los 'id' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'video_id'
    video2: informacion del segundo video que incluye su valor 'video_id'
    """
    return str(video1) < str(video2["key"])

def cmpVideosByID_date (video1, video2):

    """
    Devuelve verdadero (True) si los 'id' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'video_id'
    video2: informacion del segundo video que incluye su valor 'video_id'
    Y si los id son iguales los compara por su trending date
    """
    if video1 != video2['key']:
        return video1 < video2["key"]   
    else:
        return video1["trending_date"] < video2["trending_date"]

def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son mayores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return (float(video1) > float(video2['key']))

def cmpVideosByLikes(video1, video2):
    """
    Devuelve verdadero (True) si los 'likes' de video1 son mayores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'likes'
    video2: informacion del segundo video que incluye su valor 'likes'
    """
    #return (float(video1['likes']) > float(video2['likes']))

    if (video1['likes'] == video2['likes']):
        return 0
    elif video1['likes'] > video2['likes']:
        return 1
    else:
        return -1

def comparepais(video1, video2):

    """
    Devuelve verdadero (True) si los 'id' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'video_id'
    video2: informacion del segundo video que incluye su valor 'video_id'
    """
    return video1 < video2["key"]

def comparecategoryid(video1, video2):
    """
    Devuelve verdadero (True) si los 'id' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'video_id'
    video2: informacion del segundo video que incluye su valor 'video_id'
    """
    return (float(video1) < float(video2['key']))

def cmpVideosByViews2(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son mayores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return (float(video1['views']) > float(video2['views']))




# Funciones de ordenamiento

#1
def sortVideosByViews (lista_filtros, cantidad):
    """
    Ordena la lista recibida organizando los datos segun sus Views
    Y crea una lista nueva para guardar los datos allí, para retornar su copia
    """
    sorted_list = mergesort.sort(lista_filtros, cmpVideosByViews2)

    sub_list = lt.subList(sorted_list, 1, cantidad)
    sub_list = sub_list.copy()

    return sub_list




#1 y 3

def get_id_categoria(catalog, categoria):
    """
    Busca una categoria en especifica del catalog, y retorna su respectivo id
    """
    id_categoria = None

    for cate in lt.iterator(catalog['category']):
        if cate['name'].strip() == categoria: 
            id_categoria = int(cate['id'])
            break

    return id_categoria


#1

def filtrar_pais_categoria (catalog, pais, id_categoria):
    """
    Crea una lista nueva para ordenar los datos segun su pais.
    Y recorre la lista dada, para guardar en la nueva lista 
    solo los videos que correspondan con el pais y la categoria
    """
    nueva_lista = catalog['videos'] = lt.newList("ARRAY_LIST", cmpfunction = cmpVideosByViews)

    mapa = mp.get(catalog['country'], pais)
    mapa = me.getValue(mapa)
    for i in mapa['elements']:
        if i['category_id'] == str(id_categoria):
                lt.addLast(nueva_lista, i)
    return nueva_lista

def organizar_ma_me(catalog, cantidad):
    """
    Organiza la lista segun el parametro necesario
    """
    return sortVideosByViews(catalog, cantidad)


#2

def filtrar_pais (catalog, pais):
    """
    Crea una lista nueva para ordenar los datos segun su pais.
    Y recorre la lista dada, para guardar en la nueva lista 
    solo los videos que correspondan con el respectivo pais
    """
    lista_pais = mp.newMap(comparefunction=comparevideo_id1)

    mapa = mp.get(catalog['country'], pais)
    mapa = me.getValue(mapa)

    for x in range(1, lt.size(mapa)):
        cada_mapa = lt.getElement(mapa, x)
        contiene = mp.contains(lista_pais, cada_mapa["video_id"])

        if not contiene:
            cada_video = {}
            cada_video["title"] = cada_mapa["title"]
            cada_video["country"] = cada_mapa["country"]
            cada_video["channel_title"] = cada_mapa["channel_title"]
            cada_video["days"] = 1

            mp.put(lista_pais, cada_mapa["video_id"], cada_video)
        else:
             llave = mp.get(lista_pais, cada_mapa["video_id"])
             valor = me.getValue(llave)
             valor["days"] += 1
        


    return lista_pais


def mejor_pais (catalog, lista_pais):
    """
    A traves de contadores se haya el pais que
    tenga mas views y se retorna el respectivo
    """
    mejor_total = {}
    mejor_parcial = 0

    valores = mp.valueSet(lista_pais)

    for x in range(0, lt.size(valores)):
        mapa = lt.getElement(valores, x)

        if mapa["days"] > mejor_parcial:
            mejor_parcial = mapa["days"]
            mejor_total = mapa
    
    return mejor_total



#3
def filtrar_categoria (catalog, categoria):
    """
    Crea una lista nueva para ordenar los datos segun su categoria.
    Y recorre la lista dada, para guardar en la nueva lista 
    solo los videos que correspondan con el respectivo pais
    """
    lista_categ = mp.newMap(comparefunction=cmpVideosByID_date)
    print(catalog)

    mapa = mp.get(catalog['videos'], categoria)
    mapa = me.getValue(mapa)

    for x in range(1, lt.size(mapa)):
        cada_mapa = lt.getElement(mapa, x)
        contiene = mp.contains(lista_categ, cada_mapa["video_id"])

        if not contiene:
            cada_video = {}
            cada_video["title"] = cada_mapa["title"]
            cada_video["channel_title"] = cada_mapa["channel_title"]
            cada_video["category_id"] = cada_mapa["category_id"]
            cada_video["days"] = 1

            mp.put(lista_categ, cada_mapa["video_id"], cada_video)
        else:
             llave = mp.get(lista_categ, cada_mapa["video_id"])
             valor = me.getValue(llave)
             valor["days"] += 1
        


    return lista_categ


def mejor_categoria (catalog, lista_filtrada):
    """
    A traves de contadores se haya el video que
    tenga mas views segun su categoria 
    y se retorna el respectivo
    """
    mejor_total = {}
    mejor_parcial = 0

    valores = mp.valueSet(lista_filtrada)

    for x in range(0, lt.size(valores)):
        mapa = lt.getElement(valores, x)

        if mapa["days"] > mejor_parcial:
            mejor_parcial = mapa["days"]
            mejor_total = mapa
    
    return mejor_total





#Funciones para req 4

#4
def filtrar_pais_tag (tag, pais, catalog):
    """
    Crea una lista nueva para ordenar los datos segun sus likes.
    Y recorre la lista dada, para guardar en la nueva lista 
    solo los videos que correspondan con el pais dado,
    y que tengan en sus id's el id dado.
    Antes de leer los tag, se dividen por "|" para poderlos leer bien
    """
    nueva_lista = lt.newList("ARRAY_LIST", cmpfunction = cmpVideosByLikes)

    for x in lt.iterator(catalog['videos']):
        if str(x['country'].strip()) == pais:
            lista_tags = (x['tags'].split("|"))
            for y in lista_tags:
                if tag in str(y):
                    lt.addLast(nueva_lista, x)

    return nueva_lista
