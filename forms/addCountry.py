from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired

class addCountry(FlaskForm):
	cname = StringField("country name",validators=[DataRequired(message="Provide the valid country name")])
	code = StringField("code",validators=[DataRequired(message="Provide the code")])
	s_c_name = StringField("short code",validators=[DataRequired(message="Provide the short name")])
	status = SelectField('Status', choices=[(1, 'Active'), (0, 'Deactive')]) #(value,label)
	submit=SubmitField("ADD COUNTRY")