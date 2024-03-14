import requests

url = "https://api.vapi.ai/assistant/{id}"

payload = {
    "backgroundSound": "office",
    "clientMessages": ["transcript", "hang", "function-call", "speech-update", "metadata", "conversation-update"],
    "dialKeypadFunctionEnabled": True,
    "endCallFunctionEnabled": True,
    "endCallMessage": "<string>",
    "endCallPhrases": ["<string>"],
    "firstMessage": "<string>",
    "forwardingPhoneNumber": "null",
    "forwardingPhoneNumbers": [
        {
            "message": "<string>",
            "number": "<string>",
            "sipUri": "<string>"
        }
    ],
    "hipaaEnabled": True,
    "llmRequestDelaySeconds": 0.1,
    "maxDurationSeconds": 1800,
    "metadata": {},
    "model": {
        "fallbackModels": ["gpt-4-0125-preview", "gpt-4-0613"],
        "functions": [
            {
                "async": True,
                "description": "<string>",
                "name": "<string>",
                "parameters": {
                    "properties": {},
                    "required": ["<string>"],
                    "type": "object"
                }
            }
        ],
        "maxTokens": 525,
        "messages": [
            {
                "content": "<string>",
                "function_call": {},
                "role": "assistant",
                "tool_calls": [{}]
            }
        ],
        "model": "gpt-4-1106-preview",
        "provider": "openai",
        "semanticCachingEnabled": True,
        "temperature": 1
    },
    "name": "<string>",
    "numWordsToInterruptAssistant": 2,
    "recordingEnabled": True,
    "responseDelaySeconds": 0.4,
    "serverMessages": ["end-of-call-report", "status-update", "hang", "function-call"],
    "serverUrl": "<string>",
    "serverUrlSecret": "<string>",
    "silenceTimeoutSeconds": 30,
    "transcriber": {
        "keywords": ["<string>"],
        "language": "cs",
        "model": "nova-2",
        "provider": "deepgram"
    },
    "voice": {
        "provider": "azure",
        "voiceId": "andrew"
    },
    "voicemailDetectionEnabled": True,
    "voicemailMessage": "<string>"
}
headers = {
    "Authorization": "Bearer bee",
    "Content-Type": "application/json"
}

response = requests.request("PATCH", url, json=payload, headers=headers)

print(response.text)