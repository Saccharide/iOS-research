import json
import yaml

with open("t.txt") as stream:
    yaml_data = list(yaml.load_all(stream))

json_data = json.dumps(yaml_data)
print(json_data)
"""
for item in yaml_data:
    print("-----------------")
    print(item)
"""
