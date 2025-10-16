""" File One
Simply Print the titles of all movies

File Two
After accepting user input, print all movies that released AFTER a given year.

File Three
After accepting user input, print all movies that released AFTER a given year and BEFORE a different year.

File 4
After accepting user input, print all movies that released during a given year.

File 5
Develop a function that allows users to search for a specific movie and returns all results that match

File 6
Develop a function that allows users to search for movies by genre """

import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)

#File 1
""" for i in range(len(data)):
    print(data[i]['title'])

#File 2
def releasefinder(release):
    release = int(release)
    for i in range(len(data)):
        if (data[i]['year']) > release:
            print(data[i]['title'])
releasefinder(1980)
#File 3
def rangefinder(release, cutoff):
    release = int(release)
    cutoff = int(cutoff)
    print(f"The movies released between {release} and {cutoff} are:")
    for i in range(len(data)):
        if data[i]['year'] > release and data[i]['year'] < cutoff:
            print(data[i]['title'])
rangefinder(1980, 1985)
#File 4
def movie_year_finder(year):
    year = int(year)
    print(f"The movies released in {year} are:")
    for i in range(len(data)):
        if data[i]['year'] == year:
            print(data[i]['title'])
movie_year_finder(1980)
#File 5
def movie_name_finder(name):
    movies_found = 0
    print(f"Here are the results for '{name}':")
    for i in range(len(data)):
        if data[i]['title'] == name:
            print(data[i]['title'])
            movies_found = movies_found + 1
    if movies_found == 0:
        print("No movies found of that name!")
movie_name_finder(1) """

#File 6
def movie_finder(genres):
    genres = genres.split(", ")
    print(genres)
    print(f"Here are the results for the genre(s) '{genres}':")
    for i in range(len(data)):
        for a in range(len(genres)):
            if genres[a] in data[i]["genres"]:
                print(data[i]['title'])
movie_finder("Horror, Supernatural")

lista = ["a, b, c"]
if ["a"] in lista:
    print("yes")
else:
    print("no")