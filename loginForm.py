from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

class loginForm(FlaskForm):
	userName = StringField('UserName', validators = [Required()])
	password = PasswordField('Password', validators = [Required()])
	submit = SubmitField('Confirm')

