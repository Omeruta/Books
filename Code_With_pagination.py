import requests
import pandas as pd
from bs4 import BeautifulSoup 

URL = 'http://books.toscrape.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','Accept-Language': 'en-US,en;q=0.9',}

response = requests.get(URL, headers=headers)
print(response.text)

response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "html.parser")

Books = soup.find_all("article", class_="product_pod")
for book in Books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()
    rating = book.find("p", class_="star-rating")["class"][1]
    print(f" Title: {title}, Price: {price}, Availability {availability}, Rating {rating}")
    