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
def newMovie (title, vote_average, vote_count, release_date, id):
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
    
def dir_mas_act (lista_directores):
    director_mas=0
    for director in lista_directores.values():
        if director>director_mas:
            director_mas=director
    return director_mas

#creación de las ramas del catálogo

def newActor (name, movies, average_vote, directores, director_mas):
    """
    Crea una nueva estructura para almacenar los actores de una pelicula 
    """
    actor = {'name':' ', 'movies':lt.newList(), 'average':" ",'directores':{}, 'director_mas':" "}
    actor["name"]=name
    lt.addLast(actor["movies"], movies)
    actor["average"]=average_vote
    actor['directores'][directores]=1
    actor['director_mas']=director_mas
    return actor

def updateActor(actor, movie, average_vote, director):
    lt.addLast (actor['movies'], movie)
    size= lt.size(actor['movies'])
    n= (size-1)/size
    m= float(average_vote)/size
    actor['average']= (float(actor['average'])*n)+m
    if director in actor['directores']:
        actor['directores'][director]+=1
    else:
        actor['directores'][director]=1

    actor['director_mas']=dir_mas_act(actor['directores'])

def addActor (catalog, row):
    """
    Adiciona un actor a la lista de actores
    """
    name1=row["actor1_name"]
    name2=row['actor2_name']
    name3=row['actor3_name']
    name4=row['actor4_name']
    name5=row['actor5_name']
    id_m=row['id']
    director=row['director_name']
    movie= None
    average_vote= None

    peliculas= catalog['peliculas_prom']
    size = lt.size(peliculas)
    iterator = it.newIterator(peliculas)
    while  it.hasNext(iterator) and movie==None:
        pelicula = it.next(iterator)
        if pelicula['id']==id_m:
            movie=pelicula['title']
            average_vote=pelicula['vote_average']

    repetido1=0
    repetido2=0
    repetido3=0
    repetido4=0
    repetido5=0
    size = lt.size(catalog['actores'])
    
    if size:
        iterator = it.newIterator(catalog['actores'])
        while  it.hasNext(iterator):
            actor = it.next(iterator)
        
            if name1 == actor["name"]:
                repetido1=1
                updateActor(actor, movie, average_vote, director)
            elif name2 == actor["name"]:
                repetido2=1
                updateActor(actor, movie, average_vote, director)
            elif name3 == actor["name"]:
                repetido3=1
                updateActor(actor, movie, average_vote, director)
            elif name4 == actor["name"]:
                repetido4=1
                updateActor(actor, movie, average_vote, director)
            elif name5 == actor["name"]:
                repetido5=1
                updateActor(actor, movie, average_vote, director)
        
    if repetido1==0 and name1!=None:
        director_mas=director
        a1 = newActor (name1, movie, average_vote, director, director_mas)
        lt.addLast (catalog['actores'], a1)
    if repetido2==0 and name2!=None:
        director_mas=director
        a2 = newActor (name2, movie, average_vote, director, director_mas)
        lt.addLast (catalog['actores'], a2)
    if repetido3==0 and name3!=None:
        director_mas=director
        a3 = newActor (name3, movie, average_vote, director, director_mas)
        lt.addLast (catalog['actores'], a3)
    if repetido4==0 and name4!=None:
        director_mas=director
        a4 = newActor (name4, movie, average_vote, director, director_mas)
        lt.addLast (catalog['actores'], a4)
    if repetido5==0 and name5!=None:
        director_mas=director
        a5 = newActor (name5, movie, average_vote, director, director_mas)
        lt.addLast (catalog['actores'], a5)
    

def newDirector (name, movies, average_vote, positives):
    """
    Esta estructura almancena los directores de una pelicula.
    """
    director = {'name':" ", 'movies':lt.newList(), 'average':" ", 'positives':' '}
    director["name"]=name
    lt.addLast(director["movies"], movies)
    director["average"]=average_vote
    director['positives']=positives
    return director

def updateDirector (director, movie, average_vote):
    """
    Actualiza al director dado si ya está en la lista de directores
    """
    lt.addLast (director['movies'], movie)
    size= lt.size(director['movies'])
    n= (size-1)/size
    m= float(average_vote)/size
    director['average']= (float(director['average'])*n)+m
    if float(average_vote)>=6:
        director['positives']+=1

