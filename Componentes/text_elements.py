import streamlit as st

# Título
st.title("Esse é um título")

# Subtítulo
st.subheader("Esse é um subtítulo")

# Caixa de texto
st.text("Pode ser utilizado para inserir parágrafos")

# Markdown
st.markdown("**Usei markdown pra fazer texto em negrito**")

# Caixa de código
st.code(
    """
    print("hello world!")
    """, language="python"
)