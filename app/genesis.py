import random

def genesis(N, L):
    """
    Generates an initial population of chromosomes.

    Each chromosome is a string of random printable ASCII characters.

    Args:
        N (int): The number of chromosomes in the population (population size).
        L (int): The length of each chromosome.

    Returns:
        list: A list containing N chromosomes, each of length L.
    """
    population = []
    for i in range(N):
        chromosome = ""
        for j in range(L):
            chromosome += chr(random.randint(32, 126)) # Printable ASCII characters
        population.append(chromosome)
    return population