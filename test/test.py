import unittest
from nctranslator.sequence import *

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

    
class SequenceTestCase(unittest.TestCase):

    def test_is_nucleotide(self):
        seq = Sequence("ATCGatgc")
        for i in range(len(seq)):
            self.assertIsInstance(seq[i], Nucleotide)

        

    def test_add_sequence(self):
        seq = Sequence("ATCGGTGCAGTAGCDBM")
        self.assertEqual(str(seq), "ATCGGTGCAGTAGCNNN")

    def test_sequence_list(self):
        seq = Sequence("ATCgGTGcAGTAGCDBM")
        self.assertEqual(str(seq.list()), "[A, T, C, G, G, T, G, C, A, G, T, A, G, C, N, N, N]")

    def test_sequence_invalid(self):
        with self.assertRaises(ValueError):
            seq = Sequence("ATCGGTGCAGTAGCDBM1")
        
    
    
    

if __name__ == '__main__':
    unittest.main()