import json
import yaml
import sys
input = open('text.txt', 'r').read().split('&&')
counter = 0
for item in input:
    file = open("yaml/"+str(counter)+".yaml",'w')
    file.write(str(json.dumps(yaml.safe_load(item))))
    file.close()
    counter += 1
