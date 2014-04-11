from BeautifulSoup import BeautifulSoup
import urllib2

def getarwu_data():
	arwu_ranks={}

	address="http://www.shanghairanking.com/ARWU2013.html"
	#print address
	html = urllib2.urlopen(address).read()
	soup = BeautifulSoup(html)
	table = soup.find('table',attrs={'id': 'UniversityRanking'})
	rows=table.findAll('tr')
	rows=rows[1:]

	for row in rows:
		#print row
		td_data=row.findAll('td')
		arwu_ranks[td_data[1].find('a').contents[0]]=td_data[0].contents[0]

	return arwu_ranks