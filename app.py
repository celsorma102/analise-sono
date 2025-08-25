import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Análise do Sono", 
    layout="wide",
    page_icon="🛌")


df = pd.read_csv('https://raw.githubusercontent.com/celsorma102/analise-sono/refs/heads/main/dataset/dataset.csv')
