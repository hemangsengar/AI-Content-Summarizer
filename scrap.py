import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from database import *

headers = {'User-Agent': 'Mozilla/5.0'}

SITE_CONFIGS = {
    'quotes': {
        'base_url': 'https://quotes.toscrape.com/',
        'start_page': 'page/1/',
        'article_selector': {'tag': 'div', 'class': 'quote'},
        'title_selector': {'tag': 'span', 'class': 'text'},
        'author_selector': {'tag': 'small', 'class': 'author'},
        'content_selector': {'tag': 'span', 'class': 'text'},
        'next_selector': {'tag': 'a', 'parent': 'li', 'parent_class': 'next'},
        'type': 'quotes'
    },
    'thehackernews': {
        'base_url': 'https://thehackernews.com/',
        'start_page': '',
        'article_selector': {'tag': 'div', 'class': 'body-post'},
        'next_selector': {'tag': 'a', 'class': 'blog-pager-older-link'},
        'type': 'cybersecurity'
    }
}

def scrape_articles(site_name: str, limit: int = 5):
    if site_name not in SITE_CONFIGS:
        raise ValueError(f"Site '{site_name}' not configured")

    config = SITE_CONFIGS[site_name]
    articles = []
    url = config['start_page']

    while len(articles) < limit:
        full_url = urljoin(config['base_url'], url)
        response = requests.get(full_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        if site_name == 'quotes':
            quote_blocks = soup.find_all('div', class_='quote')
            for quote in quote_blocks:
                if len(articles) >= limit:
                    break
                quote_text = quote.find('span', class_='text').text.strip()
                author = quote.find('small', class_='author').text.strip()
                articles.append({
                    'title': quote_text[:25] + '...' if len(quote_text) > 25 else quote_text,
                    'author': author,
                    'content': quote_text,
                    'source_url': full_url,
                    'site': site_name
                })
            next_li = soup.find('li', class_='next')
            next_btn = next_li.find('a') if next_li else None
            url = next_btn.get('href') if next_btn else None

        elif site_name == 'thehackernews':
            post_blocks = soup.find_all("div", class_="body-post")
            links = []
            for post in post_blocks:
                a_tag = post.find("a", class_="story-link")
                if a_tag and a_tag.get("href"):
                    links.append(a_tag["href"])

            for link in links:
                if len(articles) >= limit:
                    break
                try:
                    article_resp = requests.get(link, headers=headers)
                    article_soup = BeautifulSoup(article_resp.text, "html.parser")

                    title_tag = article_soup.find("h1", class_="story-title")
                    content_div = article_soup.find("div", class_="articlebody")

                    title = title_tag.text.strip() if title_tag else "N/A"
                    paragraphs = content_div.find_all("p") if content_div else []
                    content = "\n".join(p.text.strip() for p in paragraphs if p.text.strip())

                    articles.append({
                        'title': title,
                        'author': "The Hacker News",
                        'content': content,
                        'source_url': link,
                        'site': site_name
                    })
                    print(f"Scraped: {title}")
                except Exception as e:
                    print(f"Error scraping {link}: {e}")

            next_btn = soup.find("a", class_="blog-pager-older-link")
            url = next_btn.get('href') if next_btn else None

    print("Scraping Completed!")
    return articles




