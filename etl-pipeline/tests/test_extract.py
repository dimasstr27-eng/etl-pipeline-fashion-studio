import unittest
from unittest.mock import patch, MagicMock
from utils.extract import scrape_products

MOCK_HTML = """
<html><body>
  <div class="collection-card">
    <div class="product-details">
      <h3 class="product-title">T-shirt 1</h3>
      <div class="price-container"><span class="price">$100.00</span></div>
      <p style="font-size: 14px; color: #777;">Rating: ⭐ 4.5 / 5</p>
      <p style="font-size: 14px; color: #777;">3 Colors</p>
      <p style="font-size: 14px; color: #777;">Size: M</p>
      <p style="font-size: 14px; color: #777;">Gender: Men</p>
    </div>
  </div>
</body></html>
"""

class TestExtract(unittest.TestCase):

    @patch("utils.extract.requests.get")
    def test_scrape_returns_list(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = MOCK_HTML
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response
        products = scrape_products()
        self.assertIsInstance(products, list)

    @patch("utils.extract.requests.get")
    def test_scrape_keys(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = MOCK_HTML
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response
        products = scrape_products()
        keys = ["title", "price", "rating", "colors", "size", "gender"]
        for key in keys:
            self.assertIn(key, products[0])

    @patch("utils.extract.requests.get")
    def test_scrape_error_handling(self, mock_get):
        mock_get.side_effect = Exception("Connection error")
        products = scrape_products()
        self.assertEqual(products, [])

if __name__ == "__main__":
    unittest.main()