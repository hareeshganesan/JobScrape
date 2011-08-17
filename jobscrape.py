from flask import Flask
from flask import render_template
from flask import request
import sqlite3
app = Flask(__name__)

DATABASE = 'jobscrape'


def connect_db():
	return sqlite3.connect(DATABASE)

@app.route('/')
def jobscrape():
	calendar = month_count()
	return render_template('layout.html', data=json.dumps(calendar))
	
def month_count():
	conn = sqlite3.connect('jobscrapedata')
	c = conn.cursor()
	date_list = c.execute('select jobid, deadline from jobs').fetchall()
	grouping = {}
	return grouping
		
@app.route('/submit', methods=['POST'])
def submit():
	conn = connect_db()
	c = conn.cursor()
	c.execute("""select * from cases where caseid='"""+request.form['caseid']+"'")
	if(c.fetchone()[6]=='TRUE'):
	  return "Data submitted improperly. Please refresh your page."

	command = "update cases "+"set plaintiff='"+request.form['plaintiff']+"', ada='"+request.form["ada"]+"', type='"+request.form["type"]+"', completed='TRUE' where caseid='"+request.form['caseid']+"'"
	c.execute(command)
	conn.commit()
	c.close()


	return "Thanks for submitting"

if __name__=='__main__':
	app.debug=True	
	app.run(port=6542)