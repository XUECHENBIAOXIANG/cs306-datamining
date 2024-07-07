from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# Find all quote elements
quote_elements = soup.find_all(class_="quote")

# Initialize an empty list to store quotes
quotes_data = []

# Iterate over each quote element and extract information
for quote in quote_elements:
    # Extract quote text
    quote_text = quote.find(class_="text").get_text().strip()

    # Extract author
    author = quote.find(class_="author").get_text()

    # Extract tags
    tags = [tag.get_text() for tag in quote.find_all(class_="tag")]

    quote_info = {
        "quote_text": quote_text,
        "author": author,
        "tags": tags
    }

    quotes_data.append(quote_info)

print(quotes_data)
