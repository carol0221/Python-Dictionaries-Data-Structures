festival_locations = {
      "Sinulog Festival" : "Cebu City",
      "Ati-Atihan Festival" : "Kalibu, Aklan",
      "La Tomatina" : "Valencia, Spain",
      "Songkran" : "Thailand",
      "Diwali" : "India",
      "Dinagyang Festival" : "Iloilo City",
      "Oktoberfest" : "Munich, Germany",
      "Mardi Gras" : "New Orleans, USA"
}

print(festival_locations)

print("The location of the 4th festival is:", festival_locations["Songkran"])

festival_locations["Dinagyang Festival"] = "Baguio City"
print(festival_locations)

del festival_locations["Ati-Atihan Festival"]
print(festival_locations)

last_key = list(festival_locations.keys())[-1]
last_value = festival_locations[last_key]
print("The last key-value pair is", last_key, ":", last_value)