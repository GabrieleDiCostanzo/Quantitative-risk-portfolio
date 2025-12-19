import numpy as np
import matplotlib.pyplot as plt

# --- 1. IL MODELLO NELSON-SIEGEL ---
def nelson_siegel(tau, b0, b1, b2, lam):
    """
    Calcola il tasso di interesse per una data scadenza (tau).
    Formula standard usata dalle Banche Centrali.
    
    tau: Scadenza in anni (es. 10)
    b0:  Livello a lungo termine (Long term)
    b1:  Pendenza breve termine (Short term / Slope)
    b2:  Curvatura (Medium term / Curvature)
    lam: Fattore di decadimento (Decay factor)
    """
    term1 = (1 - np.exp(-tau / lam)) / (tau / lam)
    term2 = term1 - np.exp(-tau / lam)
    
    yield_val = b0 + (b1 * term1) + (b2 * term2)
    return yield_val * 100  # Moltiplico per 100 per avere la %

# --- 2. SETUP DELLA SIMULAZIONE ---
# Creiamo le scadenze standard: da 3 mesi (0.25 anni) a 30 anni
maturities = np.linspace(0.25, 30, 100)

# SCENARIO A: Mercato Normale (Curva inclinata positivamente)
# Tassi bassi a breve, alti a lungo.
y_normal = nelson_siegel(maturities, b0=0.04, b1=-0.02, b2=-0.01, lam=2.0)

# SCENARIO B: Mercato in Crisi/Recessione (Curva Invertita)
# Tassi alti a breve (Banca Centrale alza i tassi), bassi a lungo (pessimismo).
y_inverted = nelson_siegel(maturities, b0=0.025, b1=0.03, b2=-0.02, lam=1.0)

# --- 3. GENERAZIONE GRAFICO ---
plt.figure(figsize=(10, 6))

# Disegno le due curve
plt.plot(maturities, y_normal, label='Scenario Normale (Espansione)', color='green', linewidth=2.5)
plt.plot(maturities, y_inverted, label='Scenario Invertito (Rischio Recessione)', color='red', linewidth=2.5, linestyle='--')

# Abbellimenti grafici
plt.title('Yield Curve Simulator: Nelson-Siegel Model', fontsize=14)
plt.xlabel('Scadenza (Anni)', fontsize=12)
plt.ylabel('Tasso di Interesse (%)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

# Evidenzio lo spread 2Y-10Y (Classico indicatore di rischio)
plt.axvline(x=2, color='gray', linestyle=':', alpha=0.5)
plt.axvline(x=10, color='gray', linestyle=':', alpha=0.5)
plt.text(10.5, 1.0, "Spread 10Y-2Y monitorato", fontsize=10, color='gray')

print("Generazione grafico Curve dei Tassi completata...")
plt.show()