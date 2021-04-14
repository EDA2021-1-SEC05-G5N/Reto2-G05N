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
 """

import time
import tracemalloc
import config as cf
import model
import csv
from datetime import datetime


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en kBytes (ej.: 2100.0 kB)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0
    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory



# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la función de inicialización del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog



# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y carga los datos en la
    estructura de datos
    """
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadVideos(catalog)
    loadCategories(catalog)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory



def loadVideos(catalog):
    """
    Carga los videos del archivo.  Por cada video se toman los datos necesarios:
    video id, trending date, category id, views, nombre del canal, país, nombre del 
    video, likes, dislikes, fecha de publicación, likes y tags.
    """
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
  
    for video in input_file:
        cada_video = {}
        datos_str = ["title",
                     "video_id",
                     "category_id",
                     "channel_title",
                     "country",
                     "publish_time"]
        datos_numeros = ["likes",
                         "dislikes",
                         "views" ]

        for dato in datos_str:
            cada_video[dato] = video[dato]

        for dato_num in datos_numeros:
            cada_video[dato_num] = video[dato_num]
        cada_video["trending_date"] = datetime.strptime(video['trending_date'], '%y.%d.%m').date()
        
        model.addVideo(catalog, cada_video)

        model.addCountry(catalog, cada_video)



def loadCategories (catalog):
    """
    Carga las categorías del archivo. Por cada categoría su guarda su id y su nombre.
    """
    categoriesfile = cf.data_dir + 'category-id.csv'

    input_file = csv.DictReader(open(categoriesfile, encoding='utf-8'), delimiter="\t")
    for category in input_file:
        categories = {'id': int(category['id']),
                      'name': category['name']}
        model.addCategory(catalog, category)








# FUNCIONES RETO 2



# Funciones de ordenamiento

#1
def sortVideosByViews(lista_filtros, cantidad):
    """
    Ordena los videos por views.
    """
    return model.sortVideosByViews(lista_filtros, cantidad)

#2
def sortVideosByID(filtro_pais):
    """
    Ordena los videos por id.
    """
    return model.sortVideosByID(filtro_pais)

#3
def sortVideosByID_date(filtro_categoria):
    """
    Ordena los videos por dos criterios: en primer lugar por su id y segundo por su trending_date. 
    """
    return model.sortVideosByID_date(filtro_categoria)

#4
def sortVideosByLikes (lista_filtros):
    """
    Ordena los videos por likes.
    """
    return model.sortVideosByLikes(lista_filtros)





# Funciones de consulta sobre el catálogo


#1
def filtrar_pais_categoria (id_categoria, catalog):
    """
    Retorna una lista que cumple con los requerimientos de país y categoría.
    """
    return model.filtrar_pais_categoria(id_categoria, catalog)

#2
def filtrar_pais (pais, catalog):
    """
    Retorna una lista que cumple con el requerimiento de país.
    """
    return model.filtrar_pais(pais, catalog)

#2
def getTendencia2 (sorted_list):
    """
    Retorna el video con más días en tendencia.
    """
    return model.getTendencia2(sorted_list)

#3
def filtrar_categoria (id_categoria, catalog):
    """
    Retorna una lista que cumple con el requerimiento de categoría.
    """
    return model.filtrar_categoria(id_categoria, catalog)

#3
def getTendencia3 (sorted_list):
    """
    Retorna el video con más días en tendencia. En este caso, tiene en cuenta que 
    no se cuente doble como tendencia el mismo día en países distintos. 
    """
    return model.getTendencia3(sorted_list)

#4
def filtrar_pais_tag (tag, pais, catalog):
    """
    Retorna una lista que cumple con los requerimientos de país y tag. 
    """
    return model.filtrar_pais_tag(tag, pais, catalog)
    
#4
def acortar_lista (sorted_list, cantidad):
    """
    Retorna una lista que cumple con el requerimiento de la cantidad de videos. 
    """
    return model.acortar_lista(sorted_list, cantidad)








#Funciones:

#1
def requerimiento_1(catalog, categoria, cantidad, pais):

    id_categoria = model.get_id_categoria(catalog, categoria)
    #buscartag = model.getVideosbytag(catalog, id_categoria)
    lista_filtros = model.filtrar_pais_categoria(id_categoria, catalog, pais)
    #sorted_list = sortVideosByLikes(lista_filtros)

    return lista_filtros

#1
def requerimiento_2(catalog, pais):

    filtro_pais = model.filtrar_pais(catalog, pais)
    mejor_pais = model.mejor_pais(catalog, filtro_pais)

    return filtro_pais









