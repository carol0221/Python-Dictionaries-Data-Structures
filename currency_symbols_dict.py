currency_symbols = {
      "Euro" : "€",
      "Japanese Yen" : "¥",
      "Australian Dollar" : "A$",
      "British Pound" : "£",
      "Canadian Dollar" : "C$",
      "Swiss Franc" : "CHF",
      "Chinese Yuan": "¥",
      "South African Rand" : "R",
      "United States Dollar" : "$",
      "Indian Rupee" : "₹",
}
print(currency_symbols)

print("The symbol of the 5th currency is:", currency_symbols["Canadian Dollar"])

currency_symbols["United States Dollar"] = 'S'
print(currency_symbols)

del currency_symbols["Australian Dollar"]
print(currency_symbols)

last_key = list(currency_symbols.keys())[-1]
last_value = currency_symbols[last_key]
print("The last key-value pair is", last_key, ":", last_value)