import os
from flask import Flask, redirect, url_for, request, render_template
from forms import RecipeForm
import pandas as pd
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SECRET_KEY'] = "aon123xzdondfipubasdfgibf45234uasdfbipSBDFPIUBdsf"
app.config['SUBMITTED_DATA'] = os.path.join("static", "data_dir", "")
app.config['SUBMITTED_IMG'] = os.path.join("static", "image_dir", "")


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/add_recipe', methods=["Post", "Get"])
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe_name = form.recipe_name.data
        picture_filename = (recipe_name.lower().replace(" ", "_") + "." +
                            secure_filename(form.recipe_picture.data.filename).split(".")[-1])
        form.recipe_picture.data.save(os.path.join(app.config['SUBMITTED_IMG'] + picture_filename))
        df = pd.DataFrame([{'name': recipe_name, 'picture':picture_filename}])
        df.to_csv(os.path.join(app.config["SUBMITTED_DATA"] + recipe_name.lower().replace(" ", "_") + ".csv"))
        return redirect(url_for("hello_world"))
    else:
        return render_template("add_recipe.html", form=form)


@app.route("/search_recipe", methods=["Post", "Get"])
def search_recipe():
    return render_template("search_recipe.html")


if __name__ == "__main__":
    app.run()