def addDirector (catalog, row):
    """
    Adiciona un director a la lista de directores
    """
    name=row["director_name"]
    id_m=row['id']
    movie= None
    average_vote= None

    peliculas= catalog['peliculas_prom']
    size = lt.size(peliculas)
    iterator = it.newIterator(peliculas)
    #encuentra el nombre de la pelicula en la lista de películas a partir de su id
    while  it.hasNext(iterator) and movie==None:
        pelicula = it.next(iterator)
        if pelicula['id']==id_m:
            movie=pelicula['title']
            average_vote=pelicula['vote_average']
    #adiciona un director nuevo si no está en la lista de directores o lo actualiza si a está
    size = lt.size(catalog['directores'])
    repetido= 0
    if size:
        iterator = it.newIterator(catalog['directores'])
        while  it.hasNext(iterator):
            director = it.next(iterator)
        
            if name == director["name"]:
                updateDirector(director, movie, average_vote)
                repetido=1
                
    if not(size) or repetido==0:
        if float(average_vote)>=6:
            positives=1
        else:
            positives=0
        d = newDirector (name, movie, average_vote, positives)
        lt.addLast (catalog['directores'], d)



def newGenre (genre, movies, average_vote):
    """
    Esta estructura almancena los géneros con sus películas y promedio de votos
    """
    genero = {'genre':' ', 'movies':lt.newList(), 'average':' '}
    genero['genre']=genre
    lt.addLast(genero['movies'], movies)
    genero['average']=average_vote
    return genero

def updateGenre (genre, movie, average_vote):
    """
    Actualiza al genero dado si ya está en la lista de géneros
    """
    lt.addLast (genre['movies'], movie)
    size= lt.size(genre['movies'])
    n= (size-1)/size
    m= float(average_vote)/size
    genre['average']= (float(genre['average'])*n)+m

def addGenre(catalog, row):
    """
    Adiciona un género a la lista de géneros
    """
    name=row['genres']
    movie= row['title']
    average_vote= row['vote_average']
    repetido=0
    size = lt.size(catalog['genres'])
    if size:
        iterator = it.newIterator(catalog['genres'])
        while  it.hasNext(iterator):
            genre = it.next(iterator)

            if name == genre['genre']:
                repetido=1
                updateGenre(genre, movie, average_vote)
            
                
    if not(size) or repetido==0:
        g = newGenre (name, movie, average_vote)
        lt.addLast (catalog['genres'], g)
    


# Funciones de consulta

def getMoviesByDirector (catalog, name):
    movies=lt.newList("ARRAY_LIST")
    iterator = it.newIterator(catalog["directores"])
    while  it.hasNext(iterator):
        element = it.next(iterator)
        if name in element["name"]:
            size= lt.size(element['movies'])
            director={'director':element['name'],"películas":element['movies'], 'cantidad':size, "prom":element['average']}
            lt.addLast(movies,director)
    return movies

def getPositivesByDirector (catalog, name):
    positives=lt.newList("ARRAY_LIST")
    iterator = it.newIterator(catalog["directores"])
    while  it.hasNext(iterator):
        element = it.next(iterator)
        if name in element["name"]:
            director={'director':element['name'],"positive_votes":element['positives']}
            lt.addLast(positives,director)
    return positives

def getBestMovies (catalog, number, criteria):
    if criteria=="average":           
        movies = catalog['peliculas_prom']
    else:
        movies = catalog['votos_totales']

    pos= 1
    bestmovies = lt.subList(movies, pos, number)
    return bestmovies

def getWorstMovies (catalog, number, criteria):
    if criteria=="average":           
        movies = catalog['peliculas_prom']
    else:
        movies = catalog['votos_totales']
    size=lt.size(movies)
    pos=size-number
    worstmovies = lt.subList(movies, pos, number)
    return worstmovies

def getMoviesByActor (catalog, name):
    movies=lt.newList("ARRAY_LIST")
    iterator = it.newIterator(catalog["actores"])
    while  it.hasNext(iterator):
        element = it.next(iterator)
        if name in element["name"]:
            size= lt.size(element['movies'])
            actor={'actor':element['name'],"películas":element['movies'], 'cantidad':size, "promedio":element['average'], 'director':element['director_mas']}
            lt.addLast(movies,actor)
    return movies

def getMoviesByGenre (catalog, name):
    movies=lt.newList("ARRAY_LIST")
    iterator = it.newIterator(catalog["genres"])
    while  it.hasNext(iterator):
        element = it.next(iterator)
        if name in element["genre"]:
            size= lt.size(element['movies'])
            genre={'genero':element['genre'],'cantidad':size, "prom":element['average']}
            lt.addLast(movies,genre)
    return movies
