# Logic & Utility

## 1. Geometric Price Discovery
Traditional models exhibit numerical drift under high volatility. This engine uses **Symplectic Integration** to maintain price evolution on the information manifold.

- Price (`q`) deviates toward equilibrium (`Target`) according to **Manifold Stiffness** (`k`), generating mean-reverting oscillations consistent with observed asset behavior.

## 2. Momentum-Based Risk Management
Liquidity momentum is represented by `p`. Extreme events (e.g., flash crashes, short squeezes) cause momentum spikes.

- **Hard Momentum Clipping** (`±20`) enforces **Market Depth Limits**, preventing unbounded price changes and broken trades.

## 3. Deterministic Stress Testing
A **Master Seed** converts stochastic noise into a deterministic, reproducible sequence.

- **Backtesting:** 1,000 market scenarios generated via seed variation.  
- **Reproducibility:** Specific failure states can be recreated to calibrate `k` and `p`.

## 4. Quantitative Performance Metrics
The engine computes key risk metrics:

- **Annualized Volatility:** Standard deviation of returns scaled to a trading year.  
- **Max Drawdown (MDD):** Largest peak-to-trough capital decline.  
- **Symplectic Stability:** Verification of long-horizon numerical stability (1,000+ rounds).
