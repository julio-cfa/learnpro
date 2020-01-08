#!/usr/bin/python3
#Made in Tokyo - v1.0

import requests, sys, colorama
from colorama import *


# In this part of the code, we are checking whether there is an argument after th e script's name or not. When are using 'sys.argv', the argument that is set as 0 is the script's name, that's why we are using the number 1 here. Therefore, if the length of sys.argv equals one, that is, if there's only the script's name in the command line, then what is inside 'help_bull.txt' will be printed out.

if len(sys.argv) == 1:
	with open('docs/help_bull.txt', 'r') as bull_help:
		print(bull_help.read())	

# Here, we are checking whether the first argument passed right after the script's name is '-h' or '--help'. If it is either one, then what is inside the 'help_bull.txt' will be printed out, just as if there was no argument - as seen above.

elif (sys.argv[1] == '-h') or (sys.argv[1] == '--help'):
	with open('docs/help_bull.txt', 'r') as bull_help:
		print(bull_help.read())

else:

	url1 = sys.argv[1]
	if "/" in url1[-1]:
		url1 = url1.rstrip('/')

	if len(sys.argv) == 2:
		wordfile = 'docs/common.txt'

	else:
		wordfile = sys.argv[2]

	
	wordlist = open(wordfile, 'r')
	for line in wordlist:

		if ("https://" in url1) or ("http://" in url1):
			line = line.replace('\n', '')
			url_usada = (f"{url1}/{line}")
	

			cookies1 = {"JSESSIONID": ""}
			headers1 = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0"}


			r = requests.get(url_usada, headers=headers1, cookies=cookies1)
			
			if (r.status_code == 200) or (r.status_code == 302):
				print(f"{Fore.CYAN} {url_usada} - {r.status_code}")

			else:
				print(f"{Fore.BLUE} {url_usada} - {r.status_code}")
		
		else:
			print("URL does not contain 'https://' nor 'http://', try again including the protocol you want at the beginning of the URL")
			break


