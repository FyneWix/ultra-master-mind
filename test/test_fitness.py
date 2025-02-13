import unittest
from app.fitness import fitness

class TestFitness(unittest.TestCase):

    # Test identical strings
    def test_identical_strings(self):
        self.assertEqual(fitness("hello", "hello"), 0)

    # Test empty strings
    def test_empty_strings(self):
        self.assertEqual(fitness("", ""), 0)

    # Test different strings
    def test_different_characters(self):
        self.assertEqual(fitness("abcde", "fghij"), -25)
        self.assertEqual(fitness("fghij", "abcde"), -25)

    # Test mixed characters
    def test_mixed_characters(self):
        self.assertEqual(fitness("test", "tEst"), -32)

    # Test special characters
    def test_special_characters(self):
        self.assertEqual(fitness("test", "t$st"), -65)
        self.assertEqual(fitness("alpha", "@lpha"), -33)
        self.assertEqual(fitness("flint", "fl!nt"), -72)
        self.assertEqual(fitness("hello", "h&llo"), -63)
        self.assertEqual(fitness("stars", "st*rs"), -55)

    # Test different lengths
    def test_different_lengths(self):
        with self.assertRaises(ValueError):
            fitness("short", "longer")   

if __name__ == '__main__':
    unittest.main()