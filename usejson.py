import json

json_string = '{"fName":"Brian","lName":"Katchmar","Age":30}'
decoded_json = json.loads(json_string)
print(decoded_json["fName"])
print(decoded_json["lName"])
print(decoded_json["Age"])