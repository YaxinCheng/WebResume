from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

class loginForm(FlaskForm):
	dumbQuestion = StringField("DumbQuestion", validators = [Required()])
	submit = SubmitField('Confirm')

