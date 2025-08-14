import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from openai import OpenAI
import os
from data_sources import get_world_bank_data, get_stock_data, get_istat_data, get_eurostat_data, get_demo_data

# --- Recupero API key ---
api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
if not api_key:
    st.error("❌ API Key mancante. Aggiungila in st.secrets o come variabile d'ambiente OPENAI_API_KEY.")
    st.stop()

client = OpenAI(api_key=api_key)

# --- Funzione per interpretare la frase ---
def interpret_request_with_ai(user_input):
    prompt = f"""
    Analizza la frase e restituisci in JSON:
    1. tipo di dato (es: GDP, popolazione, fatturato, azioni, inflazione, ecc.)
    2. fonte preferita (World Bank, ISTAT, Eurostat, Yahoo Finance)
    3. paese o azienda
    4. periodo (start_year, end_year)
    Frase: {user_input}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    import json
    return json.loads(response.choices[0].message.content)

# --- Funzione per creare grafico ---
def plot_chart(df, x_col, y_col, title):
    fig, ax = plt.subplots(figsize=(10,6))
    if pd.api.types.is_numeric_dtype(df[y_col]):
        ax.plot(df[x_col], df[y_col], marker="o", color="skyblue")
    else:
        ax.bar(df[x_col], df[y_col], color="skyblue")
    ax.set_title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

# --- Interfaccia Streamlit ---
st.title("📊 Market Analysis Tool")
st.write("Scrivi una frase in linguaggio naturale per generare grafici con dati reali.")

user_input = st.text_input("La tua domanda:")

if user_input:
    try:
        params = interpret_request_with_ai(user_input)
        st.write("🔍 Parametri interpretati:", params)

        tipo = params.get("tipo", "demo").lower()
        fonte = params.get("fonte", "").lower()
        paese = params.get("paese", "IT")
        azienda = params.get("azienda", "AAPL")
        start_year = params.get("start_year", 2010)
        end_year = params.get("end_year", 2023)

        if fonte == "world bank":
            if tipo in ["gdp", "pil"]:
                df = get_world_bank_data("NY.GDP.MKTP.CD", country=paese, start_year=start_year, end_year=end_year)
                fig = plot_chart(df, "Anno", "Valore", f"PIL {paese}")
            elif tipo == "popolazione":
                df = get_world_bank_data("SP.POP.TOTL", country=paese, start_year=start_year, end_year=end_year)
                fig = plot_chart(df, "Anno", "Valore", f"Popolazione {paese}")

        elif fonte == "istat":
            df = get_istat_data(dataset_code=tipo, start_year=start_year, end_year=end_year)
            fig = plot_chart(df, "Anno", "Valore", f"Dati ISTAT: {tipo}")

        elif fonte == "eurostat":
            df = get_eurostat_data(dataset_code=tipo, start_year=start_year, end_year=end_year)
            fig = plot_chart(df, "Anno", "Valore", f"Dati Eurostat: {tipo}")

        elif fonte == "yahoo finance":
            df = get_stock_data(azienda)
            fig = plot_chart(df, "Data", "Prezzo", f"Andamento azioni {azienda}")

        else:
            df = get_demo_data()
            fig = plot_chart(df, "Anno", "Valore", "Esempio dati")

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Errore: {e}")
