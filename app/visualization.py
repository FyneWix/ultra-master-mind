import matplotlib.pyplot as plt
import os

def plot_fitness_evolution(generations, best_fitness_values, avg_fitness_values=None, title="Évolution de la fitness"):
    """
    Trace l'évolution de la fitness en fonction des générations.
    
    Args:
        generations: Liste des numéros de génération
        best_fitness_values: Liste des meilleures valeurs de fitness à chaque génération
        avg_fitness_values: Liste optionnelle des valeurs moyennes de fitness à chaque génération
        title: Titre du graphique
    """
    # Create the 'figures' directory if it doesn't exist
    figures_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'figures')
    if not os.path.exists(figures_dir):
        os.makedirs(figures_dir)
    
    plt.figure(figsize=(10, 6))
    plt.plot(generations, best_fitness_values, 'b-', label='Meilleure fitness')
    
    if avg_fitness_values:
        plt.plot(generations, avg_fitness_values, 'r--', label='Fitness moyenne')
    
    plt.title(title)
    plt.xlabel('Génération')
    plt.ylabel('Valeur de fitness')
    plt.grid(True)
    plt.legend()
    
    # Save the figure with a timestamp
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'fitness_evolution_{timestamp}.png'
    
    # Save the figure in the 'figures' directory
    filepath = os.path.join(figures_dir, filename)
    plt.savefig(filepath)
    
    print(f"Graph saved to: {filepath}")
    
    # Show the graph
    plt.show()