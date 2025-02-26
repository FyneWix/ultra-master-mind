import genesis
import selection
import fitness
import reproduction
import mutation

def get_input_phrase():
    m = str(input("Enter the mystery phrase: "))
    return m

if __name__ == "__main__":

    # Get the mystery phrase
    TARGET_PHRASE = get_input_phrase()
    print("The mystery phrase is: ", TARGET_PHRASE)

    # Constants for the game
    ## amount of generations
    GENERATIONS = 2
    ## population size
    POP_SIZE = 10
    ## mutation rate
    MUTATION_RATE = 0.5
    ## selection rate
    SELECTION_RATE = 0.5
    ## chromosome length
    CHROMOSOME_LENGTH = len(TARGET_PHRASE)

    # 1. Initialize the population
    population = genesis.genesis(POP_SIZE, CHROMOSOME_LENGTH)
    print("Initial population: ", population)

    # 2. Evolution
    for generation in range(GENERATIONS):
        # 2.1 Evaluation (fitness)
        # Calculate the fitness of each chromosome in the population
        fitness_values = fitness.fitness_list(population, TARGET_PHRASE)
        print("Fitness values: ", fitness_values)

        # Sort the population by fitness
        sorted_fitness_list = fitness.sort_fitness_list(fitness_values)
        print("Sorted fitness list: ", sorted_fitness_list)

        # Extract the chromosomes from the population
        chromosomes = selection.extract_chromosomes(sorted_fitness_list)
        print("Chromosomes: ", chromosomes)

        # 2.2 Selection
        # Select the best chromosomes
        selected_chromosomes = selection.selection(chromosomes, SELECTION_RATE, POP_SIZE)
        print("Selected chromosomes: ", selected_chromosomes)

