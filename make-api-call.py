import requests

api_endpoint = "http://mysafeinfo.com/api/data?list=englishmonarchs&format=json"
r = requests.get(api_endpoint)
print(r.status_code)

english_rulers = r.json()

for ruler in english_rulers:
    print(ruler["nm"] + " of " + ruler["hse"])