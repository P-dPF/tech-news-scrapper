from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    search_result = search_news(query)
    formatted_results = list()

    if not search_result:
        return []

    for result in search_result:
        formatted_results.append((result["title"], result["url"]))

    return formatted_results


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
