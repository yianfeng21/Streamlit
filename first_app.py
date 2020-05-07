# --- Terminal --- #
# View the app ： streamlit run first_app.py
# Kill the app ： "Ctrl+c"

# --- Console --- #
import streamlit as st
import numpy as np
import pandas as pd

# --- (1) Add text and data --- #
# Add a title
st.title('My first app')

# Write a data frame
# st.dataframe(), st.table()
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# --- (2) Use magic --- #
# magic commands for Python 3
st.write("Use Magic")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df

# --- (3) Draw charts and maps --- #
# Draw a line chart
st.write("Line Chart")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# Plot a map --San Francisco
st.write("Map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

# --- (4) Add interactivity with widgets --- #
# Use checkboxes to show/hide data
st.write("show/hide data")
if st.checkbox('Show the chart'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

# # Use a selectbox for options
# st.write("options")
# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])
#
# 'You selected: ', option

# Put widgets in a sidebar
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option

# --- (5) Show progress --- #
import time

'Starting a long computation...'
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'


# 參考網址：
# Streamlit DOCUMENTATION --Get started
# https://docs.streamlit.io/getting_started.html