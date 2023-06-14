from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    email = StringField('e-mail', validators=[DataRequired(), Email()])
    subject = StringField("Subject", validators=[DataRequired(), Length(min=1, max=100)])
    message = TextAreaField("Message", validators=[DataRequired()])


    submit = SubmitField('Send')