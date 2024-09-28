phone_models = {
     "iPhone 13" : "Apple",
     "Galaxy S21" : "Samsung",
     "Xperia 1 III" : "Sony",
     "Xiaomi Mi 11'" : "Xiaomi",
     "Sony Xperia 5" : "Sony",
     "Nokia G50" : "Nokia",
     "Galaxy Z Fold 4" : "Samsung",
     "Moto G Power" : "Motorola",
     "LG Velvet" : "LG",
     "Mi 11": "Xiaomi"
}

print(phone_models)

print("The manufacturer of the second phone model is:", phone_models["Galaxy S21"])

phone_models["Moto G Power"] = "Google"
print(phone_models)

del phone_models["Nokia G50"]
print(phone_models)

last_key = list(phone_models.keys())[-1]
last_value = phone_models[last_key]
print("The last key-value pair is", last_key, ":", last_value)

