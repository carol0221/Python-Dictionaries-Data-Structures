video_game_platforms = {
    "Halo Infinite" : "Xbox Series X",
    "The Legend of Zelda:Breath of the Wild": "Nintendo Switch",
    "Persona 4 Golden" : "PlayStation Vita",
    "Final Fantasy X" : "PlayStation",
    "The Witcher 3:Wild Hunt" : "PC",
    "Fortnite" : "Multi-platform",
    "Astro Bot Rescue Mission" : "PlayStation",
    "Cyberpunk 2077" : "PC, PS4, Xbox One" 
}

print(video_game_platforms)

print("The platform of the 2nd video game is:", video_game_platforms["The Legend of Zelda:Breath of the Wild"])

video_game_platforms["Fortnite"] = "PC"
print(video_game_platforms)

del video_game_platforms["Final Fantasy X"]
print(video_game_platforms)

last_key = list(video_game_platforms.keys())[-1]
last_value = video_game_platforms[last_key]
print("The last key-value pair is", last_key, ":", last_value)



  
    