import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_sources import get_data
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Market Analysis Tool")

prompt = st.text_input("Inserisci la tua richiesta in linguaggio naturale")

if prompt:
    # Qui idealmente useremmo OpenAI per capire cosa fare con il prompt
    # Per semplificazione, chiediamo all'utente quale dataset vuole
    st.write("Ecco un esempio di grafico generato da dati di esempio")
    data = get_data("example")
    st.line_chart(data)
