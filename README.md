## Nucleotide Translator

A simple program to translate Nucleotide sequences into protien sequences.

### Structure

The repository has three branches master, build and webapp. `master` was used for the inital development of the program, it has three python files `nctranslator.py`, `sequence.py` and `test.py`.  
`sequence.py` contains two classes `Nucleotide` and `Sequence` which is used to store the input in a structured manner. `nctranslator.py` contains the main program which uses the two mentioned classes and return
translated sequences in a string/ fasta string depending on the input. The program does not use a specific organism as a refrenece for the translation process, rather looks at all possible encodable Amino acid. It can also translate in three different frames in the forward direction
and deal with both DNA and RNA sequences. 

`build` manages publishing the app to make it easier to distribute and cross platform compatible. More details can be found on the branch.  

`webapp` is a Flask based web application that demonstates a use case for the app. It can be hosted to run server side as it uses minimal resources and can send the results to NCBI blastp for further analysis. It uses the BLAST API documentation of which can be
found here(https://ncbi.github.io/blast-cloud/dev/using-url-api.html).


## Usage 
It is a fully functional cli app, but would recommend using Releases under the `build` branch.

Run from cli using to see the help dialog  
` python nctranslaor.py --help `  

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
```
  from nctranslator.nctranslator import * 

    translator = Translator() 
    output = translator.fasta_handler(sequence, frame)
    # Where sequence is you input and frame is the reading frame
```

### Please See
I have used Unittests but only for the sequence.py file. The build branch has tags and versioning over the master branch. The webapp is not ready for production cause of a couple of error handling oversight. I haven't tried deploying it on no windows systems.
I have some experience in webdev hence I am unsure how to site the methods and functions I have used, although the realworld applications are lacking I hope this project help demonstrate my knowledge in programming.
