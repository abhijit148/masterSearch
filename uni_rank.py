from BeautifulSoup import BeautifulSoup
import urllib2
from google import *
import data_load

arwu_data=data_load.getarwu_data()

def getarwu(uni,arwu_ranks=arwu_data):
	query="site:shanghairanking.com "+uni
	search_results = Google.search(query)
	first_result=search_results[0]
	key=first_result.link
	
	index1=key.find('World-University-Rankings/')
	index2=key.find('.html')
	key=key[index1+26:index2]
	key=key.replace('-',' ')
	
	return arwu_ranks[key]

def getqs(uni):
	query="site:topuniversities.com node world"+uni
	search_results = Google.search(query)
	first_result=search_results[0]
	link=first_result.link
	index=link.find('&')
	link=link[7:index]

	address=link+"/ranking-details"
	print address
	html = urllib2.urlopen(address).read()
	soup = BeautifulSoup(html)
	tr_data = soup.findAll('tr')
	tr=tr_data[1]
	td = tr.findAll('td')
	rank= td[-1].contents[0]
	return rank