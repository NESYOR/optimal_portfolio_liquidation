# src/liquidation_strategy.py

import numpy as np

def time_driven_liquidation(total_holdings, time_horizon):
    """
    Calculate the liquidation schedule such that the portfolio is liquidated evenly over the time horizon.

    Parameters:
        total_holdings (float): Total initial holdings to liquidate.
        time_horizon (int): Number of time steps for liquidation.

    Returns:
        numpy.ndarray: Array showing the remaining holdings at each time step.
    """
    holdings = np.linspace(total_holdings, 0, time_horizon + 1)  # Descending from total_holdings to 0
    return holdings
