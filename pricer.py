import numpy as np
import matplotlib.pyplot as plt # Importiamo il "pittore"
from scipy.stats import norm

# --- 1. IL MOTORE (Sempre lo stesso) ---
def risk_engine(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        price = (S * norm.cdf(d1)) - (K * np.exp(-r * T) * norm.cdf(d2))
    else:
        price = (K * np.exp(-r * T) * norm.cdf(-d2)) - (S * norm.cdf(-d1))
    return price

# --- 2. GENERAZIONE DEL GRAFICO ---
if __name__ == "__main__":
    # Parametri fissi
    K = 100
    T = 1.0
    r = 0.05
    sigma = 0.20

    # Genero 100 prezzi spot diversi: da 80 a 120
    # È come fare uno "Stress Test" simulando vari scenari di mercato
    spot_prices = np.linspace(80, 120, 100) 
    option_prices = []

    # Calcolo il prezzo dell'opzione per ogni scenario
    for S in spot_prices:
        p = risk_engine(S, K, T, r, sigma, 'call')
        option_prices.append(p)

    # Disegno il grafico
    plt.figure(figsize=(10, 6))
    plt.plot(spot_prices, option_prices, label='Prezzo Call Option', color='blue', linewidth=2)
    
    # Aggiungo linea dello Strike e del Payoff intrinseco (facoltativo, per bellezza)
    plt.axvline(x=K, color='red', linestyle='--', label='Strike Price (100€)')
    plt.grid(True, alpha=0.3)
    
    # Etichette
    plt.title('Profilo di Prezzo Call Option (Convessità)', fontsize=14)
    plt.xlabel('Prezzo del Sottostante (Spot)', fontsize=12)
    plt.ylabel('Prezzo Opzione (€)', fontsize=12)
    plt.legend()
    
    print("Grafico generato! Guarda la finestra che si è aperta.")
    plt.show()