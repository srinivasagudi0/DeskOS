from pathlib import Path

import streamlit as st


def render_css():
    css_path = Path(__file__).with_name("app.css")
    with css_path.open() as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


render_css()


st.title("DeskOS")

st.markdown("""
    <br />
    <hr />
            """, unsafe_allow_html=True)

left, middle, right = st.columns(3)

with left: 
    container = st.container(border=True)
    with container:
        st.write("This is the left column.")
