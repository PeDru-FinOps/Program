import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Componentes.listar_arquivos import listar_arquivos_clientes

st.set_option('server.maxMessageSize', 350)

# Definir o diretório

diretorio = "Clientes/Simpar"

arquivos = listar_arquivos_clientes(diretorio)

selecao = st.selectbox("Selecione o arquivo:", arquivos)

path_arquivo = os.path.join(diretorio, selecao)

df_simpar = pd.read_csv(f"{path_arquivo}", on_bad_lines='warn', delimiter=',')

st.table(df_simpar.head())