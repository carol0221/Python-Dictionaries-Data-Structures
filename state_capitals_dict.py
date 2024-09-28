state_capitals = {
    "Alaska" : "Juneau",
    "Arizona" : "Phoenix",
    "California" : "Sacramento",
    "Colorado" : "Denver",
    "Florida" : "Tallahassee",
    "Hawai" : "Honolulu",
    "Georgia" : "Atlanta",
    "Arkansas" : "Little Rock",
    "Connecticut" : "Hartford",
    "Delaware" : "Dover"
}

print(state_capitals)

print("The capital of the 4th state is:", state_capitals["Colorado"])

state_capitals["Connecticut"] = "Boise"
print(state_capitals)

del state_capitals["Georgia"]
print(state_capitals)

last_key = list(state_capitals.keys())[-1]
last_value = state_capitals[last_key]
print("The last key-value pair is", last_key, ":", last_value)