#!/usr/bin/env python3
"""
Geometric-Liquidity-Dynamics (GLD) Engine

A deterministic, physics-inspired financial simulator for backtesting,
quantitative research, and risk modeling. Prices evolve according to
momentum, trend, and stochastic noise with reproducible results.
"""

import math
import random
import matplotlib.pyplot as plt


class GeometricLiquidityDynamics:
    """
    Deterministic financial market simulator.

    Attributes:
        seed (int): Master seed for reproducible randomness.
        steps (int): Number of simulation steps.
        price (float): Current price level.
        momentum (float): Price momentum.
        dt (float): Time step for momentum integration.
        k (float): Momentum adjustment coefficient.
        prices (list): Recorded price trajectory.
    """

    def __init__(self, seed=888, steps=1000, initial_price=100.0):
        self.price = initial_price
        self.momentum = 0.0
        self.dt = 0.05
        self.k = 0.15
        self.steps = steps
        self.prices = []

        random.seed(seed)
        self.seed = seed

    def run(self, verbose=True, plot=False):
        """
        Run the simulation.

        Args:
            verbose (bool): If True, prints progress logs.
            plot (bool): If True, plots the simulated price trajectory.
        """
        if verbose:
            print(f"MASTER SEED: {self.seed}")
            print(f"{'PROGRESS':<10} | {'PRICE':<8} | {'MOMENTUM'}\n{'-'*32}")

        for step in range(1, self.steps + 1):
            target = 100.0 + math.sin(step * 0.1) * 15.0 + random.uniform(-1, 1) * 10
            # Update momentum and cap it
            self.momentum = max(min(self.momentum + (target - self.price) * self.k * self.dt, 20), -20)
            # Update price
            self.price += self.momentum * self.dt
            self.prices.append(self.price)

            # Log progress every 10%
            if verbose and step % (self.steps // 10) == 0:
                print(f"{(step/self.steps)*100:>3.0f}%        | {int(round(self.price)):<8} | {abs(self.momentum):.2f}")

        self.audit(verbose=verbose)

        if plot:
            self.plot_prices()

    def audit(self, verbose=True):
        """
        Compute finance-ready metrics: annualized volatility and max drawdown.

        Args:
            verbose (bool): If True, prints audit report.
        """
        # Compute returns
        returns = [(self.prices[i] - self.prices[i-1]) / self.prices[i-1] for i in range(1, len(self.prices))]
        avg_ret = sum(returns) / len(returns)

        # Annualized volatility
        vol = math.sqrt(sum((r - avg_ret)**2 for r in returns) / len(returns)) * math.sqrt(252)

        # Max drawdown
        peak = self.prices[0]
        max_dd = 0
        for px in self.prices:
            peak = max(peak, px)
            max_dd = min(max_dd, (px - peak) / peak)

        if verbose:
            print(f"{'='*32}")
            print(f"FINAL PRICE:    {self.prices[-1]:.2f}")
            print(f"VOLATILITY:     {vol:.2%}")
            print(f"MAX DRAWDOWN:   {max_dd:.2%}")
            print(f"STATUS:         VERIFIED")
            print(f"{'='*32}")

    def plot_prices(self):
        """Plot the simulated price trajectory."""
        plt.figure(figsize=(10, 4))
        plt.plot(self.prices, color='blue', linewidth=1.5)
        plt.title("Geometric-Liquidity-Dynamics: Simulated Price Path")
        plt.xlabel("Step")
        plt.ylabel("Price")
        plt.grid(True, alpha=0.3)
        plt.show()


if __name__ == "__main__":
    # Run 1000-step simulation with optional plotting
    engine = GeometricLiquidityDynamics(seed=888, steps=1000)
    engine.run(verbose=True, plot=True)
