import json
import requests

LINK = 'https://www.bicing.cat/availability_map/getJsonObject'

r = requests.get(LINK)
obj = r.json()
print "obj: ", obj

print json.dumps(sorted(obj, key=lambda entry: int(entry['slots'])), indent=2)

