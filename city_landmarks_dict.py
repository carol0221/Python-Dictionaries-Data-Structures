city_landmarks = {
     "Paris, France" : "Eiffel Tower",
     "Rome, Italy" : "Trevi Fountain",
     "Yucatan, Mexico" : "Chichen Itza",
     "Agra, India" : "Taj Mahal",
     "Cairo, Egypt" : "Pyramids Of Giza",
     "Rio De Janeiro, Brazil" : "Christ The Redeemer",
     "Athens, Greece" : "Acropolis",
     "California,USA" : "The Golden Gate Bridge"
}

print(city_landmarks)

print("The landmark of the 6th city is:", city_landmarks["Rio De Janeiro, Brazil"])

city_landmarks["Rome, Italy"] = "The Colosseum"
print(city_landmarks)

del city_landmarks["Athens, Greece"]
print(city_landmarks)

last_key = list(city_landmarks.keys())[-1]
last_value = city_landmarks[last_key]
print("The last key-value pair is", last_key, ":", last_value)