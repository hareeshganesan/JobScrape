import csv
import sqlite3
import uuid
import sys
import json

def importJSON(jobfile):
  f = open(jobfile)
  jobstr = f.read()
  f.close()
  jobs = json.loads(jobstr)
  conn = sqlite3.connect('jobscrapedata')
  c = conn.cursor()
  c.execute('''create table jobs (jobid text, compensation text, contact_details text, date text, deadline text, description text, hours_type text, location text, opp_type text, pay_type text, title text)''')
  i=1
  for job in jobs:
  	jobid = str(uuid.uuid4()).replace('-','')
  	print str(i)+jobid
  	command =  "insert into jobs values('"+jobid+"','"+job["compensation"]+"','"+job["contact_details"]+\
  	"','"+job["date"]+"','"+job["deadline"]+"','"+job["description"]+"','"+job["hours_type"]+"','"+\
	job["location"]+"','"+job["opp_type"]+"','"+job["pay_type"]+"','"+job["title"]+"')"
  	c.execute(command)
	i+=1
  conn.commit()
  c.close()
  



def populate(inputData):
  read = csv.reader(open(inputData, 'rb'), delimiter = '|')
  disp_info = []

  conn = sqlite3.connect('/tmp/example')
  c = conn.cursor()
  c.execute('''create table cases (caseid text, background text, holding text, plaintiff boolean, ada boolean, type boolean, completed boolean)''')

  index=0
  for row in read:
	  if(index==0):
		  print row
	  index=1	
	  caseid = str(uuid.uuid4()).replace('-','')
	  print caseid
	  command =  "insert into cases values('"+caseid+"','"+row[7].replace("'","[ap]")+"','"+row[8].replace("'","[ap]")+"','FALSE','FALSE','FALSE','FALSE')"
	  c.execute(command)

  conn.commit()
  c.close()

  c = conn.cursor()
  c.execute('select * from cases order by plaintiff limit 2')
 
  print "\n\n"
  print c.fetchall()
def sqldump():
  f = open('results.csv','w')
  conn = sqlite3.connect('/tmp/example')
  c = conn.cursor()
  c.execute("select * from cases where completed='TRUE'")
  for row in c:
    f.write('| '.join(row))