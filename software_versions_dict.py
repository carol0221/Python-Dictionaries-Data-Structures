software_versions = {
      "Windows" : "11.0",
      "macOS" : "13.5",
      "Apache OpenOffice" : "4.1.15",
      "Python" : "3.11.4",
      "Adobe Photoshop" : "2024.1.0",
      "Malwarebytes" : "5.1.10.127"

}

print(software_versions)

print("The version of the 4th software is:", software_versions["Python"])

software_versions["macOS"] = 11.4
print(software_versions)

del software_versions["Adobe Photoshop"]
print(software_versions)

last_key = list(software_versions.keys())[-1]
last_value = software_versions[last_key]
print("The last key-value pair is", last_key, ":", last_value)