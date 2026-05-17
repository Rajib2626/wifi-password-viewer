import requests

user = "torvalds"

url = f"https://api.github.com/users/{"Rajib2626"}"

r = requests.get(url)

data = r.json()

print("Name:", data["name"])
print("Bio:", data["bio"])
print("Followers:", data["followers"])
print("Public repos:", data["public_repos"])
