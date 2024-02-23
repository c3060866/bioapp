## Nucleotide Translator

Alternative Branch to maintain a distribusion environment. 

## Usage 

Find releases under the build folder or releases tab.

Install using
` pip install nctranslator-0.*.0.tar.gz `  

Run from cli using to see the help dialog  
` nctranslator ` or ` nctranslaor --help `  

```
usage: nctranslator [-h] [-i INPUT] [-f FRAME]

Translate DNA sequence to protein sequence

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        DNA sequence to be translated, takes a regular string, fasta string or a file
  -f FRAME, --frame FRAME
                        Frame to translate the sequence, '0' '1' '2'

```

To use in modules import using 
``` from nctranslator.nctranslator import * 

    translator = Translator() 
    output = translator.fasta_handler(sequence, frame)
    # Where sequence is you input and frame is the reading frame ```

