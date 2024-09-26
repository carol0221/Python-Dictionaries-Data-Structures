fruit_colors = {
     "Banana" : "Yellow",
     "Strawberry" : "Red",
     "Grapes" : "Green",
     "Apple" : "Red", 
     "Mango" : "Yellow",
     "Peach" : "Orange", 
     "Cherry" : "Red",
     "Plum" : "Purple"
}

print(fruit_colors)

print("The color of the 6th fruit is:", fruit_colors["Peach"])

fruit_colors["Apple"] = "Green"
print(fruit_colors)

del fruit_colors["Cherry"]
print(fruit_colors)

last_key = list(fruit_colors.keys())[-1]
last_value = fruit_colors[last_key]
print("The last key-value pair is", last_key, ":", last_value)