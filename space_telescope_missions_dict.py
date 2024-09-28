space_telescope_missions = {
     "Hubble Space Telescope" : "To observe the universe in visible, ultraviolet, and near-infrared light",
     "James Webb Space Telescope" : "To study every phase in the history of our universe, from the Big Bang to the formation of solar systems capable of supporting life",
     "Chandra X-ray Observatory" : "To observe X-rays from high-energy regions of the universe, such as the remnants of exploded stars",
     "Fermi Gamma-ray Space Telescope" : "To study gamma-ray sources, including pulsars, black holes, and gamma-ray burst",
     "Spitzer Space Telescope" : " To observe the universe in infrared light, revealing objects that are too cool or obscured by dust to be seen in visible light"
}

print(space_telescope_missions)

print("The mission of the third telescope is:", space_telescope_missions["Chandra X-ray Observatory"])

space_telescope_missions["Hubble Space Telescope"] = " To observe the universe in infrared light, revealing objects that are too cool or obscured by dust to be seen in visible light"
print(space_telescope_missions)

del space_telescope_missions["Fermi Gamma-ray Space Telescope"]
print(space_telescope_missions)

last_key = list(space_telescope_missions.keys())[-1]
last_value = space_telescope_missions[last_key]
print("The last key-value pair is", last_key, ":", last_value)
