festival_dates = {
      "Diwali": "November 12",
      "Eid al-Fitr": "April 21",
      "Hanukkah": "December 18",
      "Halloween": "October 31",
      "Thanksgiving": "November 24",
      "Chinese New Year": "February 10",
      "Cinco de Mayo" : "May 5",
      "Songkran" : "April 13",
      "All Saints' Day" : "November 1",
      "Valentine's Day" : "February 14"
}

print(festival_dates)

print("The date of the third festival is:", festival_dates["Hanukkah"])

festival_dates["Cinco de Mayo"] = "April 5"
print(festival_dates)

del festival_dates["Chinese New Year"]
print(festival_dates)

last_key = list(festival_dates.keys())[-1]
last_value = festival_dates[last_key]
print("The last key-value pair is", last_key, ":", last_value)