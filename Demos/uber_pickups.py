# --- Tutorial: Create a data explorer app --- #
# - create an interactive app
# - exploring a public Uber dataset for pickups and drop-offs in New York City

# --- Demo --- #
# - terminal $ streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/app.py

import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

# --- (1) Fetch some data and Caching data --- #
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!')
data_load_state.text("Done! (using st.cache)")

# --- (2) Inspect the raw data --- #
# Use a button to toggle data
if st.checkbox('Show raw data'):
    st.subheader('Raw data') # 子標題
    st.write(data) # an interactive table

# --- (3) Draw a histogram --- #
st.subheader('Number of pickups by hour')
# Use NumPy to generate a histogram that breaks down pickup times binned by hour
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# --- (4) Plot data on a map --- #
# st.subheader('Map of all pickups')
# st.map(data)

# Filter results with a slider
hour_to_filter = st.slider('hour', 0, 23, 17) # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# 同上 st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data) # visualize complex map data：st.deckgl_chart
