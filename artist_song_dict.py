artist_songs = {
    "Taylor Swift" : "Love Story",
    "Ariana Grande" : "Thank U, Next",
    "Do Kyungsoo" : "Popcorn",
    "Baekhyun" : "Pineapple Slice",
    "Dua Lipa" : "New Rules",
    "Bruno Mars" : "That's What I Like",
    "Brian McKnight" : "6,8,12",
    "Beyonce" : "Irreplaceable"
}

print(artist_songs)

print("The top song of the third artist is:", artist_songs["Do Kyungsoo"])

artist_songs["Bruno Mars"] = "24K Magic"
print(artist_songs)

del artist_songs["Brian McKnight"]
print(artist_songs)

last_key = list(artist_songs.keys())[-1]
last_value = artist_songs[last_key]
print("The last key-value pair is", last_key, ":", last_value)
