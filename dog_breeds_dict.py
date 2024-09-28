dog_breeds = {
     "Chihuahua" : "Small",
     "Beagle" : "Medium",
     "Pomeranian" : "Small",
     "Bulldog" : "Medium",
     "Golden Retriever" : "Large",
     "Great Dane" : "Large",
     "Yorkshire Terrier" : "Small",
     "German Shepherd" : "Large",
     "Labrador Retriever" : "Large",
     "Cocker Spaniel" : "Medium"
}

print(dog_breeds)

print("The size of the 5th breed is:", dog_breeds["Golden Retriever"])

dog_breeds["German Shepherd"] = "Small"
print(dog_breeds)

del dog_breeds["Great Dane"]
print(dog_breeds)

last_key = list(dog_breeds.keys())[-1]
last_value = dog_breeds[last_key]
print("The last key-value pair is", last_key, ":", last_value)