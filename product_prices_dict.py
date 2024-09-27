product_prices = {
        "Smartphone" : 800.00,
        "Camera" : 600.00,
        "Tablet" : 400.00,
        "Printer": 200.00,
        "Headphones" : 150.00,
        "Laptop" : 1200.00,
        "Smartwatch" : 250.00,
        "Monitor" : 350.00,
        "External Hard Drive" : 120.00,
        "Keyboard" : 50.00
}

print(product_prices)

print("The price of the 4th product is:", product_prices["Printer"])

product_prices["External Hard Drive"] = 500.00
print(product_prices)

del product_prices["Laptop"]
print(product_prices)

last_key = list(product_prices.keys())[-1]
last_value = product_prices[last_key]
print("The last key-value pair is", last_key, ":", last_value)

   
   
   