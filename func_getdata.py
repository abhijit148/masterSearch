from datetime import datetime
from uni_rank import *
import time

now=datetime.now()
now=now.strftime('%Y-%m-%d %H:%M:%S')

def get_data(courses):
	data=()
	header=("degree","course_name","univeristy","rank_arwu","rank_qs","location","course_date","duration","eeacost","noneeacost","more")
	data+=(header,)
	for course in courses:
		#print course
		#Course Details using Scraping of MastersPortal.eu
		course_degree=getdegree(course)
		course_name=getname(course)
		course_uni=getuni(course)
		course_loc=getloc(course)
		course_date=getdate(course)
		course_duration=getduration(course)
		course_more=getmore(course)
		course_eeacost=geteeacost(course)
		course_noneeacost=getnoneeacost(course)

		course_uni=course_uni.replace(',',' ')

		#if (course_noneeacost=="Not Specified"):
			#Costs using WolframAlpha API. This will be a 2-element Array. Element 0 is Local Students Cost and Element 1 is Foreign Students Cost
		#	course_cost=getcost(course_uni)
		try:
			unirank_arwu=getarwu(course_uni)
		except:
			try:
				#time.sleep(30)
				unirank_arwu=getarwu(course_uni)
			except:
				unirank_arwu="Not Found"

		try:
			unirank_qs=getqs(course_uni)
		except:
			try:
				#time.sleep(30)
				unirank_qs=getqs(course_uni)
			except:
				unirank_qs="Not Found"


		datarow=(course_degree,course_name,course_uni,unirank_arwu,unirank_qs,course_loc,course_date,course_duration,course_eeacost,course_noneeacost,course_more)
		data+=(datarow,)
	
	filename="results/masters ["+now+"].csv"
	with open(filename, 'wb') as f:
		for row in data:
			for element in row:
				f.write(element.encode('ascii','ignore')+"\t")
			f.write('\n')
	print "CSV generated at "+now
	return data

def getdegree(course):
	try:
		heading=course.find('h3')
		link=heading.find('span')
		return link.contents[0]
	except:
		return "Degree Error"

def getname(course):
	try:
		heading=course.find('h3')
		link=heading.find('a')
		link=str(link)
		link=link.replace('</a>',"")
		index=link.find('/span') + 7
		name=link[index:]
		return name
	except:
		return "Name Error"

def getuni(course):
	try:
		ulist=course.find('ul', attrs={'class': 'Organisations face2face'})
		link=ulist.find('a')
		return link.contents[0]
	except:
		return "Uni Error"

def getloc(course):
	try:
		ulist=course.find('ul', attrs={'class': 'Venues Compact'})
		link=ulist.find('a')
		return link.contents[0]
	except:
		return "Loc Error"


def getdate(course):
	try:
		ulist=course.find('ul', attrs={'class': 'StartDate Expandable'})
		li=ulist.find('li')
		data=li.contents[0]
		data=data.replace('&nbsp;'," ")
		return data
	except:
		return "Date Error"

def getduration(course):
	try:
		td=course.find('td', attrs={'class': 'Value Duration'})
		abbr=td.find('abbr')
		return abbr.contents[0]
	except:
		return "Duration Error"

def getmore(course):
	try:
		heading=course.find('h3')
		link=heading.find('a')
		link=str(link)
		index=link.find('"') + 1
		link=link[index:]
		index=link.find('"')
		link=link[:index]
		return link
	except:
		return "More Error"

def geteeacost(course):
	try:
		ulist=course.find('ul', attrs={'class': 'TuitionFee Expandable'})
		li=ulist.find('li', attrs={'class': 'eea'})
		abbr=li.find('abbr')
		data=abbr.contents[0]
		data=data.replace('&euro;',"Euro")
		data=data.replace('&nbsp;'," ")
	except:
		data = "Not Specified"
	return data

def getnoneeacost(course):
	try:
		ulist=course.find('ul', attrs={'class': 'TuitionFee Expandable'})
		li=ulist.find('li', attrs={'class': 'noneea'})
		abbr=li.find('abbr')
		data=abbr.contents[0]
		data=data.replace('&euro;',"Euro")
		data=data.replace('&nbsp;'," ")
	except:
		data = "Not Specified"
	return data