import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# --- 1. PRICING ENGINE (Black-Scholes Model) ---
def risk_engine(S, K, T, r, sigma, option_type='call'):
    """
    Calculates Option Price and Greeks (Delta, Gamma).
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        price = (S * norm.cdf(d1)) - (K * np.exp(-r * T) * norm.cdf(d2))
        delta = norm.cdf(d1)
    else:
        price = (K * np.exp(-r * T) * norm.cdf(-d2)) - (S * norm.cdf(-d1))
        delta = norm.cdf(d1) - 1
        
    # Gamma (Same for Call and Put)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    
    return price, delta, gamma

# --- 2. MAIN EXECUTION ---
if __name__ == "__main__":
    # Market Parameters
    spot_example = 100  # Current Spot Price
    strike = 100
    expiry = 1.0        # 1 Year
    rate = 0.05         # 5% Risk-free rate
    vol = 0.20          # 20% Volatility

    # A. SINGLE POINT CALCULATION (For Console Output)
    price, delta, gamma = risk_engine(spot_example, strike, expiry, rate, vol, 'call')

    # B. SIMULATION FOR PLOTTING (Gamma/Convexity View)
    spot_range = np.linspace(80, 120, 100)
    option_prices = []
    
    for S in spot_range:
        p, d, g = risk_engine(S, strike, expiry, rate, vol, 'call')
        option_prices.append(p)

    # --- 3. PROFESSIONAL OUTPUT ---
    print(f"--- BLACK-SCHOLES PRICING REPORT ---")
    print(f"Underlying: {spot_example} | Strike: {strike}")
    print(f"Maturity:   {expiry} Yr  | Volatility: {vol:.1%}")
    print(f"------------------------------------")
    print(f"Fair Value: {price:.4f} EUR")
    print(f"Delta:      {delta:.4f}")
    print(f"Gamma:      {gamma:.4f}")
    print(f"------------------------------------")
    print("Generating Convexity Plot...")

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(spot_range, option_prices, label='Call Option Value', color='blue', linewidth=2)
    plt.axvline(x=strike, color='red', linestyle='--', alpha=0.5, label='Strike Price')
    
    plt.title('Derivatives Pricing: Payoff & Convexity Profile', fontsize=14)
    plt.xlabel('Underlying Spot Price', fontsize=12)
    plt.ylabel('Option Theoretical Value', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.show()