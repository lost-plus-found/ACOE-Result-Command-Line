import urllib2
from bs4 import BeautifulSoup
from prettytable import PrettyTable

page = open('./.temp', 'r').read()
soup = BeautifulSoup(page, "lxml")
results = soup.findAll('table')

res = ['REGULAR', 'ARREAR', 'REVALUATION']
i = 0
for result in results:
	if result.findParent('table') is None:
		print "\t\t\t\t%s" % res[i]
		t = PrettyTable(['Subject Code', 'Subject Name', 'Grade'])
		for tr in result.find_all('tr')[1:]:
			tds = tr.find_all('td')
			t.add_row([tds[0].text, tds[1].text, tds[2].text])
		print t
		print "\n"
		i+=1
