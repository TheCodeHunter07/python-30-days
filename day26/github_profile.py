# STRETCH CHALLENGE
# github_profile.py — Fetch and display GitHub user's public details

import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}"

try:
    response = requests.get(url, timeout=5)

    response.raise_for_status()

    data = response.json()

    print("\n========== GITHUB PROFILE ==========")

    print("Username:", data["login"])
    print("Name:", data["name"] or "Not provided")
    print("Bio:", data["bio"] or "Not provided")
    print("Public Repositories:", data["public_repos"])
    print("Followers:", data["followers"])
    print("Following:", data["following"])
    print("Profile URL:", data["html_url"])

    print("====================================")

except requests.exceptions.Timeout:
    print("Request timed out! Please try again.")

except requests.exceptions.ConnectionError:
    print("No internet connection!")

except requests.exceptions.HTTPError:
    print("GitHub user not found!")

except requests.exceptions.RequestException as error:
    print("Something went wrong:", error)