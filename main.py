# IMPORTAR AS BIBLIOTECAS
import streamlit as st
from Componentes.menu_superior import menu_superior
from Componentes.menu_lateral import menu_lateral
from Componentes.rodape import rodape

# Layout da Página

def pagina_principal():
    menu_superior()
    
    # Conteúdo principal da página
    st.title("Página Principal")
    st.write("Este é um exemplo de página com menu lateral, menu superior e rodapé utilizando Streamlit.")
    
    rodape()

pagina_principal()