import requests
from requests_ntlm import HttpNtlmAuth
from getpass import getpass
import threading
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-usr','--username', dest = "username", help='AD username/Domain ID')
parser.add_argument('-u','--url',dest = "url", help='Target URL')
parser.add_argument('-w','--wordlist',dest = "wordlist", help='Path to Wordlist')
args = parser.parse_args()
geturl = args.url

word_list = open(args.wordlist, 'r')
threads = []
password = getpass()
print(''' 
##    ## ######## ##       ##     ##         ######## #### ##    ## ########  #### ########  
###   ##    ##    ##       ###   ###         ##        ##  ###   ## ##     ##  ##  ##     ## 
####  ##    ##    ##       #### ####         ##        ##  ####  ## ##     ##  ##  ##     ## 
## ## ##    ##    ##       ## ### ## ####### ######    ##  ## ## ## ##     ##  ##  ########  
##  ####    ##    ##       ##     ##         ##        ##  ##  #### ##     ##  ##  ##   ##   
##   ###    ##    ##       ##     ##         ##        ##  ##   ### ##     ##  ##  ##    ##  
##    ##    ##    ######## ##     ##         ##       #### ##    ## ########  #### ##     ## v1.0 By m4xx!  ''')

try:
	def scan(word):
		url = args.url+word
		session = requests.Session()
		session.auth = HttpNtlmAuth('nseroot\\args.username',password)
		#response = requests.get(url,auth=HttpNtlmAuth('nseroot\\hmt_aprasad',password))
		response = session.get(url)
		if response.status_code == 200:
			print(args.url)
		else :
		 	print(args.url+word,end="\r")
	        
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
