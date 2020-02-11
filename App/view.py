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
    print("3- Peliculas por Director")
    print("4- Requerimiento 2 ... etc")
    print("5- Cargar peores películas")
    print("6- Número de votos positivos por director: ")
    print("7- 10 películas con mayor votos totales y promedio, X peliculas con menos votos totales y promedio:  ")
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
            print ('Titulo: ' + movie['original_title'] + '  Fecha: ' + movie['release_date'] + ' Rating: ' + movie['vote_average'])
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
        number = input ("Buscando las TOP ?: ")
        movies = controller.getBestMovies (catalog, int(number))
        printBestMovies (movies)

    elif int(inputs[0])==3: #Requerimento 3
        name = input("Nombre del director a buscar: ")
        movies = controller.getMoviesByCriteria (catalog, name, name_catalog, criterio)
        numero=size(movies)
        prom_votos=controller.getVotosProm()
        print(movies)


    elif int(inputs[0])==4:
        label = input ("Nombre del Actor a buscar: ")
        pass

    elif int(inputs[0])==5:
        number = input ("Buscando las TOP ?: ")
        movies = controller.getWorstMovies (catalog, int(number))
        print (movies)

    elif int(input[0])==6: #Requerimento 1
        director = input("Ingrese el nombre del director")
        peliculas = controller.getMoviesByDirector (catalog, director)
        positivos = controller.getPositiveVotes (peliculas)
        print (positivos)
    elif int(input[0])==7: #Requerimento 2
        X=int(input("Ingrese un número X que define el número de elementos que se retornan: "))
        mayor_votos_prom=controller.getXVotosProm(10, >)
        mayor_votos_tot=controller.getVotosTot(10, >)
        menor_xvotos_prom=controller.getXVotosProm(X, <)
        menor_xvotos_tot=controller.getXVotosTot(X, <)
    else:
        sys.exit(0)
sys.exit(0)