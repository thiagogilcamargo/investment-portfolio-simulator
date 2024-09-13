import yfinance as yf

def fetch_data(tickers, period='1y'):
    """
    Função para baixar os dados históricos de ativos usando yfinance.
    """
    data = yf.download(tickers, period=period)['Adj Close']
    return data
