software_companies = {
        "Microsoft": "Redmond, Washington, USA",
	"Google (Alphabet Inc.)": "Mountain View", 
	"Intuit": "Mountain View, California, USA",
	"Genesys" : "Daly City, California",
        "Twilio" : "San Francisco, California",
	"Apple": "Cupertino, California, USA",
	"Zoho" : "Chennai, India",
	"IBM": "Armonk, New York, USA",
	"Salesforce": "San Francisco, California, USA",
        "Miro" : "San Francisco, California"
}
print(software_companies)

print("The headquarters of the 3rd company is:", software_companies["Intuit"])

software_companies["IBM"] = "Walldorf, Germany"
print(software_companies)

del software_companies["Salesforce"]
print(software_companies)

last_key = list(software_companies.keys())[-1]
last_value = software_companies[last_key]
print("The last key-value is", last_key, ":", last_value)

