import requests
import schedule
import time

webhook_url = "https://discord.com/api/webhooks/1375297883129122816/fiL0N6IdNjkPSdJ0iavQimp5Ps4ZgtabPzuCa4bjQSMGI7r6q78ETWpC2isKeGQx3Ge1";
def get_ronnie_radke_news():
  response = requests.get(
    "https://api.search.brave.com/res/v1/web/search",
    headers={
      "Accept": "application/json",
      "Accept-Encoding": "gzip",
      "x-subscription-token": "BSA5eBuwXyxerV6pHW0l1h-nJKhlgpI"
    },
    params={
      "q": "ronnie radke news",
      "count": "1",
      "safesearch": "off",
      "freshness": "pd",
      "result_filter": "news"
    },
  ).json()

  title = response["news"]["results"][0]["title"]
  description = response["news"]["results"][0]["description"].replace("<strong>", "**").replace("</strong>", "**")
  url = response["news"]["results"][0]["url"]
  age = response["news"]["results"][0]["page_age"]
  return title, description, url, age

def send_ronnie_radke_news(title, description, url, age):
  requests.post(
    webhook_url,
    json={
      "content": "<@&1375298173685338164>",
      "embeds": [{
        "title": title,
        "description": description,
        "url": url,
        "color": 16711680,
        "footer": {
          "text": "Ronnie Radke Updates"
        },
        "timestamp": age
      }]
    }
  )
  
def newstime():
  news = get_ronnie_radke_news()
  if news:
    title, description, url, age = news
    send_ronnie_radke_news(title, description, url, age)
    
schedule.every().day.at("22:34").do(newstime)

while True:
  schedule.run_pending()
  time.sleep(1)
# This script fetches the latest news about Ronnie Radke from the Brave Search API and sends it to a Discord channel using a webhook.
# It runs every day at 3:00 AM. The news is formatted and sent as an embed message in the Discord channel.