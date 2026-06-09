import unittest
import pandas as pd
from utils.transform import transform_products


class TestTransform(unittest.TestCase):

    def setUp(self):
        self.sample_data = [
            {
                "title": "T-shirt 1",
                "price": "$100.00",
                "rating": "Rating: ⭐ 4.5 / 5",
                "colors": "3 Colors",
                "size": "Size: M",
                "gender": "Gender: Men"
            },
            {
                "title": "Hoodie 1",
                "price": "$200.00",
                "rating": "Rating: ⭐ 3.5 / 5",
                "colors": "2 Colors",
                "size": "Size: L",
                "gender": "Gender: Women"
            },
            {
                "title": "T-shirt 1",
                "price": "$100.00",
                "rating": "Rating: ⭐ 4.5 / 5",
                "colors": "3 Colors",
                "size": "Size: M",
                "gender": "Gender: Men"
            },
            {
                "title": "Invalid Product",
                "price": "Price Unavailable",
                "rating": "Rating: ⭐ Invalid Rating / 5",
                "colors": "1 Colors",
                "size": "Size: S",
                "gender": "Gender: Men"
            }
        ]

    def test_returns_dataframe(self):
        df = transform_products(self.sample_data)
        self.assertIsInstance(df, pd.DataFrame)

    def test_removes_duplicates(self):
        df = transform_products(self.sample_data)
        self.assertEqual(len(df), df.drop_duplicates().shape[0])

    def test_removes_price_unavailable(self):
        df = transform_products(self.sample_data)
        self.assertNotIn("Price Unavailable", df["price"].values)

    def test_price_is_float(self):
        df = transform_products(self.sample_data)
        self.assertEqual(df["price"].dtype, float)

    def test_rating_is_numeric(self):
        df = transform_products(self.sample_data)
        self.assertTrue(pd.api.types.is_numeric_dtype(df["rating"]))

    def test_columns_exist(self):
        df = transform_products(self.sample_data)
        for col in ["title", "price", "rating", "colors", "size", "gender"]:
            self.assertIn(col, df.columns)


if __name__ == "__main__":
    unittest.main()