from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired

class addCountry(FlaskForm):
	cname = StringField("country name",validators=[DataRequired(message="Provide the valid country name")])
	code = StringField("code",validators=[DataRequired(message="Provide the code")])
	s_c_name = StringField("short code",validators=[DataRequired(message="Provide the short name")])
	status = SelectField('Status', choices=[(1, 'Active'), (0, 'Deactive')]) #(value,label)
	submit=SubmitField("ADD COUNTRY")


class Area(FlaskForm):
	aname = StringField("Area name", validators=[DataRequired(message="Provide the valid country name")])
	status = SelectField('Status', choices=[(1, 'Active'), (0, 'Deactive')])  # (value,label)
	submit = SubmitField("ADD AREA")


class Religion(FlaskForm):
	rname = StringField("Religion name", validators=[DataRequired(message="Provide the valid country name")])
	status = SelectField('Status', choices=[(1, 'Active'), (0, 'Deactive')])  # (value,label)
	submit = SubmitField("ADD RELIGION")


class BloodGroup(FlaskForm):
	bname = StringField("Blood Group", validators=[DataRequired(message="Provide the valid country name")])

	status = SelectField('Status', choices=[(1, 'Active'), (0, 'Deactive')])  # (value,label)
	submit = SubmitField("ADD BLOOD GROUP")


class Tongue(FlaskForm):
	tname = StringField("Mother language", validators=[DataRequired(message="Provide the valid country name")])

	status = SelectField('Status', choices=[(1, 'Active'), (0, 'Deactive')])  # (value,label)
	submit = SubmitField("ADD MOTHER TONGUE")
