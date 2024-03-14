import requests

url = "https://api.vapi.ai/phone-number/buy"

payload = {
    "areaCode": "<string>",
    "assistantId": "<string>",
    "name": "<string>",
    "serverUrl": "<string>",
    "serverUrlSecret": "<string>"
}
headers = {
    "Authorization": "Bearer bee",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)