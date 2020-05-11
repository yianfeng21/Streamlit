import pandas as pd
import numpy as np
import datetime

<<<<<<< HEAD
df = pd.read_csv('/COVID-19/Data/20200507_download/OCHA/time_series_covid19_confirmed_global.csv')
=======
df = pd.read_csv('./Data/20200507_download/OCHA/time_series_covid19_confirmed_global.csv')
>>>>>>> try

df = df.iloc[:, 1:]
df_long = pd.melt(df, id_vars=df.columns[0:3], value_vars=df.columns[4:], var_name='Date', value_name='Number')
df_long['Date'] = [datetime.datetime.strptime(d, '%m/%d/%y') for d in df_long['Date']]
df_long['Date_str'] = [int(str(x)[0:10].replace("-","")) for x in df_long['Date']]

np.unique(df_long['Date_str']).tolist()

np.min(df_long['Date'])