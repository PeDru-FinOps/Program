import streamlit as st

# Rodapé

def rodape():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #00E5B0;
            color: white;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown('<div class="footer"> Created by Pedro Drumond </div>', unsafe_allow_html=True)