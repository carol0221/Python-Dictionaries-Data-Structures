car_specs = {
    "Honda Civic" : "2.0L 4-cylinder",
    "Ford Mustang" : "5.0L V8",
    "Tesla Model 3" : "Electric motor",
    "BMW 3 Series" : "2.0L 4-cylinder turbo",
    "Chevrolet Camaro" : "6.2L V8",
    "Audi A4" : "2.0L 4-cylinder turbo",
    "Mercedes-Benz C-Class" : "2.0 4-cylinder turbo",
    "Mazda CX-5" : "2.5L 4-cylinder",
    "Hyundai ELantra" : "2.0L 4-cylinder",
    "Toyota Corolla" : "1.8L 4-cylinder"
}

print(car_specs)

print("The specifications of the 4th car model is:", car_specs["BMW 3 Series"])

car_specs["Hyundai Elantra"] = "Electric motor"
print(car_specs)

del car_specs["Chevrolet Camaro"]
print(car_specs)

last_key = list(car_specs.keys())[-1]
last_value = car_specs[last_key]
print("The last key-value pair is", last_key, ":", last_value)
