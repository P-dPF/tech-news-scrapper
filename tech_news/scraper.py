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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
