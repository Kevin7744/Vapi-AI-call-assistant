import requests

url = "https://api.vapi.ai/call"

headers = {"Authorization": "Bearer bee"}

response = requests.request("GET", url, headers=headers)

print(response.text)