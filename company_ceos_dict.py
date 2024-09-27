companies_ceos = {
    "Netflix": "Ted Sarandos",
    "Microsoft": "Satya Nadella",
    "Amazon": "Andy Jassy",
    "Tesla": "Elon Musk",
    "Meta": "Mark Zuckerberg",
    "Alphabet": "Sundar Pichai",
    "IBM": "Arvind Krishna",
    "Oracle": "Safra Catz",
    "Disney": "Bob Iger",
    "Apple": "Tim Cook"
}

print(companies_ceos)

print("The ceo of the 6th company is:", companies_ceos["Alphabet"])

companies_ceos["Amazon"] = "Stanley"
print(companies_ceos)

del companies_ceos["Disney"]
print(companies_ceos)

last_key = list(companies_ceos.keys())[-1]
last_value = companies_ceos[last_key]
print("The last key-value pair is", last_key, ":", last_value)