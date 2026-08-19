import requests

def ask_llama(prompt):
    url = "http://localhost:11434/api/generate"

    response = requests.post(url, json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })

    return response.json()["response"]