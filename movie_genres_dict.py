movie_genres = {
     "Fantasy" : "Harry Potter",
     "Action" : "The Predator",
     "Drama" : "Falling Into Your Smile",
     "Horror" : "The Conjuring", 
     "Science Fiction" : "Megan",
     "Romance" : "Love Next Door",
     "Comedy" : "Welcome to Waikiki",
     "Musical Romance" : "Camp Rock"
}
 
print(movie_genres)

print("The example movie of the third genre is:", movie_genres["Drama"])

movie_genres["Science Fiction"] = "The Hunger Games"
print(movie_genres)

del movie_genres["Comedy"]
print(movie_genres)

last_key = list(movie_genres.keys())[-1]
last_value = movie_genres[last_key]
print("The last key-value pair is", last_key, ":", last_value)

