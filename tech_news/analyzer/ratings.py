from collections import Counter
from tech_news.analyzer.search_engine import news_tuplator
from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    results = find_news()
    news = sorted(
        results, key=lambda results: results["title"]
    )
    sorted_by_comments = sorted(
        news, key=lambda news: news["comments_count"]
    )
    sorted_by_comments.reverse()
    top_news = sorted_by_comments[:5]
    return news_tuplator(top_news)


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    # results = find_news()
    # categories = [news["category"] for news in results]
    # counted = Counter(categories)

    # return 
