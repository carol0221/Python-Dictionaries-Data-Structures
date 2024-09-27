sports_players = {
        "Soccer": "Lionel Messi",
        "Basketball": "Michael Jordan",
        "Tennis": "Roger Federer",
        "Cricket": "Sachin Tendulkar",
        "Golf": "Tiger Woods",
        "Boxing": "Sugar Ray Robinson",
        "Swimming": "Michael Phelps",
        "Baseball": "Babe Ruth",
        "Football" : "Johan Cruyff", 
        "Wrestling" : "John Cena"
}
print(sports_players)

print("The player of the 4th sport is:" , sports_players["Cricket"])

sports_players["Boxing"] = "Joe Louis"
print(sports_players)

del sports_players["Wrestling"]
print(sports_players)

last_key = list(sports_players.keys())[-1]
last_value = sports_players[last_key]
print("The last key-value pair is", last_key, ":", last_value)