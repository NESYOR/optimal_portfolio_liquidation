# src/transaction_cost.py
import numpy as np

def calculate_transaction_costs(trades, cost_per_trade):
    """
    Calculates total transaction costs for a series of trades.
    
    Parameters:
        trades (numpy.ndarray): Array of trades (amount sold per time step).
        cost_per_trade (float): Transaction cost per trade.
    
    Returns:
        float: Total transaction cost.
    """
    return np.sum(trades * cost_per_trade)


def calculate_transaction_costs_with_slippage(trades, cost_per_trade, slippage_factor):
    """
    Calculates total transaction costs with slippage.
    
    Parameters:
        trades (numpy.ndarray): Array of trades (amount sold per time step).
        cost_per_trade (float): Transaction cost rate.
        slippage_factor (float): Factor representing slippage cost based on trade size.
    
    Returns:
        float: Total transaction cost.
    """
    slippage_costs = slippage_factor * trades ** 2  # Quadratic slippage model
    return np.sum((trades * cost_per_trade) + slippage_costs)
