job_salaries = {
   "Doctor/Surgeon" : "166,000",
   "Judge" : "139,000",
   "Lawyer" : "113,000",
   "Bank Manager" : "106,000",
   "Mathematicians and actuaries" : "69,654",
   "Accountant" : "48,892",
   "Geologists" : "49,059",
   "Statisticians" : "51,607",
   "Chief Financial Officer" : "101,000",
   "Specialist" : "57,476"
}

print(job_salaries)

print("The salary of the third job is:", job_salaries["Lawyer"])

job_salaries["Geologists"] = "53,600"
print(job_salaries)

del job_salaries["Chief Financial Officer"]
print(job_salaries)

last_key = list(job_salaries.keys())[-1]
last_value = job_salaries[last_key]
print("The last key-value pair is", last_key, ":", last_value)
