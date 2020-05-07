# Development flow
# Data flow

# --- (1) Drawing content --- #
import streamlit as st
x = 4
st.write(x, 'squared is', x * x)
# Magic!
x = 4
x, 'squared is', x * x

# --- (2) Widgets --- #
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# --- (3) Sidebar --- #
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# --- (4) Caching --- #
# The Streamlit cache allows your app to execute quickly even when loading data from the web,
# manipulating large datasets, or performing expensive computations.

# To use the cache, just wrap functions in the @st.cache decorator:
# @st.cache  # 👈 This function will be cached
# def my_slow_function(arg1, arg2):
#     # Do something really slow in here!
#     return the_output
