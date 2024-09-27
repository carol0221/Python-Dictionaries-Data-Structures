athlete_achievements = {
     "Michael Jordan": "6 NBA Championships",
     "Michael Phelps" : "Most Olympic Gold Medals",
     "Serena Williams" : "Grand Slam Titles",
     "Roger Federer" : "20 Grand Slam Titles",
     "LeBron James" : "NBA Championships",
     "Usain Bolt" : "8 Olympic Gold Medals",
     "Tom Brady" : "Super Bowl Championships",
     "Simone Biles" : "World Championship Medals"
}

print(athlete_achievements)

print("The achivements of the thirf athlete is:", athlete_achievements["LeBron James"])

athlete_achievements["Serena Williams"] = "Gymnastic World Championship"
print(athlete_achievements)

del athlete_achievements["Tom Brady"]
print(athlete_achievements)

last_key = list(athlete_achievements.keys())[-1]
last_value = athlete_achievements[last_key]
print("The last key-value pair is", last_key, ":", last_value)