from sequence import *
from Bio import SeqIO
from io import StringIO
import os.path
import argparse

'''
Translator class to translate DNA sequence to protein sequence
has the following main methods:
    - fasta_handler(input, frame)
    - translate(sequence)

@params:
The class itself has no parameters and needs to be initialized before use. The main function to be called is 
fasta_handler(input, frame) which takes in a DNA sequence and a frame to translate the sequence. The input can be a raw string,
fasta string or a file. The frame is an integer value of 0, 1 or 2. The translate method takes in a DNA sequence and
translates it to a protein sequence.


'''

class Translator:
    # initializing the class with attributes
    def __init__(self):
        self.input = None
        self.frame = 0
        self.translated_sequence = ""
        
    # method to input a sequence which converts it to a Sequence object
    def input_sequence(self, sequence):
        self.input = Sequence(sequence)
        
    # method to parse a fasta string and return a list of sequences    
    def fasta_input(self, text):
        sequences = []
        with StringIO(text) as fasta_handle:
            for record in SeqIO.parse(fasta_handle, "fasta"):
                print(record)
                sequences.append(record)

        return sequences
    # method to parse a fasta file and return a list of sequences
    def fasta_input_file(self, file):
        sequences = []
        for record in SeqIO.parse(file, "fasta"):
                sequences.append(record)
        return sequences
    # main method to handle fasta input and translate the sequences. Returns a list of translated sequences
    def fasta_handler(self, input ,frame):
        self.frame = frame
        output = []
        if isinstance(input, str):
            sequences = self.fasta_input(input)
        if os.path.isfile(input):
            sequences = self.fasta_input_file(input)
        for i in sequences:
            transseq = ""
            transseq = self.translate(str(i.seq))
            output.append([i.id,transseq])

        if sequences == []:
            return self.translate(input)
        
        return output

    # method to translate the sequence by spliting them into all possible condons in one direction regardless of the frame, takes in a DNA sequence as input and returns a psuedo-protein sequence
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

        return self.frame_translation(self.frame)
    
    # method to filter the transated sequence based on the frame returns a sequence string filtered by the frame
    def frame_translation(self, frame):
        frame_sequence = ""
        for i in range(len(self.translated_sequence)):
            if i % 3 == frame:
                frame_sequence += self.translated_sequence[i]
        return frame_sequence

    # method to translate the codon to the corresponding amino acid returns a single amino acid
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
        

# Initialisiing the class and the parser for cli functinality
# Takes in a DNA sequence and a frame to translate the sequence.
# Output for the sequence is printed to the console
        

if __name__ == "__main__":
    translator = Translator()
    parser = argparse.ArgumentParser(description="Translate DNA sequence to protein sequence")
    
    parser.add_argument('-i', '--input', help="DNA sequence to be translated, takes a fasta string or a file", required=True)
    parser.add_argument('-f', '--frame', type=int, help="Frame to translate the sequence, '0' '1' '2'", default=0)

    args = parser.parse_args()
    # print(args.input, args.frame)

    out = translator.fasta_handler(args.input, args.frame)

    if isinstance(out, str):
        print(out)
    else:
        for i in out:

            print("> %s\n%s" % (i[0], i[1]))

