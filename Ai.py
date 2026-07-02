import requests
import json
import os

with open("systemPrompt.txt", "r", encoding="utf-8") as file:
    sysPrompt = file.read()


def open_app(name):
    os.system(f'start "" "{name}"')



class AiAssistant():
    def __init__(self):
        super().__init__()
        self.ip = "http://localhost:11434/api/chat"
        self.model = "hermes3"
        self.system = [
            {
                "role" : "system",
                "content" : f"{sysPrompt}"

            }
        ]

        self.history = []
    

    def ask_ai(self, Usermsg):

        self.history.append({
            "role": "user",
            "content": Usermsg
        })

        response = requests.post(
            self.ip,
            json={
                "model": self.model,
                "messages": self.system + self.history[-50:],
                "stream": False,
                "keep_alive": "30m"
            }
        )

        msg = response.json()["message"]["content"]

        self.history.append({
            "role": "assistant",
            "content": msg
        })

        try:
            data = json.loads(msg)
            if data["action"] == "open_app":
                app = data["app"]

                open_app(app)
                return  f"Opening {app}"
        except json.JSONDecodeError:
            return msg
    






# while True:
#     user = input("User: ")
#     assistant = AiAssistant()
#     print(assistant.ask_ai(user))
