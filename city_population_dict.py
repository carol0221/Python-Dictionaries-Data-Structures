city_population = {
      "Tokyo, Japan" : "37,194,105",
      "Shanghai, China" : "40,800,000",
      "Jakarta, Indonesia" : "10,915,364",
      "Mexico City, Mexico" : "25,100,000",
      "Seoul, South Korea" : "25,100,100",
      "New York City, U.S." : "22,000,000",
      "Bangkok, Thailand" : "21,200,000",
      "Moscow, Russia" : "19,100,000",
      "Buenos Aires, Argentina" : "16,700,000",
      "Manila, Philippines" :"1,600,000"
}

print(city_population)

print("Population of the 6th city is:", city_population["New York City, U.S."])

city_population["Jakarta, Indonesia"] = 11,248,839
print(city_population)

del city_population["Buenos Aires, Argentina"]
print(city_population)

last_key = list(city_population.keys())[-1]
last_value = city_population[last_key]
print("The last key-value is", last_key, ":", last_value)

