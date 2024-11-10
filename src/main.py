# src/main.py

from portfolio import Portfolio
from user_interface import get_user_input
from liquidation_strategy import time_driven_liquidation
from transaction_cost import calculate_transaction_costs
from visualization import plot_liquidation_schedule, plot_transaction_costs

def main():
    # Get user input
    params = get_user_input()
    
    # Initialize Portfolio
    portfolio = Portfolio(
        initial_holdings=params["initial_holdings"],
        initial_price=params["initial_price"],
        transaction_cost=params["transaction_cost"]
    )
    
    # Generate a time-driven liquidation schedule
    time_horizon = params["liquidation_time_horizon"]
    liquidation_schedule = time_driven_liquidation(portfolio.holdings, time_horizon)
    
    # Calculate transaction costs
    total_costs = calculate_transaction_costs(liquidation_schedule, (portfolio.transaction_cost/100))
    
    # Visualize results
    plot_liquidation_schedule(liquidation_schedule)
    plot_transaction_costs(total_costs)

if __name__ == "__main__":
    main()
