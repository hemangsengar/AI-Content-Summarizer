import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv


'''
set PYTHONIOENCODING=utf-8

run in terminal to get the the character which does not support the default terminal encoding

'''


def scrape():
    base_url = "https://quotes.toscrape.com/"
    url = "page/1/"

    quotes = []

    while url:
        fullURL = urljoin(base_url,url)
        print(f"Scrapping: {fullURL}")

        responce = requests.get(fullURL)
        soup = BeautifulSoup(responce.text,"html.parser")
        
        for ele in soup.find_all('div', class_ = 'quote'):
            quote = ele.find('span', class_ ='text').text.lower()
            author = ele.find('small', class_ ='author').text.lower()
            quotes.append({'quote':quote,'author':author})
        
        next_btn = soup.find('li',class_ = 'next')

        if next_btn and next_btn.a:
            url = next_btn.a['href']
        else:
            url = None

    filename = 'quotes.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, ['quote','author'])
        w.writeheader()
        for quote in quotes:
            w.writerow(quote)


if __name__ == "__main__":
    scrape()
    
    
    
    



    
    