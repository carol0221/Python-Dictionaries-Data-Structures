app_store_ratings = {
    "Weverse" : "4.5",
    "Instagram": 4.3,
    "Facebook": 4.1,
    "TikTok": 4.4,
    "Spotify": 4.6,
    "Snapchat": 4.2,
    "YouTube": 4.7,
    "Twitter": 4.0,
    "Pinterest": 4.5,
     "Zoom": 4.4
}

print(app_store_ratings)

print("The ratings of the 6th app is:", app_store_ratings["Snapchat"])

app_store_ratings["Twitter"] = "4.7"
print(app_store_ratings)

del app_store_ratings["Pinterest"]
print(app_store_ratings)

last_key = list(app_store_ratings .keys())[-1]
last_value = app_store_ratings [last_key]
print("The last key-value is", last_key, ":", last_value)