import streamlit as st
import pandas as pd
import numpy as np

st.title("streamlit hello")
st.write("AirBNB New York 2019 Dataset")


st.write("#1 Some columns wrong type: id, host_id, last_review")
df = pd.read_csv("https://github.com/bankmanx9x/portfolio/blob/main/01%20airbnb_original.csv?raw=true")

st.dataframe(df.head())


st.write("#2 Convert data type")
df2 = pd.read_csv("https://github.com/bankmanx9x/portfolio/blob/main/01%20airbnb_original.csv?raw=true", parse_dates=['last_review'])
df2['id'] = df2['id'].astype(str)
df2['host_id'] = df2['host_id'].astype(str)

st.dataframe(df2.head())
