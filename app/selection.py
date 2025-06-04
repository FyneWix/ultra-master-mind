def extract_chromosomes(population_with_fitness):
    """
    Extracts chromosomes from a list of (chromosome, fitness_value) tuples.

    The order of chromosomes in the returned list corresponds to their order
    in the input list.

    Args:
        population_with_fitness (list): A list of tuples, where each tuple
                                        is of the form (chromosome, fitness_value).

    Returns:
        list: A list of chromosomes (strings).
    """
    return [chromosome for chromosome, fitness_value in population_with_fitness]

def selection(population, SR, N):
    """
    Selects a portion of the population based on a selection rate.

    It is assumed that the input population is already sorted by fitness
    in descending order (best individuals first).

    Args:
        population (list): A list of chromosomes (strings), sorted by fitness
                           in descending order.
        SR (float): The selection rate (e.g., 0.5 for 50%).
        N (int): The total population size, used to calculate the number of
                 individuals to select.

    Returns:
        list: A list containing the selected chromosomes. This will be the top
              SR * N individuals from the input population.
    """
    num_to_select = int(SR * N)
    return population[:num_to_select]