import requests
import time
from parsel import Selector

# Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3,
        )
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news_urls_list = selector.css(".entry-title > a::attr(href)").getall()
    if not news_urls_list:
        return []
    return news_urls_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(".next::attr(href)").get()
    if not next_page_link:
        return None
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    news_url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author > a::text").get()
    reading_time = selector.css(".meta-reading-time::text").re_first(r"\d+")

    summary = selector.css(
        ".entry-content > p:nth-of-type(1) *::text"
    ).getall()
    summary = "".join(summary).strip()

    category = selector.css(".label::text").get()

    return {
        "url": news_url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
