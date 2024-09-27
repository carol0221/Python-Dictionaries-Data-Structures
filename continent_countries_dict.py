continent_countries = {
        "Asia" : "Korea, Japan, Singapore",
        "Africa" : "Angola, Cameroon, Algeria",
        "Europe" : "Austria, Belgium, Denmark",
        "North America" : "Costa Rica, Cuba, El Salvador",
        "Oceania" : "Australia, New Zealand, Solomon Islands",
        "South America" : "Argentina, Ecuador, Peru"
}

print(continent_countries)

print("The countries of the 4th continent is:", continent_countries["North America"])

continent_countries["Oceania"] = "Palau, Fiji, Marshall Islands"
print(continent_countries)

del continent_countries["South America"]
print(continent_countries)

last_key = list(continent_countries.keys())[-1]
last_value = continent_countries[last_key]
print("The last key-value pair is", last_key, ":", last_value)