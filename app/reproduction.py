import random

def reproduction(population):
    """
    Creates a new child chromosome by combining parts of two parent chromosomes.

    Parents are selected randomly from the population. A single crossover point
    is chosen, and the child is formed by taking the first part of one parent
    and the second part of the other.

    Args:
        population (list): A list of parent chromosomes (strings).
                           Assumes all chromosomes have the same length and
                           the list is not empty.

    Returns:
        str: A new child chromosome. Returns an empty string if the population
             is empty or chromosomes are empty.
    """
    if not population or not population[0]:
        return "" # Handle empty population or empty chromosomes

    # Chromosome length
    L = len(population[0])
    if L == 0:
        return "" # Handle empty chromosomes

    # Choose two parents
    M, F = choose_two_parents(population)

    # Cutting point
    # Ensure L//3 is not greater than 2*L//3 for randint, especially for small L
    if L < 2: # If length is 0 or 1, cut point is tricky.
        cut = 0
    elif L == 2:
        cut = 1
    else:
        cut = random.randint(L//3, 2*L//3)

    # Create a child
    child = M[:cut] + F[cut:]

    return child


def choose_two_parents(population):
    """
    Randomly selects two distinct parents from the given population.

    Args:
        population (list): A list of chromosomes (strings). Requires at least
                           two chromosomes for selection.

    Returns:
        tuple: A tuple containing two distinct parent chromosomes (M, F).
               Returns (None, None) if population has fewer than 2 individuals.
    """
    if len(population) < 2:
        raise ValueError("Population must contain at least two individuals to choose two parents.")
    # Selects two different parents
    M, F = random.sample(population, 2)
    return M, F