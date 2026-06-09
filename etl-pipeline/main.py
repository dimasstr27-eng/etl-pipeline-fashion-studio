from utils.extract import scrape_products
from utils.transform import transform_products
from utils.load import save_to_csv, save_to_postgresql, save_to_google_sheets

# Konfigurasi PostgreSQL - sesuaikan dengan password Anda
DB_URL = "postgresql://postgres:dimas2704@localhost:5432/products"

# Konfigurasi Google Sheets
SPREADSHEET_ID = "17QfZUcQw3peDny1z9W0k8FI85l24Fi16oCvMd9MGYLU"
CREDENTIALS_FILE = "google-sheets-api.json"


def main():
    print("=" * 50)
    print("ETL Pipeline - Fashion Studio")
    print("=" * 50)

    # EXTRACT
    print("\n[1] Extracting data...")
    products = scrape_products()
    print(f"    Extracted {len(products)} products")

    # TRANSFORM
    print("\n[2] Transforming data...")
    df = transform_products(products)
    print(f"    Transformed {len(df)} products")
    print(df.head())

    # LOAD
    print("\n[3] Loading data...")
    save_to_csv(df)
    save_to_postgresql(df, DB_URL)
    save_to_google_sheets(df, SPREADSHEET_ID, CREDENTIALS_FILE)

    print("\n✅ ETL Pipeline selesai!")


if __name__ == "__main__":
    main()