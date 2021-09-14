import requests
import json

request = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
# print(request.json()['items'])
for item in request.json()['items']:
    if item['is_answered'] == False:
        print(item)

    else:
        print('answered')
print("--------------")
