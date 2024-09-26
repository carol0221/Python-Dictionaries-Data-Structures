movie_directors = {
    "Parasite" : "Bong Joon Ho",
    "Jurassic Park" : "Steven Spielberg",
    "Inception" : "Christopher Nolan",
    "Kill Bill" : "Quentin Tarantino",
    "Taxi Driver" : "Martin Scorsese", 
    "Titanic" : "James Cameron", 
    "The Shining" : "Stanley",
    "The Godfather" : "Francis Ford Coppola", 
    "Pacific Rim" : "Guillermo del Toro",
    "Psycho" : "Alfred Hitchcock"
}

print(movie_directors)

print("The director of the 5th movie is:", movie_directors["Taxi Driver"])

movie_directors["Pacific Rim"] = "Ida Lupino"
print(movie_directors)

del movie_directors["The Shining"]
print(movie_directors)

last_key = list(movie_directors.keys())[-1]
last_value = movie_directors[last_key]
print("The last key-value is", last_key, ":", last_value)