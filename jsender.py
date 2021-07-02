import requests
import json
import time
import config


def send(text):
    data = {
        "text": text,
        }
    answer = requests.post(config.url, data=json.dumps(data), headers=config.headers)
    print(answer)


def ssend(text):
    data = {
        "text": text,
        }
    answer = requests.get(config.url, data=json.dumps(data), headers=config.headers)
    print(answer)


send("https://www.youtube.com/watch?v=RNhtJBuZ8i8")
time.sleep(10)
send("https://www.youtube.com/watch?v=aoqmOG4EiJQ")
time.sleep(10)
ssend('iQaDvb')
time.sleep(10)
ssend('2zR_f-')
time.sleep(10)
ssend('koZ3B_')
time.sleep(10)
send("https://www.youtube.com/watch?v=F7cwo0tRWWw")
time.sleep(10)
ssend('1B2M2Y')
