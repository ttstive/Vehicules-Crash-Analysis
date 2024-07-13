import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide", page_title="Dashboard")
st.title("Vehicules Crash Analysis")

# Carregar os dados
df = pd.read_excel("dados_limpos.xlsx")
df["Date"] = pd.to_datetime(df["Date"].sort_values(ascending=True))
df["Month"] = df["Date"].apply(lambda x: f"{x.year}/{x.month:02d}")

# Definir filtros na barra lateral
month = st.sidebar.selectbox("Select the month for analysis", df["Month"].unique())
location = st.sidebar.selectbox("Select the location for analysis", df["Reported_Location"].value_counts(7).index)

# Atualizar descrição das lesões
change_description = {
    "No injury/unknown": "No injury",
    "Non-incapacitating injury": "No Incapacitating",
    "Fatal injury": "Fatal"
}
df["Injury Type"].replace(change_description, inplace=True)

# Filtrar os dados pelo mês selecionado
df_filtered = df[df["Month"] == month]

# Layout do dashboard
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Criar gráficos
fig = px.histogram(df_filtered, x="Date", color="Injury Type", nbins=30, title="Crash per day")
col1.plotly_chart(fig)

fig_total = px.pie(df_filtered, names="Injury Type", color="Injury Type", title="Injury Type Distribution")
col2.plotly_chart(fig_total)

fig_fator_colision = px.histogram(df_filtered, x="Collision Type", y="Primary Factor", color="Injury Type", 
                                  orientation="h", histfunc="count", title="Collision Type x Primary Factor", 
                                  width=1000, height=800)
col3.plotly_chart(fig_fator_colision)

# Contar o número total de acidentes
total_accidents = df_filtered["Injury Type"].count()

# Estilos customizados para o "card"
card_style = """
    <style>
    .card {
        position: fixed;
        bottom: 10px;
        right: 10px;
        width: 300px;
        padding: 20px;
        border-radius: 10px;
        background-color: black;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .card-title {
        font-size: 24px;
        font-weight: bold;
        color: white;
    }
    .card-value {
        font-size: 48px;
        color: red;
        font-weight: bold;
    }
    </style>
"""

# HTML para o "card"
card_html = f"""
    <div class="card">
        <div class="card-title">Total Crashes</div>
        <div class="card-value">{total_accidents}</div>
    </div>
"""

# Exibir o "card" no layout do Streamlit
st.markdown(card_style, unsafe_allow_html=True)
st.markdown(card_html, unsafe_allow_html=True)

st.sidebar.title("Filters")
