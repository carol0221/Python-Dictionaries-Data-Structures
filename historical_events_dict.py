hitorical_events = {
      "Signing of the Magna Carta" : 1215,
      "Start of World War I" : 1914,
      "Moon Landing by Apollo 11" : 1969,
      "Arrival of Ferdinand Magellan" : 1521,
      "First Philippine Republic" : 1899,
      "End of World War II" : 1945,
      "La Liga Filipina" : 1892,
      "Beatles Atteck in the Philippines" : 1966
}

print(hitorical_events)

print("The year of the second event is:", hitorical_events["Start of World War I"])

hitorical_events["La Liga Filipina"] = "1876"
print(hitorical_events)

del hitorical_events["First Philippine Republic"]
print(hitorical_events)

last_key = list(hitorical_events.keys())[-1]
last_value = hitorical_events[last_key]
print("The last key-value pair is", last_key, ":", last_value)