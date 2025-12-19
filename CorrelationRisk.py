import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# --- 1. SCARICO DATI REALI ---
print("Scaricamento dati in corso da Yahoo Finance... (attendere)")

# Ticker: SPY (ETF S&P 500), TLT (ETF US Treasury 20+ Year)
tickers = ['SPY', 'TLT']
start_date = '2020-01-01'

# FIX PER NUOVA VERSIONE YFINANCE:
# auto_adjust=True è ora il default, quindi usiamo la colonna 'Close' 
# che contiene già i prezzi rettificati.
data = yf.download(tickers, start=start_date, progress=False)['Close']

# --- 2. CALCOLO RENDIMENTI E CORRELAZIONE ---
# Calcolo i rendimenti percentuali giornalieri
returns = data.pct_change().dropna()

# Calcolo la Rolling Correlation (Finestra mobile di 60 giorni ~ 3 mesi)
rolling_corr = returns['SPY'].rolling(window=60).corr(returns['TLT'])

# --- 3. VISUALIZZAZIONE RISCHIO ---
plt.figure(figsize=(12, 6))

# Disegno la correlazione
plt.plot(rolling_corr.index, rolling_corr, label='Rolling Correlation (SPY vs TLT)', color='purple', linewidth=1.5)

# Linea dello zero
plt.axhline(0, color='black', linestyle='--', linewidth=1)

# Coloro le aree (Rischio vs Safe)
plt.fill_between(rolling_corr.index, 0, rolling_corr, where=(rolling_corr > 0), color='red', alpha=0.3, label='RISCHIO: Correlazione Positiva (Stocks & Bonds giù insieme)')
plt.fill_between(rolling_corr.index, 0, rolling_corr, where=(rolling_corr < 0), color='green', alpha=0.3, label='SAFE: Diversificazione Efficace')

# Titoli e legende
plt.title('Risk Monitor: Analisi Correlazione (Equity vs Bond)', fontsize=14)
plt.ylabel('Correlazione (Rolling 60gg)', fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)

print(f"Dati scaricati fino a oggi.")
print("Grafico generato! Se vedi rosso nel 2022/2023, il modello funziona.")
plt.show()