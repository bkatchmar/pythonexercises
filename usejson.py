import json

json_string = '[{"fName":"Brian","lName":"Katchmar","Age":32},{"fName":"John","lName":"Smith","Age":25}]'
decoded_json = json.loads(json_string)

for item in decoded_json:
    print("============")
    print(item["fName"])
    print(item["lName"])
    print(item["Age"])