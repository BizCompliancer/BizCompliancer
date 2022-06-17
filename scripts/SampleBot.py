import requests


base_url = "https://api.telegram.org/bot5485160927:AAF6miryPYATiiGAMb_1XWwGWFk31InpK80"

def read_message(offset):

    parameters = {"offset": offset}

    response = requests.get(base_url + "/getUpdates", data = parameters)

    data = response.json()

    for result in data["result"]:
        if "hi" in result["message"]["text"]:
            send_message()

    if data["result"]:
        return data["result"][-1]["update_id"] + 1


def send_message():

    parameters = {"chat_id": "-1001625142889", "text": "Hello from Biz_Compliancer"}

    response = requests.get(base_url + "/sendMessage", data = parameters)
    print(response.text)


offset = 0
while True:
    offset = read_message(offset)