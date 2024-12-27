import streamlit as st
import pandas as pd
import os

def listar_arquivos_clientes(diretorio):
    try:
        arquivos = os.listdir(diretorio)
        for arquivo in arquivos:
            print(arquivo)
    except FileNotFoundError:
        print(f"Diretório não encontrado: {diretorio}")
    except PermissionError:
        print(f"Permissão negada para acessar: {diretorio}")
    return arquivos