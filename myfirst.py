import requests
import json
r = requests.get('https://github.com/timeline.json')
r.json()
print r.json

