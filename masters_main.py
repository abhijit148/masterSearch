from BeautifulSoup import BeautifulSoup
from datetime import datetime
import urllib2
from func_getdata import *

now=datetime.now()
now=now.strftime('%Y-%m-%d %H:%M:%S')

keywords=raw_input("Enter Keywords Yo! :")
keywords=keywords.replace(" ","+")

#address="http://www.mastersportal.eu/search/?q=ci-9|kw-graphic+design|lv-master||85eab53a"
address="http://www.mastersportal.eu/search/?q=kw-"+keywords+"|lv-master|mh-face2face||bb5c838c&length=1000"

html = urllib2.urlopen(address).read()

soup = BeautifulSoup(html)
regular_courses = soup.findAll('div', attrs={'class': 'Result master'})
premium_courses = soup.findAll('div', attrs={'class': 'Result master premium'})

courses=regular_courses+premium_courses

#course_data=get_data(courses)
print get_data(courses)
