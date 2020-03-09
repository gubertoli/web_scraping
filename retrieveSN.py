import cfscrape
from bs4 import BeautifulSoup
import re
import pandas as pd
from random import randint
from time import sleep

xls = pd.read_excel(open('CMC_LIST.xls', 'rb'), sheet_name='CMC10')
regex = r"Construction No\.<\/span>, <span class=\"value\">(\d+)<\/span>"



for index, row in xls.iterrows():
	scraper = cfscrape.create_scraper()
	ac = str(row['installed_ac'])
	html = scraper.get("https://planefinder.net/data/aircraft/"+ac).content 
	bsObj = BeautifulSoup(html, features="html.parser")

	content = bsObj.findAll("span")

	matches = re.search(regex, str(content), re.MULTILINE)

	if matches:
		for groupNum in range(0, len(matches.groups())):
			groupNum = groupNum + 1
			print (ac,matches.group(groupNum))
			
	sleep(randint(1,5))
