import requests
import os

URL = "https://www.sheinindia.in/s/footwear-207316?query=%3Anewn%3Arelevance%3Aundefined%3Aundefined%3Anull&curated=true&curatedid=footwear-207316&customerType=Existing&gridColumns=5&sort=prce-desc&segmentIds=&customertype=Existing"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

response = requests.get(URL, timeout=30)

count = response.text.count("goods_id")

msg = f"🔍 SHEIN Test\nCurrent Count: {count}"

requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": msg
    }
)

print(msg)
