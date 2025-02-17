import random

def reproduction(population):

    # Chromosome length
    L = len(population[0])

    # Choose two parents
    M, F = choose_two_parents(population)

    # Cutting point
    cut = random.randint(L//3, 2*L//3)

    # Create a child
    child = M[:cut] + F[cut:]

    return child

def choose_two_parents(population):
    # Mother
    M = random.choice(population) 
    m_index = population.index(M)

    # Father
    F = random.choice(population)
    f_index = population.index(F)

    if m_index == f_index:
        return choose_two_parents(population)
        
    return M, F