import unittest
import pandas as pd
from unittest.mock import patch, MagicMock
from utils.load import save_to_csv, save_to_postgresql, save_to_google_sheets


class TestLoad(unittest.TestCase):

    def setUp(self):
        self.sample_df = pd.DataFrame({
            "title": ["T-shirt 1", "Hoodie 1"],
            "price": [100.00, 200.00],
            "rating": [4.5, 3.5],
            "colors": [3, 2],
            "size": ["M", "L"],
            "gender": ["Men", "Women"]
        })

    @patch("utils.load.pd.DataFrame.to_csv")
    def test_save_to_csv(self, mock_csv):
        save_to_csv(self.sample_df, "test_products.csv")
        mock_csv.assert_called_once()

    @patch("utils.load.create_engine")
    def test_save_to_postgresql_success(self, mock_engine):
        mock_eng = MagicMock()
        mock_engine.return_value = mock_eng
        save_to_postgresql(self.sample_df, "postgresql://postgres:password@localhost:5432/products")
        mock_engine.assert_called_once()

    @patch("utils.load.create_engine")
    def test_save_to_postgresql_error(self, mock_engine):
        mock_engine.side_effect = Exception("Connection error")
        try:
            save_to_postgresql(self.sample_df, "postgresql://wrong:wrong@localhost:5432/products")
        except Exception:
            self.fail("save_to_postgresql raised exception unexpectedly")

    @patch("utils.load.build")
    @patch("utils.load.Credentials")
    def test_save_to_google_sheets(self, mock_creds, mock_build):
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        mock_creds.from_service_account_file.return_value = MagicMock()
        save_to_google_sheets(self.sample_df, "spreadsheet_id", "credentials.json")
        mock_build.assert_called_once()


if __name__ == "__main__":
    unittest.main()