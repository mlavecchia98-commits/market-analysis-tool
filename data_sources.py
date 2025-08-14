import pandas as pd
import yfinance as yf
import wbdata
from datetime import datetime

def get_world_bank_data(indicator, country="IT", start_year=2010, end_year=2023):
    """Scarica dati dal World Bank."""
    df = wbdata.get_dataframe(
        {indicator: indicator},
        country=country,
        data_date=(datetime(start_year, 1, 1), datetime(end_year, 12, 31))
    )
    df = df.reset_index()
    df.rename(columns={indicator: "Valore", "date": "Anno"}, inplace=True)
    return df

def get_stock_data(ticker="AAPL"):
    """Scarica dati azioni da Yahoo Finance."""
    df = yf.download(ticker)
    df.reset_index(inplace=True)
    df.rename(columns={"Close": "Prezzo", "Date": "Data"}, inplace=True)
    return df

def get_istat_data(dataset_code, start_year=2010, end_year=2023):
    """Dati demo ISTAT (simulazione)."""
    df = pd.DataFrame({
        "Anno": list(range(start_year, end_year + 1)),
        "Valore": [i * 1000 for i in range(start_year, end_year + 1)]
    })
    return df

def get_eurostat_data(dataset_code, start_year=2010, end_year=2023):
    """Dati demo Eurostat (simulazione)."""
    df = pd.DataFrame({
        "Anno": list(range(start_year, end_year + 1)),
        "Valore": [i * 500 for i in range(start_year, end_year + 1)]
    })
    return df

def get_demo_data():
    """Dati demo generici."""
    df = pd.DataFrame({
        "Anno": list(range(2010, 2024)),
        "Valore": [i * 10 for i in range(2010, 2024)]
    })
    return df
