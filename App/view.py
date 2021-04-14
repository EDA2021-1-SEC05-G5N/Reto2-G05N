﻿"""
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



def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\nBienvenido!\n")
    print("0- Cargar información en el catálogo")
    print("1- Mejores videos por categoria y pais       - Req 1")
    print("2- Mejor video por pais                      - Req 2")
    print("3- Mejor video por categoria                 - Req 3")
    print("4- Videos con mas likes por categoria y pais - Req 4")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)

        print('Videos cargados: ' + str(lt.size(catalog['videos'])))

        print('\nId y categorías: ')
        for c in lt.iterator(catalog['category']):
            print(c['id'],c["name"])
        
        # Calcular tiempo
        answer = controller.loadData(catalog)
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
               "Memoria [kB]: ", f"{answer[1]:.3f}")
        

    elif int(inputs[0]) == 1:
        categoria = input('Ingrese la categoría: ')
        pais = input('Ingrese el pais: ')
        cantidad = int(input('Ingrese el número de videos: '))

        resultado = controller.requerimiento_1(catalog, categoria, cantidad, pais)
        print(resultado)
    
    elif int(inputs[0]) == 2:
        pais = input('Ingrese el pais: ')

        resultado = controller.requerimiento_2(catalog, pais)
        print(resultado)

    else:
        sys.exit(0)
sys.exit(0)







# FUNCIONES RETO 2



# Funciones para imprimir los datos en la consola

def printBestVideos(videos):
    size = lt.size(videos)
    if size:
        print(' Estos son los mejores videos: ')
        for video in lt.iterator(videos):
            print('Titulo: ' + video['title'] + '  views: ' +
                  video['views'] + ' Likes: ' + video['likes'])
    else:
        print('No se encontraron videos')

def printInfoPrimerVideo(catalog):
    print('\nInfo del primer video:\n',
        "Título del video: ",(lt.firstElement(catalog['videos']))['title'], 
        "\nTítulo del canal del video: ",(lt.firstElement(catalog['videos']))['channel_title'], 
        "\nFecha de tendencia del video: ",str((lt.firstElement(catalog['videos']))['trending_date']),
        "\nPaís del video: ",(lt.firstElement(catalog['videos']))['country'],
        "\nViews del video: ",(lt.firstElement(catalog['videos']))['views'],
        "\nLikes del video: ",(lt.firstElement(catalog['videos']))['likes'],
        "\nDislikes del video: ",(lt.firstElement(catalog['videos']))['dislikes'])

def printVideosMasViews(datos):
    lista = datos["elements"]
    for v in lista:
        print("\nFecha de tendencia: ",v['trending_date'])
        print("Nombre del video: ", v['title'])
        print("Nombre del canal: ", v['channel_title'])
        print("Fecha de publicación: ", v['publish_time'])
        print("Reproducciones: ", v['views'])
        print("Likes: ", v['likes'])
        print("Dislikes: ", v['dislikes'])

def printTendenciaPais(datos):
    print("\nNombre del video: ", datos[0]['title'])
    print("Nombre del canal: ", datos[0]['channel_title'])
    print("Pais: ", datos[0]['country'])
    print("Número de días como tendencia: ", datos[1])

def printTendenciaCategoria(datos):
    print("\nNombre del video: ", datos[0]['title'])
    print("Nombre del canal: ", datos[0]['channel_title'])
    print("Categoria: ", datos[0]['category_id'])
    print("Número de días como tendencia: ", datos[1])

def printVideosMasLikes(datos):
    lista = datos["elements"]
    for v in lista:
        print("\nNombre del video: ", v['title'])
        print("Nombre del canal: ", v['channel_title'])
        print("Fecha de publicación : ", v['publish_time'])
        print("Reproducciones: ", v['views'])
        print("Likes: ", v['likes'])
        print("Dislikes: ", v['dislikes'])
        print("Tags: ", v['tags'])

