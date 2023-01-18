from tech_news.database import search_news
from datetime import datetime


# Auxiliar
def news_tuplator(news_list):
    news_tuple = [(news["title"], news["url"]) for news in news_list]
    return news_tuple


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    result = search_news(
        {"title": {"$regex": f"{title}", "$options": "i"}}
    )
    news_list = news_tuplator(result)
    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    date_type = "%Y-%m-%d"
    try:
        raw_date = datetime.strptime(date, date_type)
        formated_date = datetime.strftime(raw_date, "%d/%m/%Y")
        result = search_news(
            {"timestamp": formated_date}
        )
        news_list = news_tuplator(result)
        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    result = search_news(
        {"tags": {"$regex": f"^{tag}$", "$options": "i"}}
    )
    news_list = news_tuplator(result)
    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
