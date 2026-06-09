# 🛒 ETL Pipeline - Fashion Studio
ETL Pipeline sederhana yang mengambil data produk fashion dari website [Fashion Studio Dicoding](https://fashion-studio.dicoding.dev), melakukan transformasi data, dan menyimpannya ke berbagai repositori data.
## 📋 Deskripsi
Project ini merupakan implementasi ETL (Extract, Transform, Load) Pipeline yang:
- **Extract**: Scraping 1000 produk dari 50 halaman website Fashion Studio
- **Transform**: Membersihkan dan memproses data mentah menjadi 867 data bersih
- **Load**: Menyimpan data ke CSV, PostgreSQL, dan Google Sheets
## 🛠️ Teknologi yang Digunakan
- **Python 3.x**
- **Pandas** - transformasi data
- **BeautifulSoup4** - web scraping
- **Requests** - HTTP requests
- **SQLAlchemy** - koneksi database
- **PostgreSQL** - penyimpanan database
- **Google Sheets API** - penyimpanan spreadsheet
- **Pytest** - unit testing
## 📁 Struktur Project
```
etl-pipeline/
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── utils/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── main.py
├── requirements.txt
├── submission.txt
└── products.csv
```
## ⚙️ Cara Install
1. Clone repository ini:
```bash
git clone https://github.com/dimasstr27-eng/etl-pipeline-fashion-studio.git
cd etl-pipeline-fashion-studio/etl-pipeline
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Siapkan PostgreSQL:
   - Buat database bernama `products`
   - Update `DB_URL` di `main.py` sesuai kredensial kamu
4. Siapkan Google Sheets API:
   - Buat project di Google Cloud Console
   - Aktifkan Google Sheets API
   - Download credentials JSON → rename ke `google-sheets-api.json`
   - Update `SPREADSHEET_ID` di `main.py`
## 🚀 Cara Menjalankan
```bash
python main.py
```
## 🧪 Menjalankan Unit Test
```bash
python -m pytest tests -v
```
## 📊 Menjalankan Test Coverage
```bash
coverage run -m pytest tests
coverage report
```
## 📈 Hasil
| Metric | Nilai |
|--------|-------|
| Total data di-scrape | 1000 produk |
| Data setelah transformasi | 867 produk |
| Test coverage | 96% |
| Unit test | 13/13 passed |
## 🔗 Google Sheets
Data hasil ETL dapat dilihat di:
[Google Sheets - Products](https://docs.google.com/spreadsheets/d/17QfZUcQw3peDny1z9W0k8FI85l24Fi16oCvMd9MGYLU)
## 👨‍💻 Author
**Dimas Satria**
- GitHub: [@dimasstr27-eng](https://github.com/dimasstr27-eng)
