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

