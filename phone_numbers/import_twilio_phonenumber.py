import requests

url = "https://api.vapi.ai/phone-number/import"

payload = {
    "assistantId": "<string>",
    "name": "<string>",
    "twilioAccountSid": "<string>",
    "twilioAuthToken": "<string>",
    "twilioPhoneNumber": "<string>"
}
headers = {
    "Authorization": "Bearer bee",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)