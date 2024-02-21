import unittest
from sequence import *

class NucleotideTestCase(unittest.TestCase):
    # Test cases for the Valid Nucleotide
    def test_add_nucleotide(self):
        nuc = Nucleotide("A")
        self.assertEqual(str(nuc), 'A')

        nuc2 = Nucleotide("a")
        self.assertEqual(str(nuc2), 'A')

        nuc3 = Nucleotide("B")
        self.assertEqual(str(nuc3), 'N')

    def test_add_uracil(self):
        nuc = Nucleotide("U")
        self.assertEqual(str(nuc), 'T')

        nuc2 = Nucleotide("u")
        self.assertEqual(str(nuc2), 'T')

    def test_add_nucleotide_invalid(self):
        with self.assertRaises(ValueError):
            nuc = Nucleotide("1")
        with self.assertRaises(ValueError):
            nuc = Nucleotide(">")

    

    

if __name__ == '__main__':
    unittest.main()