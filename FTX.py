import json
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
df = requests.get('https://ftx.us/api/markets/CUSDT/USDT/trades?start_time=0000000000&end_time=9999999999').json()
df = pd.DataFrame(df['result'])
df.head()
st.write("FTX US cUSDT-USDT")

st.write(df)
t_f = False
st.sidebar.write("Choose y-axis scale")
check = st.sidebar.checkbox("Linear/Log")
if check:
    t_f = True
df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "time",
    y = "price",
    orientation = "v",
    color = "side",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = requests.get('https://ftx.us/api/markets/CUSDT/USD/trades?start_time=0000000000&end_time=9999999999').json()
df = pd.DataFrame(df['result'])
df.head()
st.write("FTX US cUSDT-USD")

st.write(df)

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "time",
    y = "price",
    orientation = "v",
    color = "side",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = requests.get('https://ftx.com/api/markets/CUSDT/USDT/trades?start_time=0000000000&end_time=9999999999').json()
df = pd.DataFrame(df['result'])
df.head()
st.write("FTX cUSDT-USDT")

st.write(df)

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "time",
    y = "price",
    orientation = "v",
    color = "side",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)



df = requests.get('https://ftx.com/api/markets/CUSDT/USD/trades?start_time=0000000000&end_time=9999999999').json()
df = pd.DataFrame(df['result'])
df.head()
st.write("FTX cUSDT-USD")

st.write(df)

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "time",
    y = "price",
    orientation = "v",
    color = "side",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = requests.get('https://ftx.com/api/markets/CUSDT-PERP/trades?start_time=0000000000&end_time=9999999999').json()
df = pd.DataFrame(df['result'])
df.head()
st.write("FTX cUSDT-PERP")

st.write(df)

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "time",
    y = "price",
    orientation = "v",
    color = "side",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = requests.get('https://ftx.com/api/markets/USDT/USD/trades?start_time=0000000000&end_time=9999999999').json()
df = pd.DataFrame(df['result'])
df.head()
st.write("FTX USDT-USD")

st.write(df)

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "time",
    y = "price",
    orientation = "v",
    color = "side",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = requests.get('https://ftx.us/api/markets/USDT/USD/trades?start_time=0000000000&end_time=9999999999').json()
df = pd.DataFrame(df['result'])
df.head()
st.write("FTX_US USDT-USD")

st.write(df)

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "time",
    y = "price",
    orientation = "v",
    color = "side",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
# https://ftx.us/api/markets/CUSDT-PERP/trades?start_time=0000000000&end_time=9999999999
# 15, 60, 300, 900, 3600, 14400, 86400
df = requests.get('https://ftx.com/api/markets/CUSDT-PERP/candles?resolution=14400').json()
df = pd.DataFrame(df['result'])
df.head()
st.write("FTX cUSDT Perp")

st.write(df)

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ['high','low'],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = requests.get('https://ftx.com/api/markets/CUSDT/USDT/candles?resolution=14400').json()
df = pd.DataFrame(df['result'])
df.head()
st.write("FTX cUSDT USDT")

st.write(df)

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ['high','low'],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = requests.get('https://ftx.us/api/markets/CUSDT/USDT/candles?resolution=14400').json()
df = pd.DataFrame(df['result'])
df.head()
st.write("FTX US cUSDT USDT")

st.write(df)

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ['high','low'],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = requests.get('https://ftx.us/api/markets/CUSDT/USD/candles?resolution=14400').json()
df = pd.DataFrame(df['result'])
df.head()
st.write("FTX US cUSDT USD")

st.write(df)

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ['high','low'],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)




query_id = "e9b9351a-7cfc-41a6-b217-d8f0d477424e"
df_y = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_y)
df_y = px.scatter(
    df_y, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = ['MIN(RATE)','MAX(RATE)','AVG(RATE)','MEDIAN(RATE)'],
    orientation = "v",
    # color = "LABEL",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df_y)

df = requests.get('https://ftx.com/api/markets/CUSDT/USDT/candles?resolution=86400&start_time=1623110400').json()

df = pd.DataFrame(df['result'])
st.write("FTX cUSDT USDT")

st.write(df)

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ['open','close','high','low'],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)


