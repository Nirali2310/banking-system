from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DecimalField
from wtforms import validators, ValidationError
from wtforms.validators import DataRequired


class TransectionForm(FlaskForm):
   from_user = StringField("From_user ", validators=[DataRequired()])
   to_user = StringField('To_user', validators=[DataRequired()])
   amount_transfered = DecimalField("amount", validators=[DataRequired()])
   submit = SubmitField("Submit")