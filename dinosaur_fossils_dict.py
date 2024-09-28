dinosaur_fossils = {
      "Tyrannosaurus rex" : "North America",
      "Triceratops" : "North America",
      "Brachiosaurus" : "Colorado, USA",
      "Stegosaurus" : "Western United States",
      "Velociraptor" : "Gobi Desert of Mongolia",
      "Spinosaurus" : "Kem Kem Beds of Morocco",
      "Patagotitan mayorum" : "Patagonia, Argentina"
}

print(dinosaur_fossils)

print("The location of the 4th dinosaur's fossils is:", dinosaur_fossils["Stegosaurus"])

dinosaur_fossils["Triceratops"]
print(dinosaur_fossils)

del dinosaur_fossils["Spinosaurus"]
print(dinosaur_fossils)

last_key = list(dinosaur_fossils.keys())[-1]
last_value = dinosaur_fossils[last_key]
print("The last key-value pair is", last_key, ":", last_value)
