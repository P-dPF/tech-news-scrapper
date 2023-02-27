import requests
import time
from parsel import Selector
from tech_news.database import create_news

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
    title = selector.css(".entry-title::text").get()

    if title is not None:
        title = title.strip()

    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author > a::text").get()
    reading_time = selector.css(".meta-reading-time::text").re_first(r"\d+")

    if reading_time is not None:
        reading_time = int(reading_time)

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
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


def scrape_all_page_news(news_urls_list):
    news_list = list()

    for news_url in news_urls_list:
        current_news = scrape_news(fetch(news_url))
        news_list.append(current_news)
    return news_list


# Requisito 5
def get_tech_news(amount):
    next_page_url = "https://blog.betrybe.com/"
    news_list = list()

    while next_page_url:
        htmt_content = fetch(next_page_url)
        news_urls_list = scrape_updates(htmt_content)
        news_list.extend(scrape_all_page_news(news_urls_list))

        if len(news_list) >= amount:
            next_page_url = None
            news_list = news_list[0:amount]
        else:
            next_page_url = scrape_next_page_link(htmt_content)

    create_news(news_list)
    return news_list
