rivers_length = {
      "Nile River" : "6,650 km",
      "Amazon River" : "6,600 km",
      "Yangtze River" : "6,300 km",
      "Mississippi River" : "6,270 km",
      "Yellow River" : "5,464 km",
      "Rio De La Plata" : "4,880 km"
}

print(rivers_length)

print("The length of the second river is:", rivers_length["Amazon River"])

rivers_length["Yellow River"] = "4,500 km"
print(rivers_length)

del rivers_length["Mississippi River"]
print(rivers_length)

last_key = list(rivers_length.keys())[-1]
last_value = rivers_length[last_key]
print("The last key-value pair is", last_key, ":", last_value)