import pandas as pd

def get_data(request_type):
    # Funzione di esempio: ritorna dati fittizi
    if request_type == "example":
        df = pd.DataFrame({
            "Anno": [2018, 2019, 2020, 2021, 2022],
            "Valore": [100, 120, 90, 150, 200]
        })
        df.set_index("Anno", inplace=True)
        return df
    return pd.DataFrame()
