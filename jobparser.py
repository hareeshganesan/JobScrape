from BeautifulSoup import BeautifulSoup

def readProfile():
	for i in range(5):
		index = i+7
		f = open("output"+str(index))
		docs = f.read()
		soup = BeautifulSoup(''.join(docs))
		f.close()
		
		f = open("links",'a')
		print soup.prettify()
		
		entries = soup.findAll("td", {"class" : "text_data"})
		for entry in entries:
			link = entry.findAll('a')
			if(link!=[]):
				f.write("http://duke.experience.com"+link[0]['href']+"\n")
		
		
def readLinks():
	f = open("links")
	links = []
	g = open("events_script", 'wb')
	
	index = 0
	for line in f:
		# http://duke.experience.com/er/stu/opportunities/job_profile.jsp?job_hnd=27515590&affiliation_hnd=14272
		#g.write("curl --dump-header headers_and_cookies"+str(index)+" -kvd \"x=34&y=13&scheme=http&username=dukehg30&password=skarlath5\" http://duke.experience.com/er/security/login.jsp?returnto="+(line[0:(len(line)-23)]).strip().replace("http://duke.experience.com","")+"\n")

		g.write("curl --cookie  headers_and_cookies -kv " + (line[0:(len(line)-23)]).strip().replace('/er','/er/stu') + " > jobs/link"+str(index)+" \n")
		index+=1

def processJobs():
	f = open("jobs/link0")
	docs = BeautifulSoup(''.join(f.read()))
	attrs = docs.findAll("tr",{"class": "displayRow"})
	for attr in attrs:
		print attr
		print "\n\n\n"
#readProfile()
#readLinks()
processJobs()