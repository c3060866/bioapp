import requests
import json
from bs4 import BeautifulSoup, Comment


# from nctranslator.nctranslator import Translator
# sequence = """>3
# GATGCATGTGTTATGCGTGATtgtgtcgatgagtagca
# atgctagtatgcgtgtagtcgtaacgtacgtaatatatgcggcga"""
# test = Translator()
# print(test.fasta_handler(sequence, 1))

url = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi'

query1 = "MKKCACKSDYHTTT"

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
        # Extract the RID (Request Identifier) from the response
            soup = BeautifulSoup(response.content, 'html.parser')

            soup = BeautifulSoup(response.content, 'html.parser')
            comments = soup.find_all(string=lambda text: isinstance(text, Comment) and 'QBlastInfoBegin' in text)
            # print(comments)
            print(len(comments))
            rid = comments[0].split('\n')[1].split(' = ')[1]
            rtoe = comments[0].split('\n')[2].split(' = ')[1]
            print(rid, rtoe)

            return [rid, rtoe]


        # Find the input element with name 'RID'
            # rid_input = soup.find('input', {'name': 'RID'})

            # # Extract the value of the RID input element
            # if rid_input:
            #     rid = rid_input.get('value')
            # else :
            #  rid = None
            
            # print( rid)
    except requests.exceptions as e:
        print(e)


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

            
            # print(comments)
            # print(len(comments))

    except requests.exceptions as e:
        print(e)


# comment = ['QBlastInfoBegin\n    RID = XFJE56NV013\n    RTOE = 48\nQBlastInfoEnd\n']
# rid = comment[0].split('\n')[1].split(' = ')[1]
# rtoe = comment[0].split('\n')[2].split(' = ')[1]
# print(rid, rtoe)

status = ['\n                QBlastInfoBegin\n\t                Status=READY\n                QBlastInfoEnd\n                ', '\nQBlastInfoBegin\n\tThereAreHits=no\nQBlastInfoEnd\n']


# result_parameters = {
#     'CMD': 'Get',
#     'RID': 'rid',
# }

# try:
#     response = requests.get(url, params=result_parameters)
#     if response.status_code == 200:
#         print(response.content)
#         # soup = BeautifulSoup(response.content, 'html.parser')
#         # comments = soup.find_all(string=lambda text: isinstance(text, Comment) and 'QBlastInfoBegin' in text)

        
#         # print(comments)
#         # print(len(comments))

# except requests.exceptions as e:
#     print(e)
post_query(url, query1)
get_status('XFJE56NV013')