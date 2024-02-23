## Nucleotide Translator

This is a webapp built using flask to run the nctranslator library. The frontend was styled using Tailwindcss and the backend was written in Flask and minor JS logic to clear the forms. Along side running the Translator it can also query Blast servers hosted by NCBI with the resulting Amino acid sequences.

The project has no Node requirements to run as is, but requires Node to make server side changes.

The project also hasn't been tested on 'Production' build, was only tested using the developmental build on localhost.

### Running the project

Clone the repo using  

` git clone -b webapp https://github.com/c3060866/bioapp `

Install requirements using (Virtual Environment Higly recommened)  
` pip install -r "requirements.txt" `

Run the main.py file to start server on localhost:5000  

` python main.py `  
or   
` python3 main.py `  
incase of a linux system

Visit http://localhost:5000/ to use the app.

### Current Limitations
Can deal with only one sequence at a time, can easily process multiple but visualising and dealing with sending multiple query requests at once needs to be implemented.
Stores data per user session data is lost on reload.
