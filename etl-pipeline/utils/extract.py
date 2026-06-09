import requests
from bs4 import BeautifulSoup

BASE_URL = "https://fashion-studio.dicoding.dev"


def scrape_products():
    products = []
    page = 1

    while page <= 50:
        try:
            if page == 1:
                url = BASE_URL
            else:
                url = f"{BASE_URL}/page{page}"

            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            cards = soup.select("div.collection-card")

            if not cards:
                break

            for card in cards:
                title = card.select_one("h3.product-title")
                title = title.text.strip() if title else None

                price = card.select_one("div.price-container span.price")
                price = price.text.strip() if price else "Price Unavailable"

                paragraphs = card.select("div.product-details p")
                rating = None
                colors = None
                size = None
                gender = None

                for p in paragraphs:
                    text = p.text.strip()
                    if "Rating:" in text:
                        rating = text
                    elif "Colors" in text:
                        colors = text
                    elif "Size:" in text:
                        size = text
                    elif "Gender:" in text:
                        gender = text

                products.append({
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "colors": colors,
                    "size": size,
                    "gender": gender
                })

            page += 1

        except Exception as e:
            print(f"Error scraping page {page}: {e}")
            break

    return products
