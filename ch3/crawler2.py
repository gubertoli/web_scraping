# track and collect data

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


pages = set()

def getLinks(pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj = BeautifulSoup(html, features="html.parser")
	
	try:
		# article title h1->span
		print(bsObj.h1.get_text())
		# first paragraph
		print(bsObj.find(id="mw-content-text").findAll("p")[0])
		# edition link
		print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
	
	except AttributeError:
		print("This page is missing something! No worries though!")
	
	for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				# new page
				newPage = link.attrs['href']
				print("--------------\n"+newPage)
				pages.add(newPage)
				getLinks(newPage)

# "" go to wikipedia home
getLinks("")