import json

json_data = '{"name": "Ivan", "age": 30, "is_student": true}'

parsed_data = json.loads(json_data)

print(parsed_data, type(parsed_data))
