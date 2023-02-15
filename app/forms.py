from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class HouseForm(FlaskForm):
    owner = StringField('Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    neighborhood = StringField('Neighborhood', validators=[DataRequired()])
    area = StringField('Square Footage', validators=[DataRequired()])
    price = StringField('Price (optional)')
    for_sale = BooleanField('For Sale')
    submit = SubmitField('List House!')
