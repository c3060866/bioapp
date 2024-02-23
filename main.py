from flask import Flask, render_template, request, redirect, url_for, session
from nctranslator.nctranslator import *
import requests
import time
from bs4 import BeautifulSoup, Comment

# Web application using Flask to handle the fasta sequence and blast query using the library nctranslator.

app = Flask(__name__)
app.secret_key = 'secret10101090'

@app.route('/', methods=['GET', 'POST'])
def index():
    
    # Function to handle the fasta sequence using the Translator class
    def fasta_handler(sequence, frame):
        translator = Translator()
        out = translator.fasta_handler(sequence, frame)
        
        return out
    # Handle form submit
    if 'submit_button' in request.form:
        # Form submitted, process the data
        if request.form['submit_button'] == 'Submit':
            session['sequence'] = request.form.get('sequence', "")
           
            session['frame'] = request.form.get('frame', "0")

            session['out'] = fasta_handler(session['sequence'], int(session['frame']))
            print(session['out'])
            return render_template('index.html', output=[session['out'][0]], input=session['sequence'], frame=session['frame'])
        
        elif request.form['submit_button'] == 'Reset':
            return redirect(url_for('index'))
        
        else :
            pass
    else:
        # Initial page load, show empty form
        
        return render_template('index.html')

@app.route('/query', methods=['POST'])
# query function to handle the blast query
def query():
    url = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi'
    seq = request.form.get('sequence', "")
    # Function to post the blast query to the NCBI server, by default the database is set to 'nr'
    def post_query(url, query):
        parameters = {
        'QUERY': query,
        'DATABASE': 'nr',
        'PROGRAM': 'blastp',
        'CMD': 'Put'
        }
        try:
            response = requests.post(url, data=parameters)
            
            if response.status_code == 200:
            # Extract the RID (Request Identifier) and rtoe(Estimated time of completion) from the response using bs4 to parser the html response
                soup = BeautifulSoup(response.content, 'html.parser')
                comments = soup.find_all(string=lambda text: isinstance(text, Comment) and 'QBlastInfoBegin' in text)
                # print(comments)
                print(len(comments))
                rid = comments[0].split('\n')[1].split(' = ')[1]
                rtoe = comments[0].split('\n')[2].split(' = ')[1]
                for i in session['out']:
                    if i[1] == query:
                        i.append(rid)
                        i.append(rtoe)
                        i.append('WAITING')
                    print(i)
                
                # render_template('index.html', output=session['out'], input=session['sequence'], frame=session['frame'])
                    # While loop to check the status of the query, if the status is 'WAITING' or 'UNKNOWN' the loop will continue to check the status of the query
                    ti = 0
                    while i[4] in ['WAITING', 'UNKNOWN']:
                        
                        time.sleep(30)
                        status = get_status(i[2])
                        i[4] = status

                        ti += 1

                        # Timeout for the query, if the query takes more than ~2.5 minutes to complete, exits loop and returns 'TOOLONG'
                        if ti > 5:
                            status = 'TOOLONG'
                            i[4] = status

                            return render_template('index.html', output=session['out'], input=session['sequence'], frame=session['frame'])
                            
                        #  Error handling for the query, if the status is 'UNKNOWN' the loop will exit and return 'Error: UNKNOWN'
                        if status == 'UNKNOWN':
                            return f"Error: {status}"
                        
                        # return render_template('index.html', output=session['out'], input=session['sequence'], frame=session['frame'])
                    # If the status is 'READY' the loop will exit and return the result of the query
                    if status == 'READY':
                        i[4] == status

                    return render_template('index.html', output=session['out'], input=session['sequence'], frame=session['frame'])

                
            else:
                return f"Error: {response.status_code}"

        except requests.exceptions as e:
            print(e)
            return f"Error: {e}"
        
    # Function to get the status of the query using RID (Request Identifier)
    def get_status(rid):
        get_parameters = {
            'CMD': 'Get',
            'RID': rid,
            'FORMAT_OBJECT' : 'SearchInfo'
        }

        try:
            response = requests.get(url, params=get_parameters)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                comments = soup.find_all(string=lambda text: isinstance(text, Comment) and 'QBlastInfoBegin' in text)
                status = comments[0].split('\n')[2].split('=')[1]
                print(status)

                return status
            else:
                return f"Error: {response.status_code}"


        except requests.exceptions as e:
            print(e)
    
    return post_query(url, seq)
        

if __name__ == '__main__':
    app.run(debug=True)