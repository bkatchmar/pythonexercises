import json

json_string = '[{"fName":"Pepe","lName":"Katchmar","Age":30},{"fName":"Angelica","lName":"Reyes","Age":22}]'
decoded_json = json.loads(json_string)

for item in decoded_json:
    print("============")
    print(item["fName"])
    print(item["lName"])
    print(item["Age"])