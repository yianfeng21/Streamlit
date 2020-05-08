# --- Console --- #
import streamlit as st
import pandas as pd
import numpy as np
import datetime

# path
file_path = "/Users/ianfeng/Desktop/Python/Data_Viz/Streamlit/COVID-19/"

import io
def get_file_content_as_string(path):
    with io.open(path, 'r', encoding='utf8') as f:
        text = f.read()
    return text

# 主頁
def main():
    # Render the readme as markdown using st.markdown.
    readme_text = st.markdown(get_file_content_as_string(file_path+"instructions.md"))

    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Show instructions", "Run the app", "Show the source code"])
    if app_mode == "Show instructions":
        st.sidebar.success('Care about the World')
        # Add a pic
        st.image("/Users/ianfeng/Desktop/Python/Data_Viz/Streamlit/COVID-19/Slide/colin-d--ptNfxSHJW8-unsplash.jpg",
                 width=700)
    elif app_mode == "Run the app":
        readme_text.empty()
        run_the_app()
    elif app_mode == "Show the source code":
        readme_text.empty()
        st.code(get_file_content_as_string(file_path+"covid19_app.py"))

@st.cache
def load_data(csv):
    return pd.read_csv(csv)
df_confirmed = load_data('/Users/ianfeng/Desktop/Python/Data_Viz/Streamlit/COVID-19/Data/20200507_download/OCHA/time_series_covid19_confirmed_global.csv')
df_deaths = load_data('/Users/ianfeng/Desktop/Python/Data_Viz/Streamlit/COVID-19/Data/20200507_download/OCHA/time_series_covid19_deaths_global.csv')
df_recovered = load_data('/Users/ianfeng/Desktop/Python/Data_Viz/Streamlit/COVID-19/Data/20200507_download/OCHA/time_series_covid19_recovered_global.csv')

def run_the_app():
    # title
    st.title('COVID-19 Worldwide Situation')

    options = st.selectbox(
        'Please choose data type',
        ('Confirmed', 'Deaths', 'Recovered'))
    if options == "Confirmed":
        viz_app(df_confirmed)
    elif options == "Deaths":
        viz_app(df_deaths)
    elif options == "Recovered":
        viz_app(df_recovered)

def viz_app(df):

    df = df.iloc[:, 1:]
    df_long = pd.melt(df, id_vars=df.columns[0:3], value_vars=df.columns[4:], var_name='Date', value_name='Number')
    df_long['Date'] = [datetime.datetime.strptime(d, '%m/%d/%y') for d in df_long['Date']]
    df_long['Date_str'] = [int(str(x)[0:10].replace("-","")) for x in df_long['Date']]
    # Filter Date
    date_to_filter = st.date_input('Date: 2020-01-23 ~ 2020-05-06', np.max(df_long['Date']))
    filtered_data = df_long[df_long['Date'] == date_to_filter]
    # Map
    st.map(filtered_data)  # visualize complex map data：st.deckgl_chart

    # table
    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(df)

if __name__ == "__main__":
    main()