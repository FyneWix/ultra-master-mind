import Levenshtein

def fitness_sum(C, PM):
    """
    C: a chromosome
    PM: the mystery phrase

    return the fitness value of the chromosome
    """
    # Check if the chromosome and the mystery phrase have the same length
    if len(C) != len(PM):
        raise ValueError("Chromosome and mystery phrase must have the same length")

    sum = 0
    for i in range(0, len(PM)):
        sum += abs(ord(C[i]) - ord(PM[i]))
    return -sum

def fitness_match(chromosome, PM, alpha):
    """
    chromosome: a chromosome
    PM: the mystery phrase

    return the fitness value of the chromosome
    """
    match = 0
    miss = 0

    for i in range(0, len(PM)):
        if chromosome[i] == PM[i]:
            match += 1
        else:
            miss += 1

    return match + alpha * miss

def fitness_levenshtein(chromosome, PM):
    """
    chromosome: a chromosome
    PM: the mystery phrase

    return the fitness value of the chromosome
    """
    return -Levenshtein.distance(chromosome, PM)

def fitness_list(population, PM):
    """
    population: list of chromosomes
    PM: the mystery phrase

    return a list a tuples of the form (chromosome, fitness value)
    """
    return [(chromosome, fitness_sum(chromosome, PM)) for chromosome in population]

def sort_fitness_list(population_with_fitness):
    """
    population_with_fitness: list of tuples of the form (chromosome, fitness value)

    return a list of tuples sorted by fitness value in descending order
    """
    return sorted(population_with_fitness, key=lambda x: x[1], reverse=True)


