import random

def mutation(population, MR):
    """
    Mutates a portion of the population based on the mutation rate.

    For each selected chromosome, a single gene (character) is randomly
    changed to another printable ASCII character.

    Args:
        population (list): A list of chromosomes (strings).
        MR (float): The mutation rate, determining the proportion of the
                    population to mutate (e.g., 0.1 for 10%).

    Returns:
        list: The population with some chromosomes potentially mutated.
              Modifies the input list in place.
    """
    N = len(population)
    if N == 0: # Handle empty population
        return population
        
    n_mutations = int(MR * N)
    if n_mutations == 0 and MR > 0 and N > 0: # Ensure at least one mutation if rate > 0 and pop exists
        n_mutations = 1
    
    if n_mutations > N : # Cannot mutate more chromosomes than exist
        n_mutations = N

    # Selection of unique indexes for the chromosomes to mutate
    # Ensure n_mutations is not greater than population size for random.sample
    index_list = random.sample(range(N), min(n_mutations, N))

    for index in index_list:
        # Convert the chromosome into a list of characters
        chromosome = list(population[index])
        
        if not chromosome: # Skip empty chromosomes
            continue

        # Selection of a random character index in the chromosome
        gene_index = random.randint(0, len(chromosome) - 1)

        # New character to replace the old one
        new_char = chr(random.randint(32, 126)) # Printable ASCII

        # Replace the old character by the new one
        chromosome[gene_index] = new_char

        # Convert the list of characters back to a string and update the population
        population[index] = ''.join(chromosome)

    return population