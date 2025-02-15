def fitness_value(C, PM):
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

def fitness_list(population, PM):
    """
    population: list of chromosomes
    PM: the mystery phrase

    return a list a tuples of the form (chromosome, fitness value)
    """
    return [(chromosome, fitness(chromosome, PM)) for chromosome in population]