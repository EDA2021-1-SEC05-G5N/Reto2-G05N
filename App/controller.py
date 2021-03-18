﻿"""
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

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

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
    loadVideos(catalog)
    loadCategories(catalog)


def loadVideos(catalog):
    """
    Carga los libros del archivo.  Por cada video se toman los datos necesarios:
    video id, trending date, category id, views, nombre del canal, país, nombre del 
    video, likes, dislikes, fecha de publicación, likes y tags.
    """

    videosfile = cf.data_dir + 'videos-small.csv'
    
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        cada_video = {'video_id': video['video_id'],
                  #'trending_date': datetime.strptime(video['trending_date'], '%y.%d.%m').date(),
                  'category_id': int(video['category_id']),
                  'views': int(video['views']),
                  'channel_title': video['channel_title'],
                  'country': video['country'],
                  'title': video['title'],
                  'likes': video['likes'],
                  'dislikes': video['dislikes'],
                  'publish_time': video['publish_time'],
                  'tags': video['tags']}
                  
        model.addVideo(catalog, cada_video)


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



# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo











# FUNCIONES RETO 1



# Funciones de ordenamiento

#1
def sortVideosByViews(lista_filtros, cantidad):
    """
    Ordena los videos por views.
    """
    return model.sortVideos(lista_filtros, cantidad)

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
def get_id_categoria (categoria, catalog):
    """
    Retorna el id de la categoría solicitada.
    """
    return model.get_id_categoria(categoria, catalog)

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





#Funciones con el orden de las ejecuciones de cada requerimiento:

#1
def requerimiento_1(categoria, cantidad, catalog):

    id_categoria = get_id_categoria(categoria, catalog)
    lista_filtros = filtrar_pais_categoria(id_categoria, catalog)
    sorted_list = sortVideosByLikes(lista_filtros)

    return sorted_list






def cargar(catalog, categoria):
    return model.get_id_categoria(catalog, categoria)