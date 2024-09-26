book_authors = {
     "Pride and Prejudice" : "Jane Austen",
     "Journey to the Centre of the Earth" : "Jules Verne",
     "And Then There Were None" : "Agatha Christie",
     "Alice's Adventure In Wonderland" : "Lewis Carroll",
     "The Metamorphosis" : "Franz Kafka",
     "Olive Twist" : "Charles Dickens", 
     "Adventure of Huckleberry Finn" : "Mark Twain",
     "The Odyssey" : "Homer",
     "Hamlet" : "William Shakespeare",
     "Invisible Man" : "Ralph Ellison",
     "The Stranger" : "Albert Camus",
     "Things Fall Apart" : "Chinua Achebe"
}

print(book_authors)

print("The author of the 9th book is:", book_authors["Hamlet"])

book_authors["The Metamorphosis"] = "Sidney Sheldon"
print(book_authors)

del book_authors["And Then There Were None"]
print(book_authors)

last_key = list(book_authors.keys())[-1]
last_value = book_authors[last_key]
print("The last key-value pair is", last_key, ":", last_value)