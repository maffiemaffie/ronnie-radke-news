import requests
import os
import html
import random
from dotenv import load_dotenv
load_dotenv()

WEBHOOK_URL = os.environ["WEBHOOK_URL"]
BRAVE_TOKEN = os.environ["BRAVE_TOKEN"]

def get_random_ronnie_radke_news():
    response = requests.get(
        "https://api.search.brave.com/res/v1/news/search",
        headers={
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "x-subscription-token": BRAVE_TOKEN
        },
        params={
            "q": "\"ronnie radke\"",
            "count": "10",
            "safesearch": "off",
            "freshness": "pw",
            "result_filter": "news"
        },
    ).json()

    index = random.randint(0, len(response["results"]) - 1)
    result = response["results"][index]
    title = result["title"]
    description = result["description"]
    description = html.unescape(description)
    description = description.replace("<strong>", "**").replace("</strong>", "**")
    description = description.replace("<em>", "*").replace("</strong>", "*")
    thumbnail = result["thumbnail"]["src"]
    url = result["url"]
    age = result["page_age"]
    return title, description, url, age, thumbnail

def get_ronnie_radke_news():
    response = requests.get(
        "https://api.search.brave.com/res/v1/news/search",
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

    result = response["results"][0]
    title = result["title"]
    description = result["description"]
    description = html.unescape(description)
    description = description.replace("<strong>", "**").replace("</strong>", "**")
    description = description.replace("<em>", "*").replace("</strong>", "*")
    thumbnail = result["thumbnail"]["src"]
    url = result["url"]
    age = result["page_age"]
    return title, description, url, age, thumbnail

def send_ronnie_radke_news(title, description, url, age, thumbnail):
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
                "timestamp": age,
                "thumbnail": {
                    "url": thumbnail,
                },
            }]
        }
    )

if __name__ == "__main__":
    random_mode = os.environ.get("RANDOM", "false").lower() == "true"
    if (random_mode):
        news = get_random_ronnie_radke_news()
    else:
        news = get_ronnie_radke_news()
    send_ronnie_radke_news(*news)
