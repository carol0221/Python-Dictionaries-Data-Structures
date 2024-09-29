food_recipes = {
    "Chicken Adobo" : "Marinate chicken in soy sauce and garlic. Brown chicken, then add marinade, vinegar, bay leaves, peppercorns, and sugar. Simmer until chicken is  tender",
    "Beef Tacos" : "Cook ground beef with taco seasoning. Serve in tortillas with lettuce, tomatoes, cheese, and sour cream",
    "Vegetable Stir-Fry" : "Stir-fry vegetables in sesame oil with garlic and ginger. Add soy saucr and cook until vegetables are tender",
    "Shrimp Scampi" : "Cook spaghetti. Saute garlic in butter, add shrimp and cook until pink. Add lemon juice and white wine, simmer. Toss with spaghetti and parsley",
    "Pancakes" : "Mix dry ingredients. Whisk milk, egg, and melted butter. Combine with dry ingredients. Cook on a griddle until golden brown",
    "Caesar Salad" : "Toss lettuce with Ceasar dressing, croutons, and parmesan. Drizzle with lemon juice",
    "Chocolate Chip Cookies" : "Cream butter and sugars. Add eggs and vanilla. Mix in dry ingredients, then chocolate chips. Bake at 350°F (175°C) until golden",
    "Chicken Curry" : "Sauté onions, garlic, and ginger. Add chicken and cook until browned. Add tomatoes and curry powder, cook until fragrant. Stir in coconut milk and simmer until chicken is cooked through. Garnish with cilantro"
}

print(food_recipes)

print("The recipe of the 5th food is:", food_recipes["Pancakes"])

food_recipes["Vegetable Stir-Fry"] = "Heat the vegetable oil over medium-high heat. Add the broccoli, bell peppers, snaps peas, carrots, mushrooms, and baby corn. Stir-fry for about 5 minutes until vegetables are tender"
print(food_recipes)

del food_recipes["Chocolate Chip Cookies"]
print(food_recipes)

last_key = list(food_recipes.keys())[-1]
last_value = food_recipes[last_key]
print("The last key-value pair is", last_key, ":", last_value)