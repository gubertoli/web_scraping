from urllib.request import urlopen
from bs4 import BeautifulSoup
try:
	html = urlopen("http://pythonscraping.com/pages/page1.html")
	if html is None:
		print("URL not found")
	else:
		bsObj = BeautifulSoup(html.read(), features="html.parser")
		try:
			print(bsObj.h1)
		except AttributeError as e:
			print("Tag was not found")
except HTTPError as e:
	print(e)