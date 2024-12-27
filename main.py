# IMPORTAR AS BIBLIOTECAS
import streamlit as st
from Componentes.rodape import rodape
from Pages.dash_custos import exibir_dash_custos

def main():
    st.sidebar.title("Helena")
    option = st.sidebar.selectbox(
        "",
        ("Home", "Dashboard", "Snapshots Antigos", "Discos Órfãos", "Máquinas Desligadas", "Funções"),
    )

    # Exibe o conteúdo com base na opção escolhida
    if option == "Dashboard":
        exibir_dash_custos()
    elif option == "Snapshots Antigos":
        "Teste"
    elif option == "Discos Órfãos":
        "Teste"
    elif option == "Máquinas Desligadas":
        "Teste"
    elif option == "Funções":
        "Teste"
    elif option == "Home":
        "Teste"

# Executa a aplicação Streamlit
if __name__ == "__main__":
    main()