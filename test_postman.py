import requests
import json

url = "https://petstore.swagger.io/v2/user/createWithList"

payload = json.dumps([
  {
    "id": 9,
    "username": 271,
    "firstName": "Pknmsfk",
    "lastName": "skdnfkdj",
    "email": "sdjfnkjgnwn",
    "password": "weigojvs",
    "phone": "lkjbhgewukfj",
    "userStatus": 4879
  }
])
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)