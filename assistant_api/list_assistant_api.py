import requests

url = "https://api.vapi.ai/assistant"

headers = {"Authorization": "Bearer bee"}

response = requests.request("GET", url, headers=headers)

print(response.text)