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

def scrape_articles():
    base_url = "https://quotes.toscrape.com/"
    url = "page/1/"
    articles = []
    while url:
        fullURL = urljoin(base_url,url)
        print(f"Scrapping: {fullURL}")

        response = requests.get(fullURL)
        soup = BeautifulSoup(response.text,"html.parser")
        
        for ele in soup.find_all('div', class_ = 'quote'):
            quote = ele.find('span', class_ ='text').text.lower().strip()
            author = ele.find('small', class_ ='author').text.lower().strip()
            raw = ele.find('span', class_ ='text').text            
            insert_quote(quote, author, raw_content=raw)
        
        next_btn = soup.find('li',class_ = 'next')

        if next_btn and next_btn.a:
            url = next_btn.a['href']
        else:
            url = None
            print("Scrapping Completed!")

    


if __name__ == "__main__":
    db()
    scrape()
    
    
    
    



    
    