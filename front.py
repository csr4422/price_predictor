import streamlit as st 
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go 
START ="2019-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title ("Stock Predictor")

stocks = ("AAPL","GOOG","MSFT","TSLA","TATAMOTORS.NS","ASIANPAINT.NS","IRFC.NS","UNIONBANK.NS")
selected_stocks = st.selectbox("Select dataset for prediction", stocks)

n_year =st.slider("Years of prediction:",1,4)
period = n_year *365

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker,START,TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Loading data ...")
data=load_data(selected_stocks)
data_load_state.text("Loading data...Done!")
st.subheader('Raw data')
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'],name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name='stock_CLose'))
    fig.layout.update(title_text="Time Series Data",xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()


