import pandas as pd
from sqlalchemy import create_engine
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials


def save_to_csv(df, filename="products.csv"):
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


def save_to_postgresql(df, db_url):
    try:
        engine = create_engine(db_url)
        df.to_sql("products", engine, if_exists="replace", index=False)
        print("Data saved to PostgreSQL")
    except Exception as e:
        print(f"Error saving to PostgreSQL: {e}")


def save_to_google_sheets(df, spreadsheet_id, credentials_file):
    try:
        SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(credentials_file, scopes=SCOPES)
        service = build("sheets", "v4", credentials=creds)

        values = [df.columns.tolist()] + df.values.tolist()
        values = [[str(cell) for cell in row] for row in values]

        body = {"values": values}

        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range="Sheet1!A1",
            valueInputOption="RAW",
            body=body
        ).execute()

        print("Data saved to Google Sheets")

    except Exception as e:
        print(f"Error saving to Google Sheets: {e}")