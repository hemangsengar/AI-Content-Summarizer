import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from database import *

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
        'hackernews': {
            'base_url': 'https://news.ycombinator.com/',
            'start_page': '',
            'article_selector': {'tag': 'tr', 'class': 'athing'},
            'title_selector': {'tag': 'a', 'parent': 'span', 'parent_class': 'titleline'},
            'author_selector': None,  # No author on main page
            'content_selector': {'tag': 'a', 'parent': 'span', 'parent_class': 'titleline'},
            'next_selector': {'tag': 'a', 'class': 'morelink'},
            'type': 'news'
        },
        'thehackernews': {
            'base_url': 'https://thehackernews.com/',
            'start_page': '',
            'article_selector': {'tag': 'article', 'class': 'body-post'},
            'title_selector': {'tag': 'h2', 'class': 'home-title'},
            'author_selector': {'tag': 'span', 'class': 'h-author'},
            'content_selector': {'tag': 'div', 'class': 'home-desc'},
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
    while url and len(articles) < limit:
        fullURL = urljoin(config['base_url'],url)
        

        response = requests.get(fullURL)
        soup = BeautifulSoup(response.text,"html.parser")
        # Site Selection
        if site_name == 'quotes':
            for ele in soup.find_all('div', class_='quote'):
                if len(articles) >= limit:
                    break
                quote = ele.find('span', class_='text').text.strip()
                author = ele.find('small', class_='author').text.strip()
                
                articles.append({
                    'title': quote[:25] + '...' if len(quote) > 25 else quote,  # Short title
                    'author': author,
                    'content': quote,
                    'source_url': fullURL,
                    'site': site_name
                })
        elif site_name == 'hackernews':
            for ele in soup.find_all('tr', class_='athing'):
                if len(articles) >= limit:
                    break
                title_span = ele.find('span', class_='titleline')
                if title_span:
                    title_link = title_span.find('a')
                    if title_link:
                        title = title_link.text.strip()
                        
                        articles.append({
                            'title': title,
                            'author': 'Unknown',
                            'content': title,
                            'source_url': fullURL,
                            'site': site_name
                        })
        elif site_name == 'thehackernews':
            for ele in soup.find_all('article', class_='body-post'):
                if len(articles) >= limit:
                    break
                
                title_elem = ele.find('h2', class_='home-title')
                author_elem = ele.find('span', class_='h-author')
                content_elem = ele.find('div', class_='home-desc')
                
                if title_elem and content_elem:
                    title = title_elem.text.strip()
                    author = author_elem.text.strip() if author_elem else 'The Hacker News'
                    content = content_elem.text.strip()
                    
                    articles.append({
                        'title': title,
                        'author': author,
                        'content': content,
                        'source_url': fullURL,
                        'site': site_name
                    })
        
        if site_name == 'quotes':
            next_li = soup.find('li', class_='next')
            next_btn = next_li.find('a') if next_li else None
        elif site_name == 'hackernews':
            next_btn = soup.find('a', class_='morelink')
        elif site_name == 'thehackernews':
            next_btn = soup.find('a', class_='blog-pager-older-link')
        else:
            next_btn = None

        if next_btn:
            url = next_btn.get('href')
        else:
            url = None
            print("Scraping Completed!")
    return articles

    
'''
if __name__ == "__main__":
    create_articles_table()
    articles = scrape_articles('quotes')

    for article in articles:
        article_data = {
            'title': article['title'],
            'author': article['author'],
            'content': article['content'],
            'summary': None,  # No summary yet
            'source_url': article['source_url'],
            
        }
        store_article(article_data)
        print(f"Stored: {article['title']}")
    
    print(f"Successfully stored {len(articles)} articles!")
    
 '''
    



    
    