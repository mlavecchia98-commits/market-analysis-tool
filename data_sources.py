# data_sources.py
import pandas as pd
import yfinance as yf
import random
from datetime import datetime

# --- Funzione demo ---
def get_demo_data():
    anni = list(range(2010, 2024))
    valori = [random.randint(50, 150) for _ in anni]
    df = pd.DataFrame({"Anno": anni, "Valore": valori})
    return df

# --- Funzione per dati World Bank ---
def get_world_bank_data(indicator, country="IT", start_year=2010, end_year=2023):
    try:
        from wbdata import get_dataframe
    except ImportError:
        raise ImportError("Installa wbdata: pip install wbdata")
    
    import datetime as dt
    data_dates = (dt.datetime(start_year, 1, 1), dt.datetime(end_year, 12, 31))
    df = get_dataframe({indicator: indicator}, country=country, data_date=data_dates)
    df = df.reset_index().rename(columns={"date": "Anno", indicator: "Valore"})
    df["Anno"] = df["Anno"].astype(int)
    df = df.sort_values("Anno")
    return df

# --- Funzione per dati ISTAT ---
def get_istat_data(dataset_code, start_year=2010, end_year=2023):
    # Qui restituiamo dati demo perché ISTAT richiede API o scraping
    anni = list(range(start_year, end_year + 1))
    valori = [random.randint(1000, 5000) for _ in anni]
    df = pd.DataFrame({"Anno": anni, "Valore": valori})
    return df

# --- Funzione per dati Eurostat ---
def get_eurostat_data(dataset_code, start_year=2010, end_year=2023):
    # Qui restituiamo dati demo perché Eurostat richiede API o scraping
    anni = list(range(start_year, end_year + 1))
    valori = [random.randint(500, 2000) for _ in anni]
    df = pd.DataFrame({"Anno": anni, "Valore": valori})
    return df

# --- Funzione per dati azioni ---
def get_stock_data(ticker):
    today = datetime.today()
    start_date = datetime(today.year - 10, 1, 1)
    df = yf.download(ticker, start=start_date, end=today)
    df = df.reset_index()
    df = df.rename(columns={"Date": "Data", "Close": "Prezzo"})
    return df[["Data", "Prezzo"]]
