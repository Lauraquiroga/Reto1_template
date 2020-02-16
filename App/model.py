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
from ADT import list as lt
from DataStructures import listiterator as it


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de peliculas. Retorna el catalogo inicializado.
    """
    catalog = {'movies':None, 'directors':None, 'actors': None}
    catalog['generos'] = lt.newList('ARRAY_LIST')
    catalog['directores'] = lt.newList('ARRAY_LIST')
    catalog['actores'] = lt.newList('ARRAY_LIST')
    catalog['votos_prom']=lt.newList('ARRAY_LIST')
    catalog['votos_totales']=lt.newList('ARRAY_LIST')
    return catalog

#Funciones que se requieren para crear cada rama del catálogo

def actor_mas_dirigido_director(): ##Requerimento 4
    addLast (list, row["director_name"])
    if row["actor_name"] !=""

def ordenar_peli_votos (catalogo) :
    """
    ordena la lista de peliculas de mejor promedio a peor promedio
    """
    pass
    
def direct_mas_actor (buscado):
    """
    for actors:
        if actor['name']==buscado
        for directores:
            if actor['id]']==director['id']:
                if 
    """
    pass

#creación de las ramas del catálogo

def newActor (name, catalog):
    """
    Crea una nueva estructura para almacenar los actores de una pelicula 
    """
    actor = {'name':name, 'movies':lt.newList(), 'average':" ", 'director_mas':" "}
    lista_peliculas=peli_filtradas(name)
    vote_average=getVotosProm(lista_peliculas, catalog)
    director_mas=director_mas_actor(name, directores)
    actor['movies']=lista_peliculas
    actor['average']=vote_average
    actor['director_mas']=director_mas
    return actor

def addActor (catalog, actor):
    """
    Adiciona un actor a la lista de actores
    """
    pass

def newDirector (name, catalog):
    """
    Esta estructura almancena los directores de una pelicula.
    """
    director = {'name':name, 'movies':lt.newList(), 'average':" "}
    lista_peliculas=peli_filtradas(name)
    vote_average=getVotosProm(lista_peliculas, catalog)
    director['movies']=lista_peliculas
    director['average']=vote_average
    return director

def addDirector (catalog, director):
    """
    Adiciona un director a la lista de directores
    """
    d = newDirector (director['director_name'], catalog)
    lt.addLast (catalog['directors'], d)

def UpdateDirector ():
    """
    Actualiza al director dado si ya está en lalista de directores
    """
    pass

def newGenre (genre, catalog):
    """
    Esta estructura almancena los directores de una pelicula.
    """
    genero = {'genre':genre, 'movies':lt.newList(), 'average':" "}
    lista_peliculas=peli_filtradas(genre)
    vote_average=getVotosProm(lista_peliculas, catalog)
    genero['movies']=lista_peliculas
    genero['average']=vote_average
    return genre

def addGenre(catalog, genre):
    """
    Adiciona un género a la lista de géneros
    """
    pass


# Funciones de consulta

def getMoviesByCriteria (catalog, name, criteria):
    """
    Retorna una lista de diccionarios cuyo valor de "name" incluye el nombre que se busca
    (a partir del nombre del director, del actor o del género)
    """
    movies=lt.newList("ARRAY_LIST")

    if criteria ==1:
        rama="directores"
    elif criteria == 2:
        rama="actores"
    elif criteria == 3:
        rama="generos"
    
    iterator = it.newIterator(catalog[rama])
    while  it.hasNext(iterator):
        element = it.next(iterator)
        if name in element["name"]:
            #HASTA AQUÍ VA BIEN LA FUNCIÓN
            lt.addLast(movies,element['id'])
    return(movies)

def getBestMovies (catalog, number, criteria):              #TOCA CAMBIAR LOS FOR POR ITERATORS
    movies = catalog['movies']
    bestmovies = lt.newList()
    for cont in range (1, number+1):
        movie = lt.getElement (movies, cont)
        lt.addLast (bestmovies, movie)
    return bestmovies

def getWorstMovies (catalog, number, criteria):
    movies = catalog['movies']
    worstmovies = lt.newList()
    largo=lt.size(movies)
    for cont in range (largo-number, largo):
        movie = lt.getElement (movies, cont)
        lt.addLast (worstmovies, movie["title"])
    return worstmovies

def getPositiveVotes (peliculas):
    positivos = 0
    for movie in peliculas:
        if movie["vote_average"]>=6:
            positivos+=1
    return positivos