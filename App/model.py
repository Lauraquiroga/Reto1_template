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
    catalog = {'peliculas_prom':None, 'votos_totales':None, 'directores':None, 'actores': None, 'genres': None}
    catalog['genres'] = lt.newList('ARRAY_LIST')
    catalog['directores'] = lt.newList('ARRAY_LIST')
    catalog['actores'] = lt.newList('ARRAY_LIST')
    catalog['peliculas_prom']=lt.newList('ARRAY_LIST') #lista de peliculas ordenandas por vote_average
    catalog['votos_totales']=lt.newList('ARRAY_LIST') #lista de peliculas ordenadas por vote_count
    return catalog

#cargar películas
def newMovie (title, vote_average, vote_count, id):
    movie= {'title':' ', 'vote_average':' ', 'vote_count':' ', 'release_date':' ', 'id':' '}
    movie['title']=title
    movie['vote_average']=vote_average
    movie['vote_count']=vote_count
    movie['release_date']=release_date
    movie['id']=id
    return movie

def addMovie (catalog, row):
    m = newMovie (row['title'], row['vote_average'], row['vote_count'], row['release_date'], row['id'])
    lt.addLast (catalog['peliculas_prom'], m)
    lt.addLast (catalog['votos_totales'], m)

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

def newActor (name, movies, average_vote, director_mas):
    """
    Crea una nueva estructura para almacenar los actores de una pelicula 
    """
    actor = {'name':' ', 'movies':lt.newList(), 'average':" ", 'director_mas':" "}
    
    actor["name"]=name
    actor["movies"]=movies
    actor["average"]=average_vote
    actor['director_mas']=director_mas
    return actor

def updateActor(actor, movie, average_vote, director_mas)
    pass

def addActor (catalog, actor):
    """
    Adiciona un actor a la lista de actores
    """
    pass

def newDirector (name, movies, average_vote):
    """
    Esta estructura almancena los directores de una pelicula.
    """
    director = {'name':" ", 'movies':lt.newList(), 'average':" "}
    director["name"]=name
    director["movies"]=movies
    director["average"]=average_vote
    return director

def updateDirector (director, movie, average_vote):
    """
    Actualiza al director dado si ya está en la lista de directores
    """
    lt.addLast (director['movies'], movie)
    size= lt.size(director['movies'])
    n= (size-1)/size
    m= average_vote/size
    director['average']= (director['average']*n)+m

def addDirector (catalog, row):
    """
    Adiciona un director a la lista de directores
    """
    name=row["director_name"]
    id=row['id']
    size = lt.size(catalog['directores'])
    if size:
        iterator = it.newIterator(catalog['directores'])
        while  it.hasNext(iterator):
            director = it.next(iterator)
            movie=
            average_vote=
            if name == director["name"]:
                updateDirector(director, movie, average_vote)
            else:
                d = newDirector (name, movie, average_vote)
                lt.addLast (catalog['directors'], d)
                
    else:
        movie=
        average_vote=
        d = newDirector (row['director_name'], movie, average_vote)
        lt.addLast (catalog['directors'], d)



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

def getBestMovies (catalog, number, criteria):
    if criteria=="average":           
        movies = catalog['peliculas_prom']
    else:
        movies = catalog['votos_totales']

    bestmovies = lt.newList()

    iterator = it.newIterator(movies)
    while  it.hasNext(iterator) and lt.size(bestmovies)<=number:
        movie = it.next(iterator)
        lt.addLast(bestmovies, movie)
        

    
    
    return bestmovies

def getWorstMovies (catalog, number, criteria):
    if criteria=="average":           
        movies = catalog['peliculas_prom']
    else:
        movies = catalog['votos_totales']

    worstmovies = lt.newList()
    
    return worstmovies

def getPositiveVotes (peliculas):
    positivos = 0
    for movie in peliculas:
        if movie["vote_average"]>=6:
            positivos+=1
    return positivos