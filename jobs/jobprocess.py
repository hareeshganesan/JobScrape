from BeautifulSoup import BeautifulSoup

def readProfile():
	for i in range(1):
		f = open("jobs/output"+str(index))
		docs = f.read()
		soup = BeautifulSoup(''.join(docs))
		f.close()
		
		entry = soup.findAll("div", {"class" : "job_layouthead"})[0]
		title = entry.findAll('h1')
		print title