car_brands = {
      "BMW" : "Germany",
      "Roll Royce" : "United Kingdom",
      "Toyota" : "Japan",
      "Mercedes-Benz" : "Germany",
      "Volvo" : "Sweden",
      "Lamborghini" : "Italy",
      "Ford" : "America", 
      "Innoson" : "Nigeria",
      "Aston Martin" : "United Kingdom",
      "Hyundai" : "South Korea"
}

print(car_brands)

print("The country origin of the third car brand is:", car_brands["Toyota"])

car_brands["Ford"] = "China"
print(car_brands)

del car_brands["Innoson"]
print(car_brands)

last_key = list(car_brands.keys())[-1]
last_value = car_brands[last_key]
print("The last key-value is", last_key, ":", last_value)