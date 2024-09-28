company_founders =  {
     "McDonald's" : "Richard and Maurice McDonald",
     "Nike" : "Bill Bowerman and Philip Knight",
     "Nokia" : "Fredrik Idestam and Leo Mechelin",
     "Alibaba" : "Jack Ma",
     "Google (Alphabet)" : "Larry Page and Sergey Brin",
     "Tesla" : "Elon Musk, JB Straubel, Martin Eberhard, Marc Tarpenning, and Ian Wright",
     "Amazon" : "Jeff Bezos",
     "Microsoft" : "Bill Gates and Paul Allen"
}

print(company_founders)

print("The founder of the 6th company is:", company_founders["Tesla"])

company_founders["Nike"] = "Ronald Wayne"
print("Ronald Wayne")

del company_founders["Microsoft"]
print(company_founders)

last_key = list(company_founders.keys())[-1]
last_value = company_founders[last_key]
print("The last key-value pair is", last_key, ":", last_value)