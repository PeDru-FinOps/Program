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

meter_category = base['MeterCategory'].unique()

# CRIAR A INTERFACE DO STREAMLIT

st.write(
    """
    # PROJETO HELENA

    Protótipo de um sistema customizado de controle de custos e gerenciamento Azure. O protótipo utilizará dados em repositório local.
    """
) #MARKDOWN

# Barra Lateral

st.sidebar.header("Filtros")

categorias = st.sidebar.multiselect(label="Categoria de Serviço", options = meter_category, default=[])

# Filtrando os dados com base na categoria selecionada

if categorias:
    base_filtrada = base[base['MeterCategory'].isin(categorias)]
else:
    base_filtrada = base

# Gráfico de Barra

grafico = base_filtrada.groupby('Date')['Cost'].sum()
st.bar_chart(grafico)

# st.bar_chart(meter_category.set_index("Date"))