import requests

username = input("Enter username: ")

url = f"https://api.github.com/users/{username}"

data = requests.get(url).json()

print("Followers:", data["followers"])
print("Repos:", data["public_repos"])