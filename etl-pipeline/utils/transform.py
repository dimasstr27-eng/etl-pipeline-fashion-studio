import pandas as pd


def transform_products(products):
    df = pd.DataFrame(products)

    # Hapus duplikat
    df = df.drop_duplicates()

    # Hapus baris yang semua nilainya null
    df = df.dropna(how="all")
    # Hapus produk dengan title "Unknown Product"
    df = df[df["title"] != "Unknown Product"]

    # Bersihkan kolom price
    df["price"] = df["price"].replace("Price Unavailable", pd.NA)
    df = df.dropna(subset=["price"])
    df["price"] = df["price"].str.extract(r"(\d+\.\d+)").astype(float)

    # Bersihkan kolom rating
    df["rating"] = df["rating"].str.extract(r"(\d+\.\d+|\d+)")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df = df.dropna(subset=["rating"])

    # Bersihkan kolom colors
    df["colors"] = df["colors"].str.extract(r"(\d+)")
    df["colors"] = pd.to_numeric(df["colors"], errors="coerce")

    # Bersihkan kolom size
    df["size"] = df["size"].str.replace("Size: ", "").str.strip()

    # Bersihkan kolom gender
    df["gender"] = df["gender"].str.replace("Gender: ", "").str.strip()

    # Bersihkan kolom title
    df["title"] = df["title"].str.strip()

    # Reset index
    df = df.reset_index(drop=True)

    return df