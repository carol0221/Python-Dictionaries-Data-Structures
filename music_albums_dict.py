music_albums = {
    "Hello, World" : "September 6, 2024",
    "Blossom" : "May,2024",
    "GUTS" : "September 8, 2023",
    "The Record" : "March 31, 2023",
    "SOS" : "December 9, 2022",
    "Midnight" : "October 21, 2022",
    "Renaissance" : "July 29, 2022",
    "Black Out" : "August 28,2024",
    "Dawn FM" : "January 7, 2022",
    "Harry's House" : "May 20, 2022"
}

print(music_albums)

print("The release year of the third album is:", music_albums["GUTS"])

music_albums["Black Out"] = "February 21,2024"
print(music_albums)

del music_albums["Midnight"]
print(music_albums)

last_key = list(music_albums.keys())[-1]
last_value = music_albums[last_key]
print("The last key-value pair is", last_key, ":", last_value)