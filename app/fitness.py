import Levenshtein

def fitness_sum(C, PM):
    """
    Calculates the fitness of a chromosome based on the sum of absolute differences 
    between ASCII values of its characters and those of the target phrase.

    Args:
        C (str): The chromosome (a string).
        PM (str): The target mystery phrase (a string).

    Returns:
        int: The negative sum of absolute differences, representing the fitness score.
             A higher value (closer to 0) indicates better fitness.
    """
    # Check if the chromosome and the mystery phrase have the same length
    if len(C) != len(PM):
        raise ValueError("Chromosome and mystery phrase must have the same length")

    sum_val = 0
    for i in range(0, len(PM)):
        sum_val += abs(ord(C[i]) - ord(PM[i]))
    return -sum_val

def fitness_match(chromosome, PM, alpha):
    """
    Calculates the fitness of a chromosome based on matching characters
    with the target phrase, applying a factor for mismatches.

    Args:
        chromosome (str): The chromosome (a string).
        PM (str): The target mystery phrase (a string).
        alpha (float): A coefficient that weights the impact of mismatches.

    Returns:
        float: The fitness score, calculated as matches plus alpha times mismatches.
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
    Calculates the fitness of a chromosome based on the Levenshtein distance
    to the target phrase.

    Args:
        chromosome (str): The chromosome (a string).
        PM (str): The target mystery phrase (a string).

    Returns:
        int: The negative Levenshtein distance. A higher value (closer to 0)
             indicates better fitness.
    """
    return -Levenshtein.distance(chromosome, PM)

def fitness_list(population, PM, fitness_func):
    """
    Calculates the fitness for each chromosome in a population using a specified
    fitness function.

    Args:
        population (list): A list of chromosomes (strings).
        PM (str): The target mystery phrase (a string).
        fitness_func (function): The fitness function to be used for evaluation.
                                 It should accept a chromosome and the target phrase
                                 as arguments.

    Returns:
        list: A list of tuples, where each tuple is of the form
              (chromosome, fitness_value).
    """
    return [(chromosome, fitness_func(chromosome, PM)) for chromosome in population]

def sort_fitness_list(fitness_values, reverse=True):
    """
    Sorts a list of (chromosome, fitness_value) tuples based on fitness values.

    Args:
        fitness_values (list): A list of tuples, where each tuple is of the form
                               (chromosome, fitness_value).
        reverse (bool, optional): If True, sorts in descending order (higher fitness
                                  first). Defaults to True.

    Returns:
        list: A new list of tuples, sorted by fitness value.
    """
    return sorted(fitness_values, key=lambda x: x[1], reverse=True)