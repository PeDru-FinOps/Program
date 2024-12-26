# IMPORTAR AS BIBLIOTECAS
import streamlit as st
import pandas as pd

# CRIAR FUNÇÕES DE CARREGAMENTO DE DADOS

# Atribui uma funcionalidade ao item abaixo deste Decorator. No caso, sempre que possível essas informações ficarão em cache.
@st.cache_data 
def carregar_dados_atuais():
    dados_empresa = pd.read_csv("Clientes/Simpar/Novembro - Amortized.csv", on_bad_lines='warn', delimiter=',')
    return dados_empresa

# PREPARAR AS VISUALIZAÇÕES

base = carregar_dados_atuais()

custo_diario = base.groupby("Date")["Cost"].sum().reset_index()
custo_diario_categoria = base.groupby(["Date", "MeterCategory"])["Cost"].sum().unstack().fillna(0)

# CRIAR A INTERFACE DO STREAMLIT

st.write(
    """
    # PROJETO HELENA

    Protótipo de um sistema customizado de controle de custos e gerenciamento Azure. O protótipo utilizará dados em repositório local.
    """
) #MARKDOWN

st.bar_chart(custo_diario.set_index("Date"))

st.bar_chart(custo_diario_categoria)