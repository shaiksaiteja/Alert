import requests
import os

URL = "https://www.sheinindia.in/s/footwear-207316?query=%3Anewn%3Arelevance%3Aundefined%3Aundefined%3Anull&curated=true&curatedid=footwear-207316&customerType=Existing&gridColumns=5&sort=prce-desc&segmentIds=&customertype=Existing"

r = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("Status:", r.status_code)
print("Length:", len(r.text))

print(r.text[:1000])
