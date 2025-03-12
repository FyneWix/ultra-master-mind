import random

def reproduction(population):
    """
    population: list of chromosomes

    return a new chromosome (child)
    """

    # Chromosome length
    L = len(population[0])

    # Choose two parents
    M, F = choose_two_parents(population)

    # Cutting point
    cut = random.randint(L//3, 2*L//3)

    # Create a child
    child = M[:cut] + F[cut:]

    return child


def choose_two_parents(population):
    """
    population: list of chromosomes

    return two chromosomes (parents)
    """
    # Sélectionne deux parents différents
    M, F = random.sample(population, 2)
    return M, F