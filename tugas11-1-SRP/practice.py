import requests

api_key = 'ec5187c4-0d4d-4c3b-a514-d28b42f3d396'
word = 'voluminous'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

r = requests.get(url)

results = r.json()

for result in results:
    print(result)