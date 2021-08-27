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
	with open('fetch.sql') as f:
		c.execute(f.read())
		test = c.fetchall()
	
	con.commit()
	con.close()

	return render_template('index.html', form=form, test=test)