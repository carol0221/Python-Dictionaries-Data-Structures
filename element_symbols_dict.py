element_symbols = {
     "Helium" : "He",
     "Lithium" : "Li",
     "Berylium" : "Be",
     "Neon" : "Ne", 
     "Sodium" : "Na",
     "Magnesium" : "Mg",
     "Silicon" : "Si",
     "Aluminium" : "Al", 
     "Argon" : "Ar",
     "Calcium" : "Ca"
}

print(element_symbols)

print("The symbol of the 6th element is:", element_symbols["Magnesium"])

element_symbols["Aluminium"] = 'A'
print(element_symbols)

del element_symbols["Argon"]
print(element_symbols)

last_key = list(element_symbols.keys())[-1]
last_value = element_symbols[last_key]
print("The last key-value pair is", last_key, ":", last_value)