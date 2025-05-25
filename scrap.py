import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from database import *



def scrape():
    base_url = "https://quotes.toscrape.com/"
    url = "page/1/"
    
    while url:
        fullURL = urljoin(base_url,url)
        print(f"Scrapping: {fullURL}")

        responce = requests.get(fullURL)
        soup = BeautifulSoup(responce.text,"html.parser")
        
        for ele in soup.find_all('div', class_ = 'quote'):
            quote = ele.find('span', class_ ='text').text.lower().strip()
            author = ele.find('small', class_ ='author').text.lower().strip()
            insert_quote(quote, author)
        
        next_btn = soup.find('li',class_ = 'next')

        if next_btn and next_btn.a:
            url = next_btn.a['href']
        else:
            url = None
            print("Scrapping Completed!")

    


if __name__ == "__main__":
    db()
    scrape()
    
    
    
    



    
    