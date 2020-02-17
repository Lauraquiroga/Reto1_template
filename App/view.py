"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller 
import csv
from ADT import list as lt
from DataStructures import listiterator as it

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Reto 1")
    print("1- Cargar información del reto")
    print("2- Peliculas con mejores votaciones")
    print("3- Películas con peores votaciones")
    print("4- Películas más populares (mayor cantidad de votos)")
    print("5- Películas menos populares (menor cantidad de votos)")
    print("6- Número de votos positivos por director: ")
    print("7- Peliculas por director")
    print("8- Películas por actor")
    print("9- Películas por género")
    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo de peliculas
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga las peliculas en la estructura de datos
    """
    controller.loadData(catalog)



def printBestMovies (movies):
    size = lt.size(movies)
    if size:
        print (' Estas son las mejores peliculas: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Titulo: ' + movie['title'] + '  Fecha: ' + movie['release_date'] + ' Rating: ' + movie['vote_average'])
    else:
        print ('No se encontraron peliculas')

def printWorstMovies (movies):
    size = lt.size(movies)
    if size:
        print (' Estas son las mejores peliculas: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Titulo: ' + movie['title'] + '  Fecha: ' + movie['release_date'] + ' Rating: ' + movie['vote_average'])
    else:
        print ('No se encontraron peliculas')

def printMostVoted (movies):
    size = lt.size(movies)
    if size:
        print (' Estas son las peliculas con mayor número de votos: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Titulo: ' + movie['title'] + '  Fecha: ' + movie['release_date'] + ' Vote count: ' + movie['vote_count'])
    else:
        print ('No se encontraron peliculas')

def printLessVoted (movies):
    size = lt.size(movies)
    if size:
        print (' Estas son las peliculas menor npumero de votos: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Titulo: ' + movie['title'] + '  Fecha: ' + movie['release_date'] + ' Vote count: ' + movie['vote_count'])
    else:
        print ('No se encontraron peliculas')

"""
Menu principal
"""
while True:
    printMenu()
    inputs =input('Seleccione una opción para continuar\n')
    if int(inputs[0])==1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog ()
        loadData (catalog)
        print ('Peliculas cargadas: ' + str(lt.size(catalog['movies'])))
        print ('Directores cargados: ' + str(lt.size(catalog['directors'])))


    elif int(inputs[0])==2:
        number = input ("Buscando las TOP ?: ") #Requerimiento 2
        criteria="average"
        movies = controller.getBestMovies (catalog, int(number), criteria)
        printBestMovies (movies)

    elif int(inputs[0])==3:
        number = input ("Buscando las TOP ?: ") #requerimiento 2
        criteria="average"
        movies = controller.getWorstMovies (catalog, int(number), criteria)
        printWorstMovies (movies)

    elif int(inputs[0])==4: #Requerimento 2
        number =int(input("Buscando las Top ?: "))
        criteria= "count"
        movies=controller.getBestMovies(catalog, int(number), criteria)
        printMostVoted (movies)

    elif int(inputs[0])==5: #Requerimiento 2
        number =int(input("Buscando las Top ?: "))
        criteria="count"
        movies=controller.getWorstMovies(catalog, int(number), criteria)
        printLessVoted(movies)

    elif int(inputs[0])==6: #Requerimento 1
        director = input("Ingrese el nombre del director")
        positivos = controller.getPositiveVotes(catalog, director)
        print (positivos)

    elif int(inputs[0])==7: #Requerimento 3
        name = input("Nombre del director a buscar: ")
        movies = controller.getMoviesByDirector (catalog, name)
        print(movies)


    elif int(inputs[0])==8:#Requerimiento 4
        name = input ("Nombre del Actor a buscar: ")
        criteria = 2 #criterio para buscar actor
        movies = controller.getMoviesByCriteria (catalog, name, criteria)
        print(movies)

    elif int(inputs[0])==9:#Requerimiento 5
        name = input ("Nombre del Género a buscar: ")
        criteria = 3 #criterio para buscar género
        movies = controller.getMoviesByCriteria (catalog, name, criteria)
        print(movies)

    else:
        sys.exit(0)
sys.exit(0)