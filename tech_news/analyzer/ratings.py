from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    news_list = find_news()
    raw_categories_list = [news["category"] for news in news_list]

    if not raw_categories_list:
        return []

    raw_categories_list.sort()

    sorted_categories_list = [
        category[0] for category in Counter(raw_categories_list).most_common(5)
    ]

    return sorted_categories_list
