import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


'''
set PYTHONIOENCODING=utf-8

run in terminal to get the the character which does not support the default terminal encoding

'''


def scrap():
    base_url = "https://quotes.toscrape.com/"
    url = "page/1/"

    quotes = []

    while url:
        fullURL = 