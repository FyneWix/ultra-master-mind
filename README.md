# Ultra Mastermind: Genetic Algorithm Phrase Guesser

## Description

Ultra Mastermind is a Python project that implements a genetic algorithm to guess a target "mystery phrase" provided by the user. The algorithm evolves a population of candidate phrases over several generations, using principles of selection, reproduction, and mutation to converge towards the target phrase.

The project allows users to experiment with different fitness functions to evaluate how well a candidate phrase matches the target and visualizes the evolution of fitness scores over generations.

## Features

*   **Genetic Algorithm:** Core implementation of a genetic algorithm to find a target string.
*   **Multiple Fitness Functions:**
    *   **Sum Fitness:** Based on the sum of absolute differences of ASCII values.
    *   **Match Fitness:** Based on the number of matching characters, with a penalty for mismatches.
    *   **Levenshtein Fitness:** Based on the Levenshtein distance between strings.
*   **Customizable Parameters:** Users can set the number of generations, population size, mutation rate, and selection rate.
*   **Fitness Evolution Plot:** Generates and saves a plot showing the best and average fitness scores per generation.
*   **Modular Design:** Code is organized into separate modules for genesis, fitness calculation, selection, reproduction, and mutation.

## How to Run

### Prerequisites

*   Python 3.x
*   pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/FyneWix/ultra-master-mind.git
    cd ultra-master-mind
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Execution

1.  **Run the main script from the project root directory:**
    ```bash
    python app/main.py
    ```

2.  **Follow the prompts:**
    *   Enter the mystery phrase you want the algorithm to guess.
    *   Choose a fitness function (1: Sum, 2: Match, 3: Levenshtein).
        *   If Match Fitness is chosen, you'll be prompted for an alpha value.
    *   Enter the genetic algorithm parameters:
        *   Number of generations
        *   Population size
        *   Mutation rate (e.g., 0.1 for 10%)
        *   Selection rate (e.g., 0.5 for 50%)

## Project Structure

The core logic is located in the `app/` directory:

*   [`app/main.py`](app/main.py): The main script to run the genetic algorithm. Handles user input and orchestrates the algorithm's flow.
*   [`app/genesis.py`](app/genesis.py): Generates the initial population of chromosomes.
*   [`app/fitness.py`](app/fitness.py): Defines different fitness functions to evaluate chromosomes.
*   [`app/selection.py`](app/selection.py): Implements the selection mechanism for choosing chromosomes for reproduction.
*   [`app/reproduction.py`](app/reproduction.py): Implements the crossover (reproduction) mechanism.
*   [`app/mutation.py`](app/mutation.py): Implements the mutation mechanism.
*   [`app/visualization.py`](app/visualization.py): Handles plotting the fitness evolution.

The `test/` directory contains unit tests for some modules.
The `figures/` directory (created automatically if it doesn't exist) stores the generated fitness evolution plots.

## Output

*   **Console Output:**
    *   The initial population.
    *   The best chromosome found at regular intervals (every 50 generations by default).
    *   A message when the target phrase is found or when all generations are completed.
    *   The final best chromosome found.
*   **Fitness Plot:**
    *   A window will display a plot of the best (and average) fitness values against the number of generations.
    *   This plot is also saved as a `.png` file (e.g., `fitness_evolution_YYYYMMDD_HHMMSS.png`) in the `figures/` directory at the project root.

## Customization

*   **Target Phrase:** Can be any string entered by the user.
*   **Fitness Function:** Choose from the available options when prompted.
*   **Algorithm Parameters:** Adjust generations, population size, mutation rate, and selection rate to observe different evolutionary behaviors.