from app.fitness import fitness_list

def sort_fitness_list(population_with_fitness):
    """
    population_with_fitness: list of tuples of the form (chromosome, fitness value)

    return a list of tuples sorted by fitness value in descending order
    """
    return sorted(population_with_fitness, key=lambda x: x[1], reverse=True)


def extract_chromosomes(population_with_fitness):
    """
    population_with_fitness: list of tuples of the form (chromosome, fitness value)

    return a list of chromosomes sorted by fitness value in descending order
    """
    return [chromosome for chromosome, fitness_value in population_with_fitness]

def selection(population, SR, N, PM):
    """
    population: list of chromosomes
    SR: selection rate
    N: size of the population
    PM: the mystery phrase

    return a list of chromosomes selected from the population
    """
    population_with_fitness = fitness_list(population, PM)
    sorted_population_with_fitness = sort_fitness_list(population_with_fitness)
    best_chromosomes = extract_chromosomes(sorted_population_with_fitness)
    return best_chromosomes[:int(SR * N)]