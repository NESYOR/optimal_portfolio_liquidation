# src/dynamic_programming.py

import numpy as np

def calculate_value_function(total_holdings, time_horizon, transaction_cost, price_path, risk_aversion):
    """
    Calculate the value function for optimal liquidation using dynamic programming.
    
    Parameters:
        total_holdings (float): Initial holdings.
        time_horizon (int): Number of time steps.
        transaction_cost (float): Cost per transaction.
        price_path (numpy.ndarray): Simulated price path.
        risk_aversion (float): Risk aversion factor.
    
    Returns:
        numpy.ndarray: Value function matrix.
    """
    # Initialize value function matrix
    V = np.zeros((time_horizon + 1, total_holdings + 1))

    for t in range(time_horizon - 1, -1, -1):
        for h in range(total_holdings + 1):
            # Consider trading any amount up to current holdings
            possible_trades = np.arange(h + 1)
            trade_costs = possible_trades * price_path[t] * transaction_cost
            trade_penalties = risk_aversion * (price_path[t] - np.mean(price_path))**2 * possible_trades
            
            # Calculate the value for each possible trade
            future_values = V[t + 1, h - possible_trades] - trade_costs - trade_penalties
            V[t, h] = np.max(future_values)
    
    return V
