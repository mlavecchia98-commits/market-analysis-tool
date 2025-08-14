import pandas as pd
import yfinance as yf
import requests

# --- Demo data ---
def get_demo_data():
    return pd.DataFrame({
        "Anno": list(range(2010, 2024)),
        "Valore": [i*10 for i in range(2010, 2024)]
    })

# --- World Bank ---
def get_world_bank_data(indicator, country="IT", start_year=2010, end_year=2023):
    url = f"http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&date={start_year}:{end_year}"
    resp = requests.get(url)
    data = resp.json()[1]
    df = pd.DataFrame({
        "Anno": [int(d['date']) for d in data],
        "Valore": [d['value'] for d in data]
    }).sort_values("Anno")
    return df

# --- Yahoo Finance ---
def get_stock_data(ticker):
    df = yf.download(ticker, progress=False)
    df.reset_index(inplace=True)
    df.rename(columns={"Date":"Data", "Close":"Prezzo"}, inplace=True)
    return df[["Data", "Prezzo"]]

# --- ISTAT (esempio generico, usa API ISTAT se disponibili) ---
def get_istat_data(dataset_code, start_year=2010, end_year=2023):
    # Per demo, ritorna valori casuali
    df = pd.DataFrame({
        "Anno": list(range(start_year, end_year+1)),
        "Valore": [100+i*5 for i in range(end_year-start_year+1)]
    })
    return df

# --- Eurostat (demo) ---
def get_eurostat_data(dataset_code, start_year=2010, end_year=2023):
    df = pd.DataFrame({
        "Anno": list(range(start_year, end_year+1)),
        "Valore": [50+i*3 for i in range(end_year-start_year+1)]
    })
    return df

# --- Top 10 aziende italiane per fatturato ---
def get_top_italian_companies():
    # Esempio: recupero dati reali da Wikipedia
    url = "https://it.wikipedia.org/wiki/Lista_delle_principali_imprese_italiane_per_fatturato"
    tables = pd.read_html(url, decimal=",", thousands=".")
    df = tables[0].iloc[:10]  # prende le prime 10
    df = df[["Azienda", "Fatturato (milioni €)"]].rename(columns={"Fatturato (milioni €)":"Fatturato"})
    df["Fatturato"] = df["Fatturato"].str.replace(".", "", regex=False).astype(float)
    return df
