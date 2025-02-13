def fitness(C, PM):
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
