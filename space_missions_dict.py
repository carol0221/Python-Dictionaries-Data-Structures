space_missions = {
    "Apollo 11": 1969,
    "Voyager 1": 1977,
    "Mars Rover Curiosity": 2012,
    "SpaceX Falcon Heavy": 2018,
    "Perseverance Rover": 2020
}

print(space_missions)

print("The year of the third mission is:", space_missions["Mars Rover Curiosity"])

space_missions["Voyager 1"] = "1979"
print(space_missions)

del space_missions["SpaceX Falcon Heavy"]
print(space_missions)

last_key = list(space_missions.keys())[-1]
last_value = space_missions[last_key]
print("The last key-value pair is", last_key, ":", last_value)

