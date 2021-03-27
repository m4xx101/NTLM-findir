import requests
from requests_ntlm import HttpNtlmAuth
from getpass import getpass
import threading
import argparse
import concurrent.futures

print(''' 
███╗   ██╗████████╗██╗     ███╗   ███╗      ███████╗██╗███╗   ██╗██████╗ ██╗██████╗ 
████╗  ██║╚══██╔══╝██║     ████╗ ████║      ██╔════╝██║████╗  ██║██╔══██╗██║██╔══██╗
██╔██╗ ██║   ██║   ██║     ██╔████╔██║█████╗█████╗  ██║██╔██╗ ██║██║  ██║██║██████╔╝
██║╚██╗██║   ██║   ██║     ██║╚██╔╝██║╚════╝██╔══╝  ██║██║╚██╗██║██║  ██║██║██╔══██╗
██║ ╚████║   ██║   ███████╗██║ ╚═╝ ██║      ██║     ██║██║ ╚████║██████╔╝██║██║  ██║
╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝     ╚═╝      ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═╝v2.0 by m4xx101''')

print('\n')

def arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-user','--username', dest = "username", help='AD username/Domain ID')
	parser.add_argument('-u','--url',dest = "url", help='Target URL')
	parser.add_argument('-w','--wordlist',dest = "wordlist", help='Path to Wordlist')
	parser.add_argument('-d','--domain',dest = "domain", help='Domain Name')
	parser.add_argument('-t','--thread',dest = "thread", help='Threads Counts', default=27)
	parser.add_argument('-o','--output',dest = "output", help='output path')
	args = parser.parse_args()
	return args

args = arguments()
word_list = open(args.wordlist, 'r')
threads = []
words=[]
password = getpass()
def checkpassword():
    response = requests.get(args.url,auth=HttpNtlmAuth('{}\\{}'.format(args.domain,args.username),password))
    if response.status_code == 401:
    	print('\n')
    	print("401 - Unauthorized: Access is denied due to invalid credentials.")
    	exit()

checkpassword()

with open(args.wordlist, 'r',encoding="utf8") as file:
	a = file.readlines()
	for i in a:
		words.append(i.strip())
try:
	def scan(word):
			url = args.url+'/'+word
			session = requests.Session()
			session.auth = HttpNtlmAuth('{}\\{}'.format(args.domain,args.username),password)
			response = session.get(url)
			if response.status_code == 200:
				print(url)
				if args.output:
					with open("{}".format(args.output), 'a') as f:
						f.write(url+"\n")		
			else :
				print('/'+word,end="\r")

	if args.thread:
		thread_count = int(args.thread)
	else:
		print('Lol')

	with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
	    executor.map(scan, words)

	
#If keyboard interruption happens 
except KeyboardInterrupt:
    print("Someone pressed CTRL+C.....")
    exit()
#Other errors
except:
    print("Somthing went wrong!")
    exit()
