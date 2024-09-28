coffee_types = {
   "Espresso" : "A strong, concentrated coffee brewed by forcing hot water through finely-ground coffee beans",
    "Americano" : "Made by diluting an espresso shot with hot water, giving it a similar strength to drip coffee but with a different flavor profile",
    "Latte" : "Consists of one-third espresso and two-thirds steamed milk, topped with a small amount of milk foam. It’s creamy and smooth",
    "Cappuccino" : "Similar to a latte but with equal parts espresso, steamed milk, and milk foam. It has a stronger coffee flavor and a frothy top",
    "Macchiato" : "An espresso “stained” with a small amount of steamed milk or milk foam. It’s stronger than a latte or cappuccino",
    "Mocha" : "A chocolate-flavored variant of a latte, made with espresso, steamed milk, and chocolate syrup, often topped with whipped cream",
    "Flat White" : "It’s made with a shot of espresso and microfoam (steamed milk with small, fine bubbles), resulting in a velvety texture",
    "Affogato" : "A dessert coffee where a shot of hot espresso is poured over a scoop of vanilla ice cream or gelato",
    "Cold Brew" : "Coffee grounds steeped in cold water for an extended period (usually 12-24 hours), resulting in a smooth, less acidic coffee",
    "Frappuccino" : "A blended iced coffee drink, often flavored with syrups and topped with whipped cream. Popularized by Starbucks"
}

print(coffee_types)

print("The description of the 4th type of coffee is:", coffee_types ["Cappuccino"])

coffee_types["Affogato"] = "A strong, concentrated coffee brewed by forcing hot water through finely-ground coffee beans"
print(coffee_types)

del coffee_types["Macchiato"]
print(coffee_types)

last_key = list(coffee_types.keys())[-1]
last_value = coffee_types[last_key]
print("The last key-value pair is", last_key, ":", last_value)