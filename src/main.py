# src/main.py

from portfolio import Portfolio
from user_interface import get_user_input
from liquidation_strategy import time_driven_liquidation
from models.transaction_costs.transaction_cost import calculate_transaction_costs
from visualization import plot_liquidation_schedule, plot_transaction_costs
from data.simulations.monte_carlo import monte_carlo_simulation
from visualization import plot_cost_distribution, plot_monte_carlo_paths

def main():
    # # Get user input
    # params = get_user_input()
    
    # # Initialize Portfolio
    # portfolio = Portfolio(
    #     initial_holdings=params["initial_holdings"],
    #     initial_price=params["initial_price"],
    #     transaction_cost=params["transaction_cost"]
    # )
    
    # # Generate a time-driven liquidation schedule
    # time_horizon = params["liquidation_time_horizon"]
    # liquidation_schedule = time_driven_liquidation(portfolio.holdings, time_horizon)
    
    # # Calculate transaction costs
    # total_costs = calculate_transaction_costs(liquidation_schedule, (portfolio.transaction_cost/100))
    
    # # Visualize results
    # plot_liquidation_schedule(liquidation_schedule)
    # plot_transaction_costs(total_costs)

    # Parameters
    mu = 0.05  # Drift
    sigma = 0.3  # Try increasing volatility, e.g., 0.3 to 0.5
    transaction_cost = 0.005  # Transaction cost rate (e.g., 0.5%)
    slippage_factor = 0.01  # Increase slippage factor to add impact costs
    risk_aversion = 0.7  # Higher risk aversion can affect trade sizes
    num_simulations = 100  # Number of Monte Carlo simulations

    ## montecarlo
    params = get_user_input()
    total_costs = monte_carlo_simulation(
        total_holdings=params["initial_holdings"],
        time_horizon=params["liquidation_time_horizon"],
        initial_price=params["initial_price"],
        mu=mu,
        sigma=sigma,
        transaction_cost=params["transaction_cost"],
        risk_aversion=risk_aversion,
        num_simulations=100,
        slippage_factor=slippage_factor
    )
    
    plot_cost_distribution(total_costs)
    plot_monte_carlo_paths(total_costs)

if __name__ == "__main__":
    main()
