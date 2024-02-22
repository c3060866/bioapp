from sequence import *
from Bio import SeqIO
from io import StringIO




class Translator:

    def __init__(self):
        self.input = None
        self.translated_sequence = ""
        

    def input_sequence(self, sequence):
        self.input = Sequence(sequence)

    def sequence_cleaner(self):
        if len(self.input) % 3 != 0:
            self.input = self.input[:-(len(self.input) % 3)]
        

    def fasta_input(self, text):
        sequences = []
        with StringIO(text) as fasta_handle:
            for record in SeqIO.parse(fasta_handle, "fasta"):
                print(record)
                sequences.append(record)
        return sequences
    
    def fasta_input_file(self, file):
        sequences = []
        for record in SeqIO.parse(file, "fasta"):
                print(record)
                sequences.append(record)
        return sequences

    def translate(self, sequence):
        self.input_sequence(sequence)

        # self.sequence_cleaner()

        for i,j in enumerate(self.input):
            
            # if i+3 <= len(self.input):
                codon = self.input[i:i+3]
                codon = ''.join(str(i) for i in codon)
                # if self.translation(codon) == "*":
                #     break
                if self.translation(codon) != None:
                    self.translated_sequence += self.translation(codon)

        return self.translated_sequence
    
    def frame_translation(self, frame):
        frame_sequence = ""
        for i in range(len(self.translated_sequence)):
            if i % 3 == frame:
                frame_sequence += self.translated_sequence[i]
        return frame_sequence

    def translation(self, codon):

        if codon == "ATG":
            return "M"
        elif codon == "TAA" or codon == "TAG" or codon == "TGA":
            return "*"
        elif codon == "TTT" or codon == "TTC":
            return "F"
        elif codon == "TTA" or codon == "TTG" or codon == "CTT" or codon == "CTC" or codon == "CTA" or codon == "CTG":
            return "L"
        elif codon == "TCT" or codon == "TCC" or codon == "TCA" or codon == "TCG" or codon == "AGT" or codon == "AGC":
            return "S"
        elif codon == "TAT" or codon == "TAC":
            return "Y"
        elif codon == "TGT" or codon == "TGC":
            return "C"
        elif codon == "TGG":
            return "W"
        elif codon == "CCT" or codon == "CCC" or codon == "CCA" or codon == "CCG":
            return "P"
        elif codon == "CAT" or codon == "CAC":
            return "H"
        elif codon == "CAA" or codon == "CAG":
            return "Q"
        elif codon == "CGT" or codon == "CGC" or codon == "CGA" or codon == "CGG" or codon == "AGA" or codon == "AGG":
            return "R"
        elif codon == "ATT" or codon == "ATC" or codon == "ATA":
            return "I"
        elif codon == "ACT" or codon == "ACC" or codon == "ACA" or codon == "ACG":
            return "T"
        elif codon == "AAT" or codon == "AAC":
            return "N"
        elif codon == "AAA" or codon == "AAG":
            return "K"
        elif codon == "GTT" or codon == "GTC" or codon == "GTA" or codon == "GTG":
            return "V"
        elif codon == "GCT" or codon == "GCC" or codon == "GCA" or codon == "GCG":
            return "A"
        elif codon == "GAT" or codon == "GAC":
            return "D"
        elif codon == "GAA" or codon == "GAG":
            return "E"
        elif codon == "GGT" or codon == "GGC" or codon == "GGA" or codon == "GGG":
            return "G"
        else:
            pass
        



    def print_sequence(self):
        print(self.input)

sample ="ATGTTTAAAGGTG"
test = Translator()
# print(test.translate("ATGTTTAAAGGTG"))
# print(test.frame_translation(2))

fasta = """>1   
    ATGTTT 
    AAAGGTG
    cagtgtattacggg"""
print(str(test.fasta_input(fasta)[0]))

def __main__():
    test = Translator()
    print(test.translate("ATGTTTAAAGGTG"))
    print(test.frame_translation(2))

    fasta = """>1   
        ATGTTT 
        AAAGGTG
        cagtgtattacggg"""
    print(str(test.fasta_input(fasta)[0]))