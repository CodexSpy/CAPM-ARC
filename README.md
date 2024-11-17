# Capital Asset Pricing Model (CAPM)

This project implements the **Capital Asset Pricing Model (CAPM)** using stock data and the S&P 500 index. CAPM is a widely used financial model that estimates the expected return on an asset based on its risk relative to the market. This implementation provides a detailed analysis of stocks using real-time data, calculating key metrics such as beta, alpha, expected returns, Sharpe ratio, and volatility.

## Features

- **Stock Selection**: Choose multiple stocks from a predefined list.
- **Stock Price Visualization**: View normalized stock prices over a chosen period.
- **Risk and Return Analysis**: Calculate the beta, alpha, and expected return for each stock based on the CAPM formula.
- **Performance Metrics**: View performance metrics like the Sharpe ratio, volatility, and cumulative returns for the selected stocks.
- **Interactive Charts**: Interactive plots for stock prices, cumulative returns, and risk/return metrics.

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **Yahoo Finance API** (`yfinance`): For fetching stock price data.
- **Pandas**: For data manipulation and analysis.
- **Plotly**: For creating interactive charts and graphs.
- **Pandas DataReader**: For fetching financial data such as the S&P 500 index.
- **Python**: The primary language used for data processing and calculations.

## Requirements

To run this application locally, make sure you have the following Python packages installed:

- `streamlit`
- `pandas`
- `yfinance`
- `plotly`
- `pandas_datareader`

You can install these dependencies using the following command:

```bash
pip install streamlit pandas yfinance plotly pandas_datareader

```
## How to Run the App
Clone this repository to your local machine:

```bash
git clone https://github.com/CodexSpy/capm-project.git
cd capm-project
Install the required Python packages:
```
```bash
pip install -r requirements.txt
 ```
Run the Streamlit app:

```bash
streamlit run app.py
```
Open the application in your browser by navigating to the URL shown in the terminal (typically http://localhost:8501).

## Usage
- Select Stocks: Choose the stock tickers you are interested in analyzing.
- Investment Duration: Specify the number of years for which you want to calculate the CAPM metrics.
## Visualizations:
- View the normalized price plot for each stock.
- See cumulative returns for your selected stocks vs. S&P 500.
## CAPM Metrics:
- View the beta, alpha, and expected return for each stock.
- Evaluate the Sharpe ratio to measure the risk-adjusted returns.
- Volatility: Assess the annualized volatility of each stock.
## Key Metrics
- **Beta: A measure of a stock's volatility relative to the market. A beta greater than 1 indicates the stock is more volatile than the market.
- **Alpha: The difference between the actual return of a stock and its expected return based on its beta.
- **Expected Return: Calculated using the CAPM formula:
- **Expected Return = Risk-free Rate + Beta * (Market Return - Risk-free Rate)
- **Sharpe Ratio: A measure of risk-adjusted return. Higher values are better, indicating higher returns per unit of risk.
- **Volatility: The standard deviation of returns, measuring the variability of the stock price.
# Example Output
The app will provide the following:

- **Normalized stock price chart for the selected period.
- **Cumulative return comparison chart between selected stocks and the S&P 500.
- **A table with the calculated beta, alpha, and expected return for each stock.
- **Sharpe ratios and volatility for the selected stocks.

![image](https://github.com/CodexSpy/CAPM-ARC/blob/main/CAMP.png)
![image](https://github.com/CodexSpy/CAPM-ARC/blob/main/CAMP1.png)



## Acknowledgments
- Streamlit: For making it easy to build and share web apps for data science.
- yfinance: For providing an easy-to-use library for fetching stock data.
- Plotly: For enabling interactive data visualizations.

