import os
from flask import Flask, redirect, url_for, render_template, request, flash
from forms import RecipeForm, SearchForm
import pandas as pd
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SECRET_KEY'] = "aon123xzdondfipubasdfgibf45234uasdfbipSBDFPIUBdsf"
app.config['SUBMITTED_DATA'] = os.path.join("static", "data_dir", "")
app.config['SUBMITTED_IMG'] = os.path.join("static", "image_dir", "")


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/add_recipe', methods=["POST", "GET"])
def add_recipe():
    """
    A function that uses a pre-built form that allows a user to add a recipe to the database, including file handling.
    :return:
    """
    df = pd.read_csv("static/data_dir/recipes.csv", dtype={"name": str})
    df = df.set_index("name")
    form = RecipeForm()
    if form.validate_on_submit():
        recipe_name = form.recipe_name.data
        if recipe_name not in df.index:
            recipe_ingredients = form.recipe_ingredients.data
            recipe_instructions = form.recipe_instructions.data
            recipe_serving_size = form.recipe_serving_size.data
            picture_filename = (recipe_name.lower().replace(" ", "_") + "." +
                                secure_filename(form.recipe_picture.data.filename).split(".")[-1])
            form.recipe_picture.data.save(os.path.join(app.config["SUBMITTED_IMG"] + picture_filename))
            df.loc[recipe_name] = [recipe_ingredients, recipe_instructions, recipe_serving_size, picture_filename]
            df.to_csv("static/data_dir/recipes.csv")
            flash("Your recipe was added to the cookbook!")
            return redirect(url_for("add_recipe"))
        else:
            flash("A recipe with that name already exists! \nTry something funnier.")
            return redirect(url_for("add_recipe"))
    else:
        return render_template("add_recipe.html", form=form)


@app.route("/search_recipe", methods=["POST", "GET"])
def search_recipe():
    search = SearchForm(request.form)
    if request.method == "POST":
        return display_recipe(search)

    return render_template("search_recipe.html", form=search)


@app.route("/display_recipe")
def display_recipe(search):
    df = pd.read_csv("static/data_dir/recipes.csv")
    recipe = df.iloc[0]
    return render_template("view_recipe.html", recipe=recipe)


if __name__ == "__main__":
    app.run()
