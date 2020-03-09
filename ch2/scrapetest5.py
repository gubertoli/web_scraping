from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords) ~ findAll(limit=1)

# .findAll({"h1", "h2", "h3", "h4", "h5", "h6"}) - retrieve all header tags
# .findAll("span", {"class" : "green", "class": "red"}) - return span tags with class green or reduce
# recursive = True/False until limit

nameList = bsObj.findAll("span", {"class" : "green"})

for name in nameList:
	print(name.get_text())