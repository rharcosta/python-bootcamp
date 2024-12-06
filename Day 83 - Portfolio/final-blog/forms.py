from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    title = StringField("Project Title", validators=[DataRequired()])
    body = TextAreaField("Project Content", validators=[DataRequired()])
    img = StringField("Project Image", validators=[DataRequired()])
    submit = SubmitField("Submit Project")
