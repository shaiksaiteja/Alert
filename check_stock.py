from playwright.sync_api import sync_playwright
import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://www.sheinindia.in/s/footwear-207316"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="networkidle", timeout=60000)

    text = page.locator("body").inner_text()

    browser.close()

msg = f"SHEIN TEST\n\n{text[:500]}"

requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": msg[:4000]
    }
)
