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
    print(data[i]['title']) """

#File 2
""" release = input("Input a year.")
release = int(release)
for i in range(len(data)):
    if (data[i]['year']) > release:
        print(data[i]['title']) """

#File 3
""" release = input("Input a year.")
cutoff = input("Input another year, larger than the first one.")
release = int(release)
cutoff = int(cutoff)
print(f"The movies released between {release} and {cutoff} are:")
for i in range(len(data)):
    if data[i]['year'] > release and data[i]['year'] < cutoff:
        print(data[i]['title']) """

#File 4
""" year = input("Input a year.")
year = int(year)
print(f"The movies released in {year} are:")
for i in range(len(data)):
    if data[i]['year'] == year:
        print(data[i]['title']) """

#File 5
""" movies_found = 0
name = input("Search a movie.")
print(f"Here are the results for '{name}':")
for i in range(len(data)):
    if data[i]['title'] == name:
        print(data[i]['title'])
        movies_found = movies_found + 1
if movies_found == 0:
    print("No movies found of that name!") """

#File 6
