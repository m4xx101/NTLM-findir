# pip install requests_ntlm

import requests
from requests_ntlm import HttpNtlmAuth
from getpass import getpass
import threading
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-usr','--username', dest = "username", help='AD username/Domain ID')
parser.add_argument('-u','--url',dest = "url", help='Target URL')
parser.add_argument('-w','--wordlist',dest = "wordlist", help='Path to Wordlist')
parser.add_argument('-d','--domain',dest = "domain", help='Domain Name')
args = parser.parse_args()

word_list = open(args.wordlist, 'r')
threads = []
password = getpass()

def checkpassword() :
	response = requests.get(args.url,auth=HttpNtlmAuth('args.domain\\args.username',password))
	if response.status_code == 401:
		print('\n')
		print("401 - Unauthorized: Access is denied due to invalid credentials.")
		exit()
    	
print(''' 
##    ## ######## ##       ##     ##         ######## #### ##    ## ########  #### ########  
###   ##    ##    ##       ###   ###         ##        ##  ###   ## ##     ##  ##  ##     ## 
####  ##    ##    ##       #### ####         ##        ##  ####  ## ##     ##  ##  ##     ## 
## ## ##    ##    ##       ## ### ## ####### ######    ##  ## ## ## ##     ##  ##  ########  
##  ####    ##    ##       ##     ##         ##        ##  ##  #### ##     ##  ##  ##   ##   
##   ###    ##    ##       ##     ##         ##        ##  ##   ### ##     ##  ##  ##    ##  
##    ##    ##    ######## ##     ##         ##       #### ##    ## ########  #### ##     ## v1.0  ''')

checkpassword()

try:
	def scan(word):
		url = args.url+word
		session = requests.Session()
		session.auth = HttpNtlmAuth('args.domain\\args.username',password)
		response = session.get(url)
		if response.status_code == 200:
			print(args.url)
		else :
			print(word,end="\r")
	   	        
	for word in word_list:
		striped_word = word.strip()
		t1 = threading.Thread(target=scan,args=(striped_word,))
		threads.append(t1)
		t1.start()
	
	for thread in threads:
	    thread.join()

#If keyboard interruption happens 
except KeyboardInterrupt:
    print("Someone pressed CTRL+C.....")
    exit()
#Other errors
except:
    print("Somthing went wrong!")
    exit()
