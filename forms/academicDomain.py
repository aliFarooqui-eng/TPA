from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired



class Category(FlaskForm):
	catName = StringField("Category name", validators=[DataRequired(message="Provide the valid category name")])
	status = SelectField('Status', choices=[(1, 'Active'), (0, 'Deactive')])  # (value,label)
	submit = SubmitField("ADD CATEGORY")
