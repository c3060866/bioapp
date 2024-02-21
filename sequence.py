

class Nucleotide:

    ''' 
    This class is used to represent a nucleotide in a DNA sequence.
    The class has a single attribute, nucleotide, which is a string.
    The class has a single method, add_nucleotide, which checks if the nucleotide is valid and then adds it to the sequence.
    The class also takes in RNA nucleotides and converts them to DNA nucleotides.
    @param nucleotide: A string representing a nucleotide in a DNA sequence.

    '''

    def __init__(self, nucleotide):

        self.nucleotide = nucleotide
        # print(len(self.nucleotide))
        # print(self.nucleotide)
        # print(type(self.nucleotide))
        self.fixed_nucleotide = ''
        self.add_nucleotide()

    def check_nucleotide(self):
        if self.nucleotide in ['A', 'T', 'C', 'G']:
            
            return True
        else:
            
            return False
        
    def fix_nucleotide(self):
        if self.nucleotide in ['a', 't', 'c', 'g', 'A', 'T', 'C', 'G']:
            return self.nucleotide.upper()
        elif self.nucleotide in ['u', 'U']:
            return 'T'
        elif self.nucleotide.isalpha():
            return 'N'
        else:
            raise ValueError('Invalid Nucleotide')
            
        
    def add_nucleotide(self):
        if self.check_nucleotide():
            self.fixed_nucleotide = self.nucleotide
        elif not self.check_nucleotide():
            self.fixed_nucleotide = self.fix_nucleotide()
        
    def __str__(self):
        return self.fixed_nucleotide
    
    def __repr__(self):
        return self.fixed_nucleotide
    
class Sequence:
    ''' 
    This class is used to represent a DNA sequence.
    The class has a single attribute, sequence, which is a string.
    The class has a single method, add_nucleotide, which adds a nucleotide to the sequence.
    The class also has a method, __len__, which returns the length of the sequence.
    @param sequence: A string representing a sequence of nucleotides in a DNA sequence.

    '''
    def __init__(self, sequence):
        self.sequence = sequence
        self.fixed_sequence = []
        self.add_nucleotide()

        
    def add_nucleotide(self):
        for i in self.sequence:
            nuc = Nucleotide(i)
            self.fixed_sequence.append(nuc)
            

    def list(self):
        return self.fixed_sequence
    
    def __getitem__(self, index):
        return self.fixed_sequence[index]
        
    def __len__(self):
        return len(self.fixed_sequence)
    
    def __str__(self):
        strrep = ''.join([str(i) for i in self.fixed_sequence])
        return str(strrep)
    
    def __repr__(self):
        return str(self.fixed_sequence)
    
    


# seq = Nucleotide('b')
# print(len(seq))

# nuc2 = Nucleotide("a")
# print(nuc2)
    
# seq = Sequence("ATCGGTGCAGTAGCDBM")
# print(type(seq[2]))