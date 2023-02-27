from tech_news.database import search_news
from datetime import datetime


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
    received_date_format = "%Y-%m-%d"
    try:
        valid_date = datetime.strptime(date, received_date_format).date()

        if valid_date:
            date_elements = str(valid_date).split("-")
            year, month, day = (
                date_elements[0],
                date_elements[1],
                date_elements[2],
            )

            query = {"timestamp": f"{day}/{month}/{year}"}
            search_result = search_news(query)

            formatted_results = list()
            for result in search_result:
                formatted_results.append((result["title"], result["url"]))

            return formatted_results

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    search_result = search_news(query)
    formatted_results = list()

    if not search_result:
        return []

    for result in search_result:
        formatted_results.append((result["title"], result["url"]))

    return formatted_results
