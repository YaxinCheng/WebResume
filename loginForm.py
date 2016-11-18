from wtforms import Form, StringField, PasswordField, validators

class loginForm(Form):
	username = StringField('UserName', [validators.Length(min = 4, max = 25)])
	password = PasswordField('Password', [validators.DataRequired()])
	
