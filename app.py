from flask import Flask, render_template, flash
from wtforms import DateField, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import sqlite3
import os


#Establish db connection to sqlite
def get_db_connect():
	con = sqlite3.connect('database.db')
	return con

#Forms
class BirthdayForm(FlaskForm):
	birthdate = DateField('Date', validators=[DataRequired()])
	name = StringField('Full Name' , validators=[DataRequired()])
	submit = SubmitField('Submit')

#app init and secret key
key = os.urandom(21)
app = Flask(__name__)
SECRET = key
app.config['SECRET_KEY'] = SECRET


# Routes
@app.route('/', methods=['GET', 'POST'])
def index():

	con = get_db_connect()
	c = con.cursor()

	form = BirthdayForm()

	if form.validate_on_submit():
		try:
			c.execute('INSERT into birthdays (name, birthday) VALUES (?,?)',
			(form.name.data, form.birthdate.data,))
			c.commit()
			c.close()

		except Exception as e:
			print(e)

	
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


	return render_template('index.html', form=form, test=test)