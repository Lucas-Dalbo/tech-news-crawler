import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup


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

    noticia = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }
    return noticia


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
