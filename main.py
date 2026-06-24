import requests
import json
import os
from ui import ChatWindow

with open("systemPrompt.txt", "r", encoding="utf-8") as file:
    sysPrompt = file.read()

IP = "http://localhost:11434/api/chat"
MODEL = "hermes3"
SYSTEM = [
    {
        "role" : "system",
        "content" : f"{sysPrompt}"

    }
]

history = []

def open_app(name):
    os.system(f'start "" "{name}"')


def ask_ai():
    response = requests.post(
        IP,
        json={
            "model": MODEL,
            "messages": SYSTEM + history[-50:],
            "stream": False,
            "keep_alive": "30m"
        }
    )

    msg = response.json()["message"]["content"]

    history.append({
        "role": "assistant",
        "content": msg
    })

    try:
        data = json.loads(msg)
        if data["action"] == "open_app":
            app = data["app"]

            open_app(app)
            return f"Opening {app}"
    except json.JSONDecodeError:
        return msg
        





while True:
    user = input("User: ")

    history.append({
        "role": "user",
        "content": user
    })

    if user.lower() == "/bye":
        break
    elif user.lower() == "/clearhis":
        history.clear()
    else:
        print(ask_ai())
