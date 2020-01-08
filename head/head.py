#!/usr/bin/python3
# Made in Lyon, revised in Tokyo

import requests, sys, colorama
from colorama import *

# First colour is golden brown, second is cyan, and third is red. You can understand more about colours here: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
COLORS = ["\033[0;33m", "\033[0;36m", "\033[1;31m"]	

if len(sys.argv) == 1:
	print("The script expects a URL containing 'http://' or 'https://.' Please, provide a valid URL.")

else:


# The URL is passed as an argument in the command line, the 'headers' variable contains the user-agent and the 'security_headers' list contains all the security headers to be tested.
	url = sys.argv[1]
	headers1 = {"User-Agent": "Mozilla/5.0 (Window s NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
	security_headers = ["STRICT-TRANSPORT-SECURITY", "PUBLIC-KEY-PINS", "X-FRAME-OPTIONS", "X-XSS-PROTECTION", "X-CONTENT-TYPE-OPTIONS", "CONTENT-SECURITY-POLICY", "X-PERMITTED-CROSS-DOMAIN-POLICIES", "REFERRER-POLICY", "EXPECT-CT", "FEATURE-POLICY", "CONTENT-SECURITY-POLICY-REPORT-ONLY", "X-PAGE-SPEED", "ACCESS-CONTROL-ALLOW-ORIGIN"]

# Here we are executing the request and defining X as the response headers 
	req = requests.get(url, headers=headers1)
	x = (req.headers)

# Then we print the URL and the security headers found and not found by using two 'FOR LOOPS', as seen below
	print(f"{COLORS[0]}\nTarget URL: {url}:\n", Style.RESET_ALL)
	print('''This tool aims to test whether the target website has all the
necessary security headers or not. To know more about it, please
check https://www.owasp.org/index.php/OWASP_Secure_Headers_Project.\n''')

	print(COLORS[1] + "HTTP Security Headers Found:\n", Style.RESET_ALL)
	for y in x:
		y=y.upper()
		if y in security_headers:
			print(y.title())

	print(f"{COLORS[2]} \nHTTP Security Headers NOT Found:\n", Style.RESET_ALL)
	for y in security_headers:
		if (y) not in (req.headers):
			print(y.title())