import streamlit as st

# Menu Lateral Esquerdo

def menu_lateral():
    with st.sidebar:
        st.header("Teste")
        st.radio("Escolha uma opção", ["Opção 1", "Opção 2", "Opção 3"])