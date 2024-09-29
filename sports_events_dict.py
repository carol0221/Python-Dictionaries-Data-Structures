sport_events = {
    "FIFA World Cup in Qatar" : 2022,
    "Cricket World Cup in England" : 2019,
    "Paris Summer Olympics" : 2024,
    "FIFA World Cup in Brazil" : 2014,
    "London Summer Olympics" : 2012, 
    "FIFA World Cup in Russia" : 2018,
    "Rio de Janeiro Summer Olympics" : 2016
}

print(sport_events)

print("The year of the third sports event is:", sport_events["Paris Summer Olympics"])

sport_events["FIFA World Cup in Russia"] = 2017
print(sport_events)

del sport_events["London Summer Olympics"]
print(sport_events)

last_key = list(sport_events.keys())[-1]
last_value = sport_events[last_key]
print("The last key-value pair is", last_key, ":", last_value)
