# client.py

import requests
import json

url = 'http://www.google.com'

response = requests.get(url)

print(str(response))
print('')
print(json.dumps(response.json(), indent=4))