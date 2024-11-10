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
