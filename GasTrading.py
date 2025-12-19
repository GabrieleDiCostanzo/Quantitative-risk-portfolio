import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns # Libreria per grafici statistici (la installiamo se manca)

# --- 1. SETUP DATI ---
print("Scaricamento dati Gas Naturale (Henry Hub Futures)...")
ticker = "NG=F"
data = yf.download(ticker, start="2015-01-01", progress=False)['Close']

# Creiamo un DataFrame più gestibile
df = pd.DataFrame(data)
df.columns = ['Price']

# Estraggo Mese e Anno dalla data
df['Month'] = df.index.month
df['Year'] = df.index.year

# --- 2. ANALISI STAGIONALITÀ ---
# Calcolo il prezzo medio per ogni mese (su tutti gli anni dal 2015 a oggi)
seasonal_avg = df.groupby('Month')['Price'].mean()

# Isolo i dati dell'ultimo anno completo (es. 2024 o 2025) per confronto
current_year = 2024
current_year_data = df[df['Year'] == current_year].groupby('Month')['Price'].mean()

# --- 3. ANALISI VOLATILITÀ (Risk Management) ---
# Calcolo la volatilità media per ogni mese
monthly_volatility = df.groupby('Month')['Price'].std()

# --- 4. GRAFICO PROFESSIONALE ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10)) # Creo 2 grafici uno sopra l'altro

# GRAFICO 1: Stagionalità Prezzi
ax1.plot(seasonal_avg.index, seasonal_avg, label='Media Storica (10 Anni)', color='blue', linewidth=2, linestyle='--')
ax1.plot(current_year_data.index, current_year_data, label=f'Anno {current_year}', color='orange', linewidth=3)
ax1.set_title('Gas Seasonality: Prezzo Attuale vs Media Storica', fontsize=14)
ax1.set_ylabel('Prezzo ($/MMBtu)', fontsize=12)
ax1.set_xticks(range(1, 13))
ax1.set_xticklabels(['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic'])
ax1.legend()
ax1.grid(True, alpha=0.3)

# GRAFICO 2: Volatilità Mensile (Quando è pericoloso fare trading?)
ax2.bar(monthly_volatility.index, monthly_volatility, color='red', alpha=0.6)
ax2.set_title('Risk Monitor: Volatilità Storica per Mese', fontsize=14)
ax2.set_ylabel('Deviazione Standard ($)', fontsize=12)
ax2.set_xticks(range(1, 13))
ax2.set_xticklabels(['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic'])
ax2.grid(True, axis='y', alpha=0.3)

plt.tight_layout()
print("Analisi completata. Guarda come i prezzi si muovono d'inverno!")
plt.show()