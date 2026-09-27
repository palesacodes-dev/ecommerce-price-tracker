import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime
import re

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def fetch_html(url):
    """Fetch raw HTML content from a target URL."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return None  # Reached the last page
    response.raise_for_status()
    return response.text

def parse_products(html):
    """Extract product titles and prices from raw HTML."""
    soup = BeautifulSoup(html, "html.parser")
    products = []
    
    articles = soup.find_all("article", class_="product_pod")
    for item in articles:
        title = item.h3.a["title"]
        price_text = item.find("p", class_="price_color").text
        clean_price = re.sub(r"[^\d.]", "", price_text)
        price = float(clean_price)
        
        products.append({
            "title": title,
            "price": price,
            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    return products

def scrape_multiple_pages(max_pages=3):
    """Scrape product data across multiple pages."""
    all_products = []
    
    for page in range(1, max_pages + 1):
        url = BASE_URL.format(page)
        print(f"Fetching page {page}...")
        html_content = fetch_html(url)
        
        if not html_content:
            print("No more pages found.")
            break
            
        products = parse_products(html_content)
        all_products.extend(products)
        
    return all_products

def save_to_database(data, db_name="prices.db"):
    """Store extracted product data into a local SQLite database."""
    df = pd.DataFrame(data)
    conn = sqlite3.connect(db_name)
    df.to_sql("product_prices", conn, if_exists="append", index=False)
    conn.close()
    print(f"Successfully saved {len(data)} total items to {db_name}!")

if __name__ == "__main__":
    print("Starting multi-page scraper...")
    scraped_data = scrape_multiple_pages(max_pages=3)
    save_to_database(scraped_data) 