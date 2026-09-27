# E-Commerce Web Scraper & Price Tracker

A Python-based data pipeline that scrapes product listings across multiple pages, cleans and formats price data, and persists records in an SQLite database for historical price tracking.

## Features
- **Automated Scraping:** Uses `BeautifulSoup4` and `requests` to crawl multi page e-commerce listings.
- **Data Sanitization:** Cleans raw currency strings into floating point numbers using regular expressions.
- **Persistence:** Stores structured records (title, price, timestamp) directly into a local SQLite database using `pandas`.
- **Tested:** Includes automated unit testing with `pytest` for parsing logic.

## Tech Stack
- Python 3.13
- BeautifulSoup4
- Requests
- Pandas
- SQLite3
- pytest

## Getting Started

### 1. Installation
Clone the repository and install required dependencies:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install requests beautifulsoup4 pandas pytest 