# src/user_interface.py

def get_user_input():
    """
    Prompts the user for basic portfolio and strategy parameters.
    
    Returns:
        dict: A dictionary of input parameters.
    """
    initial_holdings = float(input("Enter initial holdings: "))
    initial_price = float(input("Enter initial asset price: "))
    transaction_cost = float(input("Enter transaction cost per trade (as %): "))
    liquidation_time_horizon = int(input("Enter liquidation time horizon (steps): "))
    
    return {
        "initial_holdings": initial_holdings,
        "initial_price": initial_price,
        "transaction_cost": transaction_cost,
        "liquidation_time_horizon": liquidation_time_horizon
    }
