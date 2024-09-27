planet_distances = {
     "Mars" : "1.524(227.9 million)",
     "Mercury" : "0.39(57.9 million)",
     "Venus" : "0.723(108.2)",
     "Earth" : "1(149.6 million)",
     "Jupiter" : "5.203(778.3 million)",
     "Saturn" : "9.539(1,427.0 million)",
     "Uranus" : "19.18(2,871 million)",
     "Neptune" : "30.06(4,497.1 million)"
}

print(planet_distances)

print("The distance of the third planet is:", planet_distances["Venus"])

planet_distances["Jupiter"] = "4.303(667.2 million)"
print(planet_distances)

del planet_distances["Uranus"]
print(planet_distances)

last_key = list(planet_distances.keys())[-1]
last_value = planet_distances[last_key]
print("The las key-value pair is", last_key, ":", last_value)