from database import *
from scrap import *
import re
from Gemini import *
import string


def clean_text(text:str):
    text = text.lower()  # Lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = BeautifulSoup(text, "html.parser").get_text()  # Remove HTML tags
    return text



def main():
    create_articles_table()
    
    # Step 1: Scrape articles
    site = input("Enter the site to scrape (e.g., 'quotes', 'thehackernews', etc.): ").strip()
    print("Starting Data Scrapping!")
    articles = scrape_articles(site, limit=5)
    

    if summarize_text:
        print("Summarising Content")


    for article in articles:
        # Step 2: Preprocess
        cleaned_content = clean_text(article['content'])
        
        # Step 3: Summarize with Gemini and Preprocess
        summary = clean_text(summarize_text(cleaned_content))

        
        # Step 4: Store in database
        article_data = {
            'title': article['title'],
            'author': article['author'],
            'content': cleaned_content,
            'summary': summary,
            'source_url': article['source_url']
        }
        store_article(article_data)

    
    print("Data stored in Database!")

if __name__ == "__main__":
    main()