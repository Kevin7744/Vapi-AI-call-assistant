import requests

url = "https://api.vapi.ai/assistant/{id}"

headers = {"Authorization": "Bearer bee"}

response = requests.request("DELETE", url, headers=headers)

print(response.text)