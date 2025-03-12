def extract_chromosomes(population_with_fitness):
    """
    population_with_fitness: list of tuples of the form (chromosome, fitness value)

    return a list of chromosomes sorted by fitness value in descending order
    """
    return [chromosome for chromosome, fitness_value in population_with_fitness]

def selection(population, SR, N):
    """
    population: list of chromosomes
    SR: selection rate
    N: population size

    return a list of chromosomes selected from the population
    """
    return population[:int(SR * N)]