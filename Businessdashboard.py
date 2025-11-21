import streamlit as st

st.title("Business Dashboard with Streamlit Layouts")

# Markdown
msg = "Objective: To demonstrate the usage of columns, tabs, and dynamic containers in a business dashboard."
st.write(msg)

col1, col2 = st.columns(2)

with col1:
    st.header("Col 1")
with col2:
    st.header("Col 2")
