# ASSIGNMENT
# 3 settings.py — save a dictionary to JSON and load it back

import json

settings = {
    "username": "Sumit",
    "theme": "dark",
    "notifications": True,
    "language": "English",
    "font_size": 14
}

with open("settings.json" , "w") as file:
    json.dump(settings , file ,indent=4)

with open("settings.json" , "r") as file:

    data = json.load(file)

print(data)