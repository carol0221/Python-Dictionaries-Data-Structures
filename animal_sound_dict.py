animal_sound = {
      "Cat" : "Meow",
      "Elephant" : "Trumpet",
      "Rabbit" : "Hrrr",
      "Tiger" : "Growl", 
      "Bee" : "Buzz", 
      "Pig" : "Oink",
      "Dog" : "Arf",
      "Sheep" : "Baaah"
}

print(animal_sound)

print("Sound of the 4th animal is:", animal_sound["Tiger"])

animal_sound["Dog"] = "Woof"
print(animal_sound)

del animal_sound["Bee"]
print(animal_sound)

last_key = list(animal_sound.keys())[-1]
last_value = animal_sound[last_key]
print("The las key-value is", last_key, ":", last_value)



