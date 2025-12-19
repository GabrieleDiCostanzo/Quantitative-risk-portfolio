# Quantitative-risk-portfolio
Raccolta di modelli finanziari in Python per Risk Management, Pricing e Analisi Macro
# Quantitative Finance & Risk Management Portfolio 📊

Benvenuto nel mio portfolio di analisi quantitativa. Questo repository contiene strumenti sviluppati in Python per affrontare problemi reali di Pricing, Gestione del Rischio e Analisi Macroeconomica.

## 📂 Progetti Inclusi

### 1. Derivatives Pricing Engine (`Pricer.py`)
Un motore di calcolo per Opzioni Europee basato sul modello **Black-Scholes**.
* **Funzionalità:** Calcola il Fair Value e le Greche ($\Delta, \Gamma$) per l'hedging.
* **Output:** Genera un grafico della convessità (Gamma Risk) al variare del sottostante.

### 2. Yield Curve Simulator (`YieldCurve.py`)
Simulatore della struttura a termine dei tassi d'interesse (Fixed Income).
* **Modello:** Implementazione parametrica di **Nelson-Siegel**.
* **Obiettivo:** Visualizzare scenari di stress (inversione della curva) e monitorare lo spread 2Y-10Y come indicatore di recessione.

### 3. Cross-Asset Risk Monitor (`CorrelationRisk.py`)
Dashboard per il monitoraggio del rischio sistemico.
* **Dati:** Scarica dati reali di mercato (Yahoo Finance).
* **Analisi:** Calcola la correlazione mobile (Rolling Correlation) tra Equity (SPY) e Bond (TLT) per identificare quando la diversificazione di portafoglio fallisce.

### 4. Energy Seasonality Analyzer (`GasTrading.py`)
Tool per l'analisi dei mercati delle Commodity (Gas Naturale).
* **Analisi:** Confronta la curva dei prezzi attuali con la media storica a 10 anni per identificare trend stagionali.
* **Risk:** Mappa la volatilità mensile per ottimizzare il risk budgeting stagionale.

---
**Autore:** Gabriele Di Costanzo
*Studente Magistrale in Intermediari, Finanza Internazionale e Risk Management @ Sapienza Università di Roma*
