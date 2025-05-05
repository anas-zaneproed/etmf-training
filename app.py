import streamlit as st
from forms import siv_form

st.set_page_config(page_title="ZaneProEd | eTMF Training App")

st.title("ZaneProEd - Clinical Research eTMF Training")

# Sidebar Navigation
form_choice = st.sidebar.selectbox(
    "Choose a Form to Fill",
    ["-- Select Form --", "Site Initiation Visit Report"]
)

if form_choice == "Site Initiation Visit Report":
    siv_form.render_form()
