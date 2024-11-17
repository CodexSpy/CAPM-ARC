import datetime as dt
import streamlit as st
import pandas as pd
import yfinance as yf
import pandas_datareader.data as pdr
import CAPM_charts as graphs
import price_normalize as pn
import returns
import plotly.graph_objects as go

def normalized_price_plot(data):
    fig = go.Figure()
    for col in data.columns[1:]:
        fig.add_trace(go.Scatter(x=data['Date'], y=data[col], mode='lines', name=col))
    fig.update_layout(title="Normalized Prices", xaxis_title="Date", yaxis_title="Normalized Price")
    return fig

# Function to plot cumulative returns
def cumulative_returns_plot(data):
    fig = go.Figure()
    for col in data.columns:
        fig.add_trace(go.Scatter(x=data.index, y=data[col], mode='lines', name=col))
    fig.update_layout(title="Cumulative Returns", xaxis_title="Date", yaxis_title="Cumulative Return (%)", width=1420,
        height=500,
        autosize=True,
        margin=dict(
            l=50,
            r=50,
            t=50,
            b=50
        ),
        )
    return fig

st.set_page_config(page_title="CAPM", page_icon=":dollar:", layout="wide")

st.title("Capital Asset Pricing Model 💰")
st.markdown(
    '###### Made By Moin Khan | [🔗 Github](https://github.com/CodexSpy) | [🔗 Portfolio website](https://moin-port-folio.vercel.app/)'
)
st.caption(
    "The Capital Asset Pricing Model (CAPM) is a financial model that describes the relationship between the expected return on an investment and its associated risk. It is widely used in finance to estimate the return an investor should expect for taking on a particular level of risk, as compared to a risk-free investment"
)
st.subheader("Assumed risk-free return = 4.5%")

# Inputs
col1, col2 = st.columns([1, 1])
col3, col4 = st.columns([1, 1])

with col1:
    stock_list = st.multiselect(
        "Choose stocks by ticker",
        (
            'AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOGL', 'TSLA', 'META', 'GOOG', 'BRK',
            'UNH', 'XOM', 'JNJ', 'JPM', 'V', 'LLY', 'AVGO', 'PG', 'MA', 'HD', 'MRK',
            'CVX', 'PEP', 'COST', 'ABBV', 'KO', 'ADBE', 'WMT', 'MCD', 'CSCO', 'PFE',
            'CRM', 'TMO', 'BAC', 'NFLX', 'ACN', 'A', 'DE', 'GS', 'ELV', 'LMT', 'AXP',
            'BLK', 'SYK', 'BKNG', 'MDLZ', 'ADI', 'TJX', 'GILD', 'MMC', 'ADP', 'VRTX',
            'AMT', 'C', 'CVS', 'LRCX', 'SCHW', 'CI', 'MO', 'ZTS', 'TMUS', 'ETN', 'CB',
            'FI'
        ),
        ('AAPL', 'TSLA', 'AMZN', 'GOOGL')
    )

with col2:
    year = st.number_input("Years of investment", 1, 10)

