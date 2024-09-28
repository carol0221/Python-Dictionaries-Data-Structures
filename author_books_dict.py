author_books = {
    "Jane Austen" : "Pride and Prejudice",
    "Ernest Hemingway" : "The Old Man And The Sea",
    "Herman Melville" : "Moby Dick",
    "Toni Morison" : "Beloved",
    "Aldous Huxley" : "Brave New World",
    "Umberto Eco" : "The Name Of The Rose",
    "Thomas Stearns Eliot" : "The Waste Land",
    "Jean-Paul Sartre" : "Being And Nothingness"
}

print(author_books)

print("The book of the 5th author is:", author_books["Aldous Huxley"])

author_books["Thomas Stearns Eliot"] = "Things Fall Apart"
print(author_books)

del author_books["Umberto Eco"]
print(author_books)

last_key = list(author_books.keys())[-1]
last_value = author_books[last_key]
print("The last key-value pair is", last_key, ":", last_value)