import pytest
from scraper import parse_products

def test_parse_products():
    # Mock HTML structure similar to books.toscrape.com
    sample_html = """
    <article class="product_pod">
        <h3><a title="Test Book Title" href="book.html">Test Book Title</a></h3>
        <p class="price_color">£12.34</p>
    </article>
    """
    
    result = parse_products(sample_html)
    
    assert len(result) == 1
    assert result[0]["title"] == "Test Book Title"
    assert result[0]["price"] == 12.34
    assert isinstance(result[0]["price"], float) 