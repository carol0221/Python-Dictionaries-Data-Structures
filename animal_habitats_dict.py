animals_habitats =  {
    "Lion": "Savannah",
    "Penguin": "Antarctica",
    "Elephant": "Grasslands",
    "Polar Bear": "Arctic",
    "Kangaroo": "Australian Outback",
    "Panda": "Bamboo Forests",
    "Tiger": "Rainforest",
    "Dolphin": "Oceans"
}

print(animals_habitats)

print("The habitat of the third animal is:", animals_habitats["Elephant"])

animals_habitats["Kangaroo"] = "Grasslands"
print(animals_habitats)

del animals_habitats["Tiger"]
print(animals_habitats)

last_key = list(animals_habitats.keys())[-1]
last_value = animals_habitats[last_key]
print("The last key-value pair is", last_key, ":", last_value)