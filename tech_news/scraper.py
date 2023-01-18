import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)

    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    links = selector.css(".entry-title > a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page_link = selector.css("a.next.page-numbers ::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    s = Selector(text=html_content)
    url = s.css("link[rel='canonical']::attr(href)").get()
    title = str(s.css("h1.entry-title::text").get()).strip()
    timestamp = s.css("li.meta-date::text").get()
    writer = s.css("span.author a::text").get()

    comments_count = s.css(".post-comments h5::text").re_first(r"\d+")
    if type(comments_count) != str:
        comments_count = 0
    else:
        comments_count = int(comments_count)

    raw_summary = s.css(".entry-content > p").get()
    soup = BeautifulSoup(raw_summary, 'html.parser')
    for tag in soup.find_all(['strong', 'a', 'span', 'em']):
        tag.replace_with(tag.text)
    summary = soup.text.strip()

    tags = s.css("a[rel='tag']::text").getall()
    category = s.css(".entry-details span.label::text").get()

    news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    BASE_URL = "https://blog.betrybe.com"
    page = fetch(BASE_URL)

    total_pages = amount // 12
    lp_quant_links = amount % 12

    news_links = []
    page_numb = 1
    while page_numb <= total_pages:
        this_page_links = scrape_updates(page)
        news_links.extend(this_page_links)

        if amount > page_numb * 12:
            next_page = scrape_next_page_link(page)
            print(next_page)
            page = fetch(next_page)

        page_numb += 1

    if lp_quant_links > 0:
        last_page_links = scrape_updates(page)
        news_links.extend(last_page_links[:lp_quant_links])

    news_list = []
    for link in news_links:
        news_page = fetch(link)
        news_data = scrape_news(news_page)
        news_list.append(news_data)

    create_news(news_list)
    return news_list
