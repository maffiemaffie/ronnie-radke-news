from flask import Flask
import requests
import os
import html
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
WEBHOOK_URL = os.environ["WEBHOOK_URL"]
BRAVE_TOKEN = os.environ["BRAVE_TOKEN"]

def get_ronnie_radke_news():
    response = requests.get(
        "https://api.search.brave.com/res/v1/web/search",
        headers={
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "x-subscription-token": BRAVE_TOKEN
        },
        params={
            "q": "ronnie radke news",
            "count": "1",
            "safesearch": "off",
            "freshness": "pd",
            "result_filter": "news"
        },
    ).json()

    result = response["news"]["results"][0]
    title = result["title"]
    description = result["description"]
    description = html.unescape(description)
    description = description.replace("<strong>", "**").replace("</strong>", "**")
    description = description.replace("<em>", "*").replace("</strong>", "*")
    url = result["url"]
    age = result["page_age"]
    return title, description, url, age

def send_ronnie_radke_news(title, description, url, age):
    requests.post(
        WEBHOOK_URL,
        json={
            "content": "<@&1375298173685338164>",
            "embeds": [{
                "title": title,
                "description": description,
                "url": url,
                "color": 16711680,
                "footer": {"text": "Ronnie Radke Updates"},
                "timestamp": age
            }]
        }
    )

@app.route("/trigger", methods=["GET"])
def trigger_news():
    title, desc, url, age = get_ronnie_radke_news()
    send_ronnie_radke_news(title, desc, url, age)
    return "Sent!", 200
  
@app.route("/", methods=["GET"])
def ping():
    return "Pong!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5050)))
