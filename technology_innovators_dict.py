technology_innovators = {
      "Personal Computers" : "Steve Jobs and Steve Wozniak",
      "Smarthphone" : "Martin Cooper",
      "Electric Light Bulb" : "Thomas Edison",
      "Internet" : "Tim Berners-Lee",
      "CRISPR-Cas9" : "Jennifer Doudna and Emmanuelle Charpentier",
      "Blockchain" : "Satoshi Nakamoto",
      "Artificial Intelligence(AI)" : "John McCarthy",
      "Electric Car" : "Elon Musk"
}

print(technology_innovators)

print("The innovator of the 4th technology is:", technology_innovators["Internet"])

technology_innovators["Smartphone"] = "Alexander Graham Bell"
print(technology_innovators)

del technology_innovators["Artificial Intelligence(AI)"]
print(technology_innovators)

last_key = list(technology_innovators.keys())[-1]
last_value = technology_innovators[last_key]
print("The last key-value pair is", last_key, ":", last_value)