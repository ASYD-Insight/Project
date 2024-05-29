import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

current_page = 1
data = []
proceed = True
item_id = 1

while proceed and current_page <= 50:
    print("Currently Scraping page:", current_page)
    url = f"https://books.toscrape.com/catalogue/page-{current_page}.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    if "Page not found" in soup.title.text:
        proceed = False
    else:
        all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for book in all_books:
            item = {
                'id': item_id,  # Add id field
                'Title': book.find("img").attrs["alt"],
                'Link': "https://books.toscrape.com/catalogue/" + book.find("a").attrs["href"],
                'Price': book.find("p", class_="price_color").text[1:],
                'Stock': book.find("p", class_="instock availability").text.strip()
            }
            data.append(item)
            item_id += 1  # Increment item id

    current_page += 1

df = pd.DataFrame(data)

df.to_csv("books.csv", index=False)
print("Data has been saved to books.csv")

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''DROP TABLE IF EXISTS books''')  # Drop table if it exists
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Link TEXT,
        Price TEXT,
        Stock TEXT
    )''')
print("Table created successfully")

df.to_sql('books', conn, if_exists='replace', index=False)
print("Data has been inserted into books.db")

conn.commit()
conn.close()
print("Database connection closed")
