# src/visualization.py

import matplotlib.pyplot as plt

def plot_liquidation_schedule(schedule, title="Liquidation Schedule"):
    """
    Plots portfolio holdings over time as they are liquidated.
    
    Parameters:
        schedule (numpy.ndarray): Array of portfolio holdings over time.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(schedule, marker='o')
    plt.title(title)
    plt.xlabel("Time Step")
    plt.ylabel("Holdings")
    plt.grid()
    plt.show()

def plot_transaction_costs(total_costs):
    """
    Display the total transaction costs.
    
    Parameters:
        total_costs (float): The cumulative transaction costs.
    """
    print(f"Total Transaction Costs: {total_costs:.2f}")



import matplotlib.pyplot as plt

def plot_monte_carlo_paths(paths, title="Monte Carlo Simulation of Liquidation Paths"):
    plt.figure(figsize=(10, 5))
    for path in paths:
        plt.plot(path, color='blue', alpha=0.1)
    plt.title(title)
    plt.xlabel("Time Step")
    plt.ylabel("Holdings")
    plt.grid()
    plt.show()

def plot_cost_distribution(costs, title="Transaction Cost Distribution"):
    plt.figure(figsize=(10, 5))
    plt.hist(costs, bins=30, alpha=0.7)
    plt.title(title)
    plt.xlabel("Total Transaction Cost")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()
