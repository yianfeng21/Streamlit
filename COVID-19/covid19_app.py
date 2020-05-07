# --- Console --- #
import streamlit as st
import numpy as np
import pandas as pd

# title
st.title('COVID-19 Worldwide Situation')

# table
st.write("Global COVID-19 confirmed")
# @st.cache
df = pd.read_csv('/Users/ianfeng/Desktop/Python/Data_Viz/Streamlit/COVID-19/Data/20200507_download/OCHA/time_series_covid19_confirmed_global.csv')
df

