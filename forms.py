from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms import SubmitField
from wtforms.fields import StringField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired


class RecipeForm(FlaskForm):
    recipe_name = StringField("Recipe Name:", validators=[DataRequired()])
    recipe_ingredients = TextAreaField("Recipe Ingredient List:", validators=[DataRequired()])
    recipe_instructions = TextAreaField("Recipe Instructions:", validators=[DataRequired()])
    recipe_serving_size = SelectField("Serving Size:", choices=[(1, "1-2"), (2, "3-4"), (3, "4-6"), (4, "6-8"), (5, "8+")], validators=[DataRequired()])
    recipe_picture = FileField("Recipe Picture:", validators=[FileRequired()])
    submit = SubmitField("Submit")


class SearchForm(FlaskForm):
    search = StringField("Search", validators=[DataRequired()])
    submit = SubmitField("Submit")