st.write("compare")
df = requests.get('https://ftx.com/api/markets/CUSDT/USDT/candles?resolution=86400&start_time=1623110400').json()

df = pd.DataFrame(df['result'])
st.write("FTX cUSDT USDT")
query_id = "e9b9351a-7cfc-41a6-b217-d8f0d477424e"
df_y = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_y)
st.write(df)

df_merge_1 = pd.merge(df , df_y , left_index=True, right_index=True)
# df_merge_1 = pd.merge(df, df_y, right_on = 'DAYZ')
st.write(df_merge_1)
df_merge_p = px.scatter(
    df_merge_1, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ['high','low','MIN(RATE)','MAX(RATE)','AVG(RATE)','MEDIAN(RATE)'],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df_merge_p)

df_merge_1['upper_spread'] = (df_merge_1['high'] - df_merge_1['AVG(RATE)'])/df_merge_1['AVG(RATE)']
df_merge_1['lower_spread'] = (df_merge_1['AVG(RATE)'] - df_merge_1['low'])/df_merge_1['AVG(RATE)']
df_merge_1['bid_ask_spread'] = (df_merge_1['high'] - df_merge_1['low'])/df_merge_1['high']
df_merge_pp = px.scatter(
    df_merge_1, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ["bid_ask_spread"],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df_merge_pp)
df_merge_ppp = px.scatter(
    df_merge_1, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ["upper_spread"],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df_merge_ppp)
df_merge_pppp = px.scatter(
    df_merge_1, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ["lower_spread"],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df_merge_pppp)



df2 = requests.get('https://ftx.com/api/markets/CUSDT-PERP/candles?resolution=86400&start_time=1623110400').json()
df2 = pd.DataFrame(df2['result'])
st.write("FTX cUSDT Perp")
query_id = "e9b9351a-7cfc-41a6-b217-d8f0d477424e"
df_y = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)
df_merge_2 = pd.merge(df_y, df2 , left_index=True, right_index=True)

st.write(df_merge_2)

df3 = px.scatter(
    df_merge_2, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ['high','low','AVG(RATE)'],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df3)

df_merge_2['upper_spread'] = (df_merge_2['high'] - df_merge_2['AVG(RATE)'])/df_merge_2['AVG(RATE)']
df_merge_2['lower_spread'] = (df_merge_2['AVG(RATE)'] - df_merge_2['low'])/df_merge_2['AVG(RATE)']
df_merge_2['bid_ask_spread'] = (df_merge_2['high'] - df_merge_2['low'])/df_merge_2['high']
df_merge_pp = px.scatter(
    df_merge_2, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ["bid_ask_spread"],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df_merge_pp)
df_merge_ppp = px.scatter(
    df_merge_2, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ["upper_spread"],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df_merge_ppp)
df_merge_pppp = px.scatter(
    df_merge_2, #this is the dataframe you are trying to plot
    x = "startTime",
    y = ["lower_spread"],
    orientation = "v",
    # color = "volume",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df_merge_pppp)





# https://ftx.us/api/markets/USDT/USD/candles?resolution=15&start_time=0000000000&end_time=9999999999
# https://ftx.us/api/markets/USDT/USD/candles?resolution=60&start_time=0000000000&end_time=9999999999
# https://ftx.us/api/markets/USDT/USD/candles?resolution=300&start_time=0000000000&end_time=9999999999
# https://ftx.us/api/markets/USDT/USD/candles?resolution=900&start_time=0000000000&end_time=9999999999
# https://ftx.us/api/markets/USDT/USD/candles?resolution=3600&start_time=0000000000&end_time=9999999999
# https://ftx.us/api/markets/USDT/USD/candles?resolution=14400&start_time=0000000000&end_time=9999999999
# https://ftx.us/api/markets/USDT/USD/candles?resolution=86400&start_time=0000000000&end_time=9999999999
