import requests

api_endpoint = "https://rickandmortyapi.com/api/character"
response = requests.get(api_endpoint).json()

paging_info = response["info"]
characters = response["results"]

# print(paging_info)
# print(characters)

for ruler in characters:
    print("%s - %s %s" % (ruler["name"], ruler["species"], ruler["gender"]))