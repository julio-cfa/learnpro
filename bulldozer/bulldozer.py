#!/usr/bin/python3
#Made in Tokyo - v1.0

import requests, sys

if ('-h' in sys.argv[1]) or ('--help' in sys.argv[1]):
	with open('help_bull.txt', 'r') as bull_help:
		print(bull_help.read())

else:

	url1 = sys.argv[1]
	if "/" in url1[-1]:
		url1 = url1.rstrip('/')

	if len(sys.argv) == 2:
		wordfile = 'common.txt'

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
			print(f"{url_usada} - {r.status_code}")
		
		else:
			print("URL não contém 'https://' ou 'http://', tente novamente incluindo o protocolo")
			break


