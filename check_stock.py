import requests
import os

URL = "https://www.sheinindia.in/s/footwear-207316?query=%3Anewn%3Arelevance%3Aundefined%3Aundefined%3Anull&curated=true&curatedid=footwear-207316&customerType=Existing&gridColumns=5&sort=prce-desc&segmentIds=&customertype=Existing"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

r = requests.get(URL, timeout=30)

count = r.text.count("goods_id")

try:
    with open("last_count.txt", "r") as f:
        old_count = int(f.read())
except:
    old_count = 0

if count > old_count:
    msg = f"🚨 SHEIN Alert!\nProducts increased from {old_count} to {count}"

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

with open("last_count.txt", "w") as f:
    f.write(str(count))
