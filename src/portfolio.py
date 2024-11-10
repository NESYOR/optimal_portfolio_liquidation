# src/portfolio.py

import numpy as np

class Portfolio:
    def __init__(self, initial_holdings, initial_price, transaction_cost):
        self.holdings = initial_holdings  # initial asset quantity
        self.initial_price = initial_price  # initial price per asset
        self.transaction_cost = transaction_cost  # cost per transaction

    def geometric_brownian_motion(self, steps, dt, mu=0.05, sigma=0.2):
        """
        Simulates asset price path using geometric Brownian motion.
        
        Parameters:
            steps (int): Number of time steps to simulate.
            dt (float): Time increment.
            mu (float): Drift coefficient (mean return).
            sigma (float): Volatility of the asset.

        Returns:
            numpy.ndarray: Simulated price path.
        """
        price_path = [self.initial_price]
        for _ in range(steps):
            prev_price = price_path[-1]
            random_shock = np.random.normal(0, 1)
            price_change = (mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * random_shock
            new_price = prev_price * np.exp(price_change)
            price_path.append(new_price)
        return np.array(price_path)
