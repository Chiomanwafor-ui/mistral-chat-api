import requests

url = "http://127.0.0.1:5000/api/chat"
payload = {
    "messages": [
        {"role": "user", "content": "List the major cities in belgium"} 
    ]
}

response = requests.post(url, json=payload)
reply = response.json()
print(reply["choices"][0]["message"]["content"])
