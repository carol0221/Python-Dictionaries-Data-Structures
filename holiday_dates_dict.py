holiday_dates = {
       "Independence Day": "July 4",
       "Thanksgiving": "November 24",
       "New Year's Day": "January 1",
       "Easter": "April 17",  
       "Valentine's Day": "February 14",
       "Christmas": "December 25",
       "April Fool's Day" : "April 1",
       "Labor Day" : "May 1",
       "Earth Day" : "April 22",
       "Mother's Day": "May 8"
}

print(holiday_dates)

print("The date of the 4th holiday is:", holiday_dates["Easter"])

holiday_dates["Earth Day"] = "April 1"
print(holiday_dates)

del holiday_dates["Thanksgiving"]
print(holiday_dates)

last_key = list(holiday_dates.keys())[-1]
last_value = holiday_dates[last_key]
print("The last key-value pair is", last_key, ":", last_value)