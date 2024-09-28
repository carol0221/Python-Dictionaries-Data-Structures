plant_types = {
    "Rose" : "Shrub",
    "Mango" : "Tree",
    "Basil" : "Herb",
    "Pumpkin" : "Creeper",
    "Grapevine" : "Climber",
    "Sunflower" : "Herb",
    "Hibiscus" : "Shrub",
    "Oak" : "Tree"
}

print(plant_types)

print("The type of the 5th plant is:", plant_types["Grapevine"])

plant_types["Mango"] = "Climber"
print(plant_types)

del plant_types["Sunflower"]
print(plant_types)

last_key = list(plant_types.keys())[-1]
last_value = plant_types[last_key]
print("The last key-value pair is", last_key, ":", last_value)