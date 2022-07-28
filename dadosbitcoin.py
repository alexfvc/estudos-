import yfinance as yf


dados = yf.download("BTC", start = '2022-01-01', end = '2022-01-25')
print("dados BTC")
print(dados)