import random

def mutation(population, MR):
    """
    population: list of chromosomes
    MR: Mutation rate

    Mutate the population
    """
    N = len(population)
    n_mutations = int(MR * N)


    # Selection of unique indexes for the chromosomes to mutate
    index_list = random.sample(range(N), n_mutations)
    print("Index list: ", index_list)

    for index in index_list:
        # Convert the chromosome into a list of characters
        chromosome = list(population[index])
        print("Chromosome: ", chromosome)

        # Selection of a random character index in the chromosome
        gene_index = random.randint(0, len(chromosome) - 1)
        print("Gene index: ", gene_index)

        # New character to replace the old one
        new_char = chr(random.randint(32, 126))
        print("New char: ", new_char)

        # Replace the old character by the new one
        chromosome[gene_index] = new_char
        print("Chromosome after mutation: ", chromosome)

        # Convert the list of characters back to a string and update the population
        population[index] = ''.join(chromosome)
        print("Population after mutation: ", population)

    return population


def mutation_old(population, MR):
    """
    population: list of chromosomes
    MR: Mutation rate
    
    Mutate the population
    """
    # Number of chromosomes to mutate
    N = len(population)
    n_mutations = int(MR * N)

    # List of indexes of the chromosomes to mutate
    index_list = []

    for i in range(n_mutations) :

        # Random index
        index = random.randint(0, N - 1)

        # Check if the index is already used
        while index in index_list :
            index = random.randint(0, N - 1)

        # Add the index to the list
        index_list.append(index)

        # New character to replace the old one
        new_char = chr(random.randint(32, 126))

        # Replace the old character by the new one
        population[index] = population[index].replace(random.choice(population[index]), new_char)

    return population