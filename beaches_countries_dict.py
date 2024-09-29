beaches_countries = {
    "Bondi Beach" : "Australia",
    "Waikiki Beach" : "Hawaii",
    "Boracay" : "Philippines",
    "Copacabana Beach" : "Brazil",
    "Maya Beach" : "Thailand",
    "Playa del Carmen" : "Mexico",
    "Bora Bora" : "French Polynesia",
    "Navagio Beach" : "Greece"
}
print(beaches_countries)

print("The country of the third beach is:", beaches_countries["Boracay"])

beaches_countries["Playa del Carmen"] = "Spain"
print(beaches_countries)

del beaches_countries["Maya Beach"]
print(beaches_countries)

last_key = list(beaches_countries.keys())[-1]
last_value = beaches_countries[last_key]
print("The last key-value pair is", last_key, ":", last_value)