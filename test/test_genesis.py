import unittest
from app.genesis import genesis

class TestGenesis(unittest.TestCase):
    
    # Test list length
    def test_list_length(self):
        self.assertEqual(len(genesis(10,5)), 10)

    # Test chromosome length (for each chromosome)
    def test_chromosome_length(self):
        for chromosome in genesis(10,5):
            self.assertEqual(len(chromosome), 5)

    # Test chromosome content (for each chromosome)
    def test_chromosome_content(self):
        for chromosome in genesis(10,5):
            for char in chromosome:
                self.assertTrue(ord(char) >= 32 and ord(char) <= 126)

    # Test empty list
    def test_zero_population(self):
        self.assertEqual(genesis(0,5), [])

    # Test empty chromosome
    def test_zero_chromosome(self):
        self.assertEqual(genesis(10,0), ['']*10)

    # Test empty list and chromosome
    def test_zero_population_and_chromosome(self):
        self.assertEqual(genesis(0,0), [])

    # Test minimum values
    def test_minimum_values(self):
        population = genesis(1,1)
        self.assertEqual(len(population), 1)
        self.assertEqual(len(population[0]), 1)

    # Test high values
    def test_high_values(self):
        population = genesis(1000,1000)
        self.assertEqual(len(population), 1000)
        self.assertTrue(all(len(chromosome) == 1000 for chromosome in population))

    # Test variability
    def test_variability(self):
        population1 = genesis(10, 5)
        population2 = genesis(10, 5)
        self.assertNotEqual(population1, population2)

if __name__ == '__main__':
    unittest.main()