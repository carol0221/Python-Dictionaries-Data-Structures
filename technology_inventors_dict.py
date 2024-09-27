technology_inventors = {
       "Telephone" : "Alexander Graham Bell",
       "Television" :  "John Logie Baird",
       "Computer" :   "Charles Babbage",
       "iPhone" : "Steve Jobs",
       "World Wide Web" : "Tim-Berners-Lee",
       "Light Bulb" : "Thomas Edison"
}

print(technology_inventors)

print("The inventor of the 4th technology is:", technology_inventors["iPhone"])

technology_inventors["Television"] = "Ralph H. Baer"
print(technology_inventors)

del technology_inventors["Light Bulb"]
print(technology_inventors)

last_key = list(technology_inventors.keys())[-1]
last_value = technology_inventors[last_key]
print("The last key-value pair is", last_key, ":", last_value)