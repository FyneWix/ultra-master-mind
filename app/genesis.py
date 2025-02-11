import random

def genesis(N, L):
    """
    N: size of the population
    L: length of the chromosome
    
    return a list of N chromosomes of length L
    """
    population = []
    for i in range(N):
        chromosome = ""
        for j in range(L):
            chromosome += chr(random.randint(32, 126))
        population.append(chromosome)
    return population