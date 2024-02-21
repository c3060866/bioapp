

class Nucleotide:
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
    

seq = Nucleotide('b')
# print(len(seq))

# nuc2 = Nucleotide("a")
# print(nuc2)