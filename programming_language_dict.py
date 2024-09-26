programming_language = {
      "JavaScript" : "Brendan Eich",
      "C++" : "Bjarne Stroustrup",
      "C#" : "Anders Hejlsberg",
      "Java" : "James Gosling",
      "PHP" : "Rasmus Lerdorf",
      "Scheme" : " Gerald Jay Sussman",
      "Python" : "Guido van Rossum"
      

}

print(programming_language)

print("The developer of the 4th programming language is:", programming_language["Java"])

programming_language["Scheme"] = "Guy Lewis Steele Jr"
print(programming_language)

del programming_language["C++"]
print(programming_language)

last_key = list(programming_language.keys())[-1]
last_value = programming_language[last_key]
print("The last key-value is", last_key, ":", last_value)