import pandas as pd
import yfinance as yf
import requests

# --- World Bank ---
def get_world_bank_data(indicator, country="IT", start_year=2010, end_year=2023):
    url = f"http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?date={start_year}:{end_year}&format=json"
    response = requests.get(url)
    data = response.json()
    if len(data) < 2:
        return pd.DataFrame(columns=["Anno", "Valore"])
    records = [{"Anno": int(item["date"]), "Valore": item["value"]} for item in data[1] if item["value"] is not None]
    df = pd.DataFrame(records)
    return df

# --- Yahoo Finance ---
def get_stock_data(ticker):
    df = yf.download(ticker)
    df.reset_index(inplace=True)
    df = df.rename(columns={"Date": "Data", "Close": "Prezzo"})
    return df[["Data", "Prezzo"]]

# --- ISTAT ---
def get_istat_data(dataset_code, start_year=2010, end_year=2023):
    # Questo è un esempio fittizio, da sostituire con API reale ISTAT se disponibile
    years = list(range(start_year, end_year + 1))
    values = [1000 + i*50 for i in range(len(years))]
    df = pd.DataFrame({"Anno": years, "Valore": values})
    return df

# --- Eurostat ---
def get_eurostat_data(dataset_code, start_year=2010, end_year=2023):
    # Questo è un esempio fittizio, da sostituire con API reale Eurostat se disponibile
    years = list(range(start_year, end_year + 1))
    values = [500 + i*30 for i in range(len(years))]
    df = pd.DataFrame({"Anno": years, "Valore": values})
    return df

# --- Demo dati ---
def get_demo_data():
    df = pd.DataFrame({
        "Anno": [2018, 2019, 2020, 2021, 2022],
        "Valore": [100, 150, 200, 250, 300]
    })
    return df
