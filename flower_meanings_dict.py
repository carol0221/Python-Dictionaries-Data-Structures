flowers_meaning = {
      "Red Rose" : "Love",
      "Yellow Hyancinth" : "Jealousy",
      "White Lily" : "Purity",
      "Alstroemeria" : "Devotion",
      "Aster" : "Patience",
      "Yellow Carnation" : "Rejection",
      "Daisy" : "Innocence",
      "Purple Crocus" : "Pride"
}

print(flowers_meaning)

print("The meaning of the 5th flower is:", flowers_meaning["Aster"])

flowers_meaning["Daisy"] = "Purity"
print(flowers_meaning)

del flowers_meaning["Yellow Carnation"]
print(flowers_meaning)

last_key = list(flowers_meaning.keys())[-1]
last_value = flowers_meaning[last_key]
print("The last key-value pair is", last_key, ":", last_value)