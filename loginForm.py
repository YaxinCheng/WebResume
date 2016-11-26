from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required
from random import randint

class loginForm(FlaskForm):
	question = None
	dumbQuestion = StringField("DumbQuestion", validators = [Required()])
	submit = SubmitField('Confirm')
