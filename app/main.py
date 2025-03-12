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
    GENERATIONS = 5000
    POP_SIZE = 10
    MUTATION_RATE = 0.5
    SELECTION_RATE = 0.5
    CHROMOSOME_LENGTH = len(TARGET_PHRASE)

    # 1. Initialize the population
    population = genesis.genesis(POP_SIZE, CHROMOSOME_LENGTH)
    print("Initial population: ", population)

    # 2. Evolution
    for generation in range(GENERATIONS):
        # 2.1 Evaluation (fitness)
        # Calculate the fitness of each chromosome in the population
        fitness_values = fitness.fitness_list(population, TARGET_PHRASE)

        # Sort the population by fitness
        sorted_fitness_list = fitness.sort_fitness_list(fitness_values)

        # Extract the chromosomes from the population
        chromosomes = selection.extract_chromosomes(sorted_fitness_list)

        # 2.2 Selection
        # Select the best chromosomes
        selected_chromosomes = selection.selection(chromosomes, SELECTION_RATE, POP_SIZE)

        # 2.3 Reproduction
        while len(selected_chromosomes) < POP_SIZE:
            child = reproduction.reproduction(selected_chromosomes)
            selected_chromosomes.append(child)

        # 2.4 Mutation
        mutated_population = mutation.mutation(selected_chromosomes, MUTATION_RATE)

        # Update the population
        population = mutated_population

        # Select the best chromosome
        best_chromosome = population[0]

        # Print the best chromosome every 50 generations
        if (generation + 1) % 50 == 0:
            print(f"Generation {generation + 1}: Best chromosome: {best_chromosome}")
        
        # Check if the best chromosome is the mystery phrase
        if best_chromosome == TARGET_PHRASE:
            print("The mystery phrase has been found!")
            break

    # Print the best chromosome
    print("Best chromosome: ", best_chromosome)

