country_capital = {
      "Philippines" : "Manila",
      "Argentina" : "Buenos Aires", 
      "India" : "New Delhi", 
      "France" : "Paris", 
      "Austria" : "Vienna",
      "Germany" : "Berlin", 
      "Italy" : "Rome",
      "Monaco" : "Monaco",
      "Spain" : "Madrid",
      "Belgium" : "Brussels",
      "Vatican City" : "Vatican City", 
      "Russia" : "Moscow"

}
 
print(country_capital)
       
print("The capital of the 5th country is:", country_capital["Austria"])

country_capital["Spain"] = "Barcelona"
print(country_capital)

del country_capital["Vatican City"]
print(country_capital)

last_key =list(country_capital.keys())[-1]
last_value = country_capital[last_key]
print("The last key-value is", last_key, ":", last_value)
