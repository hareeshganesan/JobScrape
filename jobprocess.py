from BeautifulSoup import BeautifulSoup
import re
import json
import sqlcreate 
import sqlite3

def fixStr(input):
	return str(input).replace("'","[ap]").replace(",","[co]")
	
def readProfile():
	all_jobs = []
	for i in range(495):
		print i
		f = open("jobs/link"+str(i))
		docs = f.read()
		soup = BeautifulSoup(''.join(docs))
		f.close()
		
		r= {}
		title_enclose = soup.findAll("div", {"class" : "job_layouthead"})[0]
		title = title_enclose.findAll('h1')[0].string.strip()
		r["title"] = fixStr(title)
		
		job_overview1_vals = soup.findAll("div", {"class" : "joboverviewPart1"})[0].findAll("span",{"class": "displayValue"})
		r["date"] = job_overview1_vals[0].string.strip()
		r["pay_type"] = fixStr(job_overview1_vals[1].string.strip())
		
		
		job_overview2_vals = soup.findAll("div", {"class" : "joboverviewPart2"})[0].findAll("span",{"class": "displayValue"})
		r["opp_type"] = job_overview2_vals[0].string.strip()
		r["hours_type"] = job_overview2_vals[1].string.strip()
		if(len(job_overview2_vals) > 2):
			r["compensation"] = fixStr(job_overview2_vals[2].string.strip())
		else:
			r["compensation"] = "undefined"
			
		#r["interviews"] = soup.findAll("div",{"class": "interviewschedules"})
		if(not(soup.find(text="Location:")==None)):
			r["location"] = fixStr(soup.findAll("div", {"class":"jobdetails"})[0].findAll("table")[0].findAll("tr")[0].findAll("td")[0].contents[3].strip())
		else:
			r["location"]="undefined"
		description_set = soup.findAll("div", {"class":"jobdetails"})[0].findAll("table")[0].findAll("tbody",{"class":"descriptionblock"})[0].findAll("tr", {"class":"displayRow"})[0].findAll("td")[0]
		description = ""
		for part in description_set:
			if(not('<' in str(part))):
				description += str(part).strip()+"\n"
		r["description"] = fixStr(description)
		
		contact_details = soup.findAll("span",{"class": "displayValue contactText"})
		
		if(len(contact_details)>0):
			r["contact_details"] = fixStr(soup.findAll("span",{"class": "displayValue contactText"})[0].contents[0].strip())
		else:
			r["contact_details"] = "undefined"
			
		s = soup.findAll("table")
		if(len(s[len(s)-2].findAll("tr"))>0):
			deadline_html = s[len(s)-2].findAll("tr")[0].findAll("td")[0]
			deadline = ""
			for part in deadline_html.contents:
				if(not('<' in str(part))):
					deadline += str(part).strip()
			r["deadline"] = fixStr(deadline)
		else:
			r["deadline"]="undefined"
		all_jobs.append(r)
	print "Done reading"
	print all_jobs
	f = open('processed_jobs.json', 'w')
	f.write(json.dumps(all_jobs, sort_keys = True, indent= 4))
	f.close()
	return all_jobs


	
#jobs = readProfile()

#sqlcreate.importJSON('processed_jobs.json')