# Download S&P 500 data from FRED using pdr
try:
    end = dt.date.today()
    start = dt.date(end.year - year, end.month, end.day)

    sp500_data = pdr.DataReader('sp500', 'fred', start, end)
    sp500_data.reset_index(inplace=True)
    sp500_data.columns = ['Date', 'sp500']
    sp500_data['Date'] = pd.to_datetime(sp500_data['Date']).dt.tz_localize(None)

    # Prepare stock data
    stocks_df = pd.DataFrame()

    for stock in stock_list:
        data = yf.download(stock, period=f'{year}y')
        stocks_df[f'{stock}'] = data['Close']

    stocks_df.reset_index(inplace=True)
    stocks_df['Date'] = pd.to_datetime(stocks_df['Date']).dt.tz_localize(None)

    # Merge data
    stocks_df = pd.merge(stocks_df, sp500_data, on='Date', how='inner')

    # Display stock data
    with col1:
        st.markdown("### Stock Prices (Head)")
        st.dataframe(stocks_df.head(), use_container_width=True, hide_index=True)

    with col2:
        st.markdown("### Stock Prices (Tail)")
        st.dataframe(stocks_df.tail(), use_container_width=True, hide_index=True)

    # Normalized price graph
    with col1:
        st.markdown("### Normalized Prices")
        st.caption("Prices normalized to initial stock prices")
        stocks_df_normalized = pn.normalized(stocks_df)
        st.plotly_chart(graphs.interactive_plot(stocks_df_normalized))

    # Calculate daily returns and CAPM metrics
    stocks_daily_return = returns.daily_returns(stocks_df)

    # Calculate beta and alpha
    beta = {}
    alpha = {}

    for i in stocks_daily_return.columns:
        if i != 'Date' and i != 'sp500':
            b, a = returns.beta(stocks_daily_return, i)
            beta[i] = b
            alpha[i] = a

    beta_df = pd.DataFrame({'Stock': beta.keys(), 'Beta Value': [round(b, 2) for b in beta.values()]})

    with col3:
        st.markdown("### Calculated Risk (Beta Values)")
        st.caption("Market risk is considered as 1")
        st.dataframe(beta_df, use_container_width=True, hide_index=True)

    # Calculate expected returns using CAPM
    risk_free_asset = 4.5
    market_return = stocks_daily_return['sp500'].mean() * 252  # 252 trading days
    return_values = [round(risk_free_asset + b * (market_return - risk_free_asset), 2) for b in beta.values()]
    return_df = pd.DataFrame({'Stock': beta.keys(), 'Expected Return': return_values})

    with col4:
        st.markdown("### Calculated Return using CAPM")
        st.caption("Formula: risk-free rate + beta * (market return - risk-free rate)")
        st.dataframe(return_df, use_container_width=True, hide_index=True)

    # Sharpe Ratio Calculation
    sharpe_ratios = {}
    for stock in stock_list:
        stock_returns = stocks_daily_return[stock]
        risk_free_rate = risk_free_asset / 100
        sharpe_ratios[stock] = (stock_returns.mean() * 252 - risk_free_rate) / (stock_returns.std() * (252 ** 0.5))

    sharpe_df = pd.DataFrame({'Stock': sharpe_ratios.keys(), 'Sharpe Ratio': [round(r, 2) for r in sharpe_ratios.values()]})
    

    with col4:
        st.markdown("### Sharpe Ratio")
        st.caption("Risk-adjusted return of stocks")
        st.dataframe(sharpe_df, use_container_width=True, hide_index=True)

   
    # Cumulative Return Comparison
    st.markdown("### Cumulative Returns Comparison")
    cumulative_returns = (stocks_df.drop('Date', axis=1) / stocks_df.drop('Date', axis=1).iloc[0] - 1) * 100
    cumulative_returns['S&P 500'] = (sp500_data['sp500'] / sp500_data['sp500'].iloc[0] - 1) * 100
    st.plotly_chart(cumulative_returns_plot(cumulative_returns))

    # Volatility Calculation
    volatilities = {}
    for stock in stock_list:
        volatilities[stock] = stocks_daily_return[stock].std() * (252 ** 0.5)  # Annualized volatility

    volatility_df = pd.DataFrame({'Stock': volatilities.keys(), 'Volatility (Std Dev)': [round(v, 2) for v in volatilities.values()]})

    with col1:
        st.markdown("### Stock Volatility")
        st.caption("Annualized standard deviation of daily returns")
        st.dataframe(volatility_df, use_container_width=True, hide_index=True)

    # Performance Metrics Overview
    performance_df = pd.DataFrame({
        'Stock': beta.keys(),
        'Beta': [round(b, 2) for b in beta.values()],
        'Expected Return': return_values,
        'Sharpe Ratio': [sharpe_ratios.get(stock, 'N/A') for stock in beta.keys()],
        'Volatility': [volatilities.get(stock, 'N/A') for stock in beta.keys()]
    })

    with col3:
        st.markdown("### Performance Overview")
        st.dataframe(performance_df, use_container_width=True, hide_index=True)

except Exception as e:
    st.error(f"An error occurred: {e}")


# Hide Streamlit footer and menu
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden;}
       footer {visibility: hidden;}   
       .footer {
           background-color: #4F46E5; 
           padding: 5px 0;
           color: white;
           text-align: center;
           font-family: Arial, sans-serif;
           position: fixed;
           bottom: 0;
           width: 100%;
           left: 0;
       }
       .footer a {
           color: #ffffff;
           text-decoration: none;
           font-weight: bold;
       }
       .footer a:hover {
           text-decoration: underline;
       }
       
      
       </style>
       <div class="footer">
           <p>Made with ❤️ by Moin Khan | <a href="https://github.com/CodexSpy" target="_blank">GitHub</a> | <a href="https://moin-port-folio.vercel.app/" target="_blank">Portfolio</a></p>
       </div>
"""

st.markdown(hide_default_format, unsafe_allow_html=True)