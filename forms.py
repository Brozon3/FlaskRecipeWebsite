from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms.fields import StringField, TextAreaField
from wtforms.fields.html5 import DateField, EmailField, TelField
from wtforms.validators import DataRequired, Length


class RecipeForm(FlaskForm):
    recipe_name = StringField("Recipe Name:", validators=[DataRequired()])
    recipe_picture = FileField("Recipe Field: ", validators=[FileRequired()])