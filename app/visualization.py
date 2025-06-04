import matplotlib.pyplot as plt
import os
from datetime import datetime

def plot_fitness_evolution(generations, best_fitness_values, avg_fitness_values=None, title="Fitness Evolution"):
    """
    Plots the evolution of best and optionally average fitness values over generations.

    The plot is displayed and also saved to a 'figures' directory at the root of the project.
    The 'figures' directory is created if it does not exist.

    Args:
        generations (list): A list of integers representing generation numbers.
        best_fitness_values (list): A list of numerical values representing the
                                    best fitness score in each generation.
        avg_fitness_values (list, optional): A list of numerical values representing
                                             the average fitness score in each
                                             generation. Defaults to None.
        title (str, optional): The title of the plot. Defaults to "Fitness Evolution".
    """
    # Create the 'figures' directory if it doesn't exist
    # Assumes this script is in 'app' and 'figures' is at project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    figures_dir = os.path.join(project_root, 'figures')
    if not os.path.exists(figures_dir):
        os.makedirs(figures_dir)
    
    plt.figure(figsize=(10, 6))
    plt.plot(generations, best_fitness_values, 'b-', label='Best Fitness')
    
    if avg_fitness_values:
        plt.plot(generations, avg_fitness_values, 'r--', label='Average Fitness')
    
    plt.title(title)
    plt.xlabel('Generation')
    plt.ylabel('Fitness Value')
    plt.grid(True)
    plt.legend()
    
    # Save the figure with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'fitness_evolution_{timestamp}.png'
    
    # Save the figure in the 'figures' directory
    filepath = os.path.join(figures_dir, filename)
    plt.savefig(filepath)
    
    print(f"Graph saved to: {filepath}")
    
    # Show the graph
    plt.show()