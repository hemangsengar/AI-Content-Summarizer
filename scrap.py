import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from database import *

SITE_CONFIGS = {
    'quotes': {
        'base_url': 'https://quotes.toscrape.com/',
        'start_page': 'page/1/',
        'article_selector': 'div.quote',
        'title_selector': 'span.text',
        'author_selector': 'small.author',
        'content_selector': 'span.text',
        'next_selector': 'li.next a',
        'type': 'quotes'
    },
    'hackernews': {
        'base_url': 'https://news.ycombinator.com/',
        'start_page': '',
        'article_selector': 'tr.athing',
        'title_selector': 'span.titleline a',
        'author_selector': 'a.hnuser',
        'content_selector': 'span.titleline a',
        'next_selector': 'a.morelink',
        'type': 'news'
    }
}

def scrape_articles(site_name: str, limit: int = 5):
    
    if site_name not in SITE_CONFIGS:
        raise ValueError(f"Site '{site_name}' not configured")
    
    config = SITE_CONFIGS[site_name]
    articles = []
    url = config['start_page']
    while url and len(articles) < limit:
        fullURL = urljoin(config['base_url'],url)
        print(f"Scrapping: {fullURL}")

        response = requests.get(fullURL)
        soup = BeautifulSoup(response.text,"html.parser")
        
        for ele in soup.find_all(config['article_selector']):
            title_elem = ele.select_one(config['title_selector'])
            author_elem = ele.select_one(config['author_selector'])
            content_elem = ele.select_one(config['content_selector'])
                      
            if title_elem and content_elem:
                articles.append({
                    'title': title_elem.get_text(strip=True),
                    'author': author_elem.get_text(strip=True) if author_elem else 'Unknown',
                    'content': content_elem.get_text(strip=True),
                    'source_url': fullURL,
                    'site': site_name
                })
        
        next_btn = soup.select_one(config['next_selector'])

        if next_btn and next_btn.a:
            url = next_btn.a['href']
        else:
            url = None
            print("Scrapping Completed!")
    return articles

    


if __name__ == "__main__":
    db()
    scrape_articles('hackernews')
    
    
    
    



    
    