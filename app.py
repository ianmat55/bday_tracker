from flask import Flask, render_template, request, url_for, flash
import sqlite3
import os

def get_db_connect():
	con = sqlite3.connect('database.db')
	return con
		
key = os.urandom(21)
app = Flask(__name__)
SECRET_KEY = key
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def index():
	con = get_db_connect()
	c = con.cursor()

	if request.method=='POST':
		data_name = request.form["name"]
		data_bd = request.form["birthday"]

		try:
			c.execute('INSERT into birthdays (name, birthday) VALUES (?,?)',
				(data_name, data_bd,))
		except:
			flash("duplicate entry")

		#select data to display
		c.execute("""
		SELECT DISTINCT
		name, birthday
		, CASE 
			WHEN strftime('%m',date('now')) > strftime('%m',date(birthday)) THEN strftime('%Y',date('now')) - strftime('%Y',date(birthday))
			WHEN strftime('%m',date('now')) = strftime('%m',date(birthday)) THEN 
				CASE 
					WHEN strftime('%d',date('now')) >= strftime('%d',date(birthday)) THEN strftime('%Y',date('now')) - strftime('%Y',date(birthday))
					ELSE strftime('%Y',date('now')) - strftime('%Y',date(birthday)) - 1
				END
			WHEN strftime('%m',date('now')) < strftime('%m',date(birthday)) THEN strftime('%Y',date('now')) - strftime('%Y',date(birthday)) - 1

		END AS 'age'

		FROM birthdays
		ORDER BY birthday;
		""")

		test = c.fetchall()

		con.commit()
		con.close()

		return render_template('index.html', data_name=data_name, data_bd=data_bd, test=test)
	
	else:
		return render_template('index.html')