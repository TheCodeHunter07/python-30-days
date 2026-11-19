# ASSIGNMENT
# 1 random_joke.py — fetch and print a joke from official-joke-api.appspot.com

import requests

url = "https://v2.jokeapi.dev/joke/Any"

response = requests.get(url)

data = response.json()

print(data)
print(type(data))

print("Category:", data["category"])
print("Joke:", data["setup"])
print("Answer:", data["delivery"])