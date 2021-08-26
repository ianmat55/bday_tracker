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

class UpdateForm(FlaskForm):
	name_update = StringField('Full Name', validators=[DataRequired()])
	birthdate_update = DateField('Date', validators=[DataRequired()])
	submit_update = SubmitField('Submit')

class DeleteForm(FlaskForm):
	name_delete = StringField('Full Name', validators=[DataRequired()])
	submit_delete = SubmitField('Submit')

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

	form1 = BirthdayForm()
	form2 = UpdateForm()
	form3 = DeleteForm()

	if form1.validate_on_submit():
		c.execute('INSERT into birthdays (name, birthday) VALUES (?,?)',
			(form1.name.data, form1.birthdate.data,))

		form1.name.data = ""
		form1.birthdate.data = ""

		

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

	#update form
	if form2.validate_on_submit():
		pass
		
	#delete form
	if form3.validate_on_submit():
		c.execute('DELETE (name, birday) FROM birthdays WHERE name = VALUES (?)',
			(form3.name_delete.data))

		con.commit()
		con.close()


	return render_template('index.html', form1=form1, form2=form2, form3=form3, test=test)