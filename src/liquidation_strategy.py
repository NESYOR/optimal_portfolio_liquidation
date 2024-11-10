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

# src/liquidation_strategy.py

import numpy as np

def risk_adjusted_liquidation_schedule(total_holdings, time_horizon, risk_aversion, price_path):
    """
    Generate a liquidation schedule adjusted by risk aversion.

    Parameters:
        total_holdings (float): Total initial holdings to liquidate.
        time_horizon (int): Number of time steps for liquidation.
        risk_aversion (float): Risk aversion parameter (higher values mean more conservative trading).
        price_path (numpy.ndarray): Simulated asset price path.

    Returns:
        numpy.ndarray: Array showing the remaining holdings at each time step.
    """
    liquidation_schedule = []
    remaining_holdings = total_holdings

    for t in range(time_horizon):
        if remaining_holdings <= 0:
            liquidation_schedule.append(0)
            continue

        # Adjust trade amount based on risk aversion and price volatility
        trade_amount = remaining_holdings / (time_horizon - t) * (1 - risk_aversion * np.std(price_path[:t+1]) / np.mean(price_path[:t+1]))
        trade_amount = max(0, min(trade_amount, remaining_holdings))  # Ensure non-negative and does not exceed holdings
        remaining_holdings -= trade_amount
        liquidation_schedule.append(remaining_holdings)
    
    liquidation_schedule.append(0)  # Ensure end state has zero holdings
    return np.array(liquidation_schedule)
