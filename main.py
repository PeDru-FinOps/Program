# IMPORTAR AS BIBLIOTECAS
import streamlit as st
from Componentes.menu_superior import menu_superior
from Componentes.menu_lateral import menu_lateral
from Componentes.rodape import rodape

# Layout da Página

def pagina_principal():
    menu_superior()

    st.markdown(
        """
        <style>
        .inicio {
            text-align: center;
            font-size: 60px;
        }
        .imagem-centralizada {
            display: block;
            margin: 0 auto;
            width=300;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    # Conteúdo principal da página
    st.markdown('<div class="inicio"> Página Inicial </div>', unsafe_allow_html=True)

    image_url = "Designer.png"
    st.image(image_url, use_container_width=True, output_format='PNG')

    st.write("Este é um exemplo de página com menu lateral, menu superior e rodapé utilizando Streamlit.")
    
    rodape()

pagina_principal()