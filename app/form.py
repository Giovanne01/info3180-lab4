from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms.validators import DataRequired
from wsgiref import validate
from flask_wtf import FlaskForm


class UploadForm(FlaskForm):
    photo=FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'])])
