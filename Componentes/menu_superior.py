# IMPORTAR AS BIBLIOTECAS
import streamlit as st

# Menu Superior

def menu_superior():
    st.markdown(
        """
        <style>
        .stApp {
            padding-top: 140px;
        }
        .topbar {
            width: 100%;
            position: fixed;
            top: 50px;
            left: 0;
            z-index: 10;
            background-color: magenta;
        }
        .header {
            color: white;
            text-align: center;
            padding: 20px 0;
            font-size: 30px;
            font_weight: bold;
        }
        .menu-superior {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: magenta;
            padding: 10px 0;
            font-size: 18px;
            font-weight: bold;
            color: white;
        }
        .menu-superior a {
            color: white;
            text-decoration: none;
            margin: 0 20px;
        }
        .menu-superior a:hover {
            text-decoration: underline;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown('<div class="header">Menu Superior</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="topbar">'
        '<div class="header">Helena</div>'
        '<div class="menu-superior">'
        '<a href="#">Dashboard</a>'
        '<a href="#">Coletas</a>'
        '<a href="#">Ferramentas</a>'
        '</div>'
        '</div>', unsafe_allow_html=True
    )
