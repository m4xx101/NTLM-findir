# NTLM-findir

NTLM-findir is simple python script written by me to do directory bruteforcing on web application which required NTLM base authentication 

This tool is majorly used for intranet web application which required AD Creds for login 

## Usage

```sh

███╗   ██╗████████╗██╗     ███╗   ███╗      ███████╗██╗███╗   ██╗██████╗ ██╗██████╗       
████╗  ██║╚══██╔══╝██║     ████╗ ████║      ██╔════╝██║████╗  ██║██╔══██╗██║██╔══██╗      
██╔██╗ ██║   ██║   ██║     ██╔████╔██║█████╗█████╗  ██║██╔██╗ ██║██║  ██║██║██████╔╝      
██║╚██╗██║   ██║   ██║     ██║╚██╔╝██║╚════╝██╔══╝  ██║██║╚██╗██║██║  ██║██║██╔══██╗      
██║ ╚████║   ██║   ███████╗██║ ╚═╝ ██║      ██║     ██║██║ ╚████║██████╔╝██║██║  ██║      
╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝     ╚═╝      ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═╝v2.0  


usage: NTLM-FINDIR.py [-h] [-user USERNAME] [-u URL] [-w WORDLIST] [-d DOMAIN] [-t THREAD] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -user USERNAME, --username USERNAME
                        AD username/Domain ID
  -u URL, --url URL     Target URL
  -w WORDLIST, --wordlist WORDLIST
                        Path to Wordlist
  -d DOMAIN, --domain DOMAIN
                        Domain Name
  -t THREAD, --thread THREAD
                        Threads Counts
  -o OUTPUT, --output OUTPUT
                        output path
```

