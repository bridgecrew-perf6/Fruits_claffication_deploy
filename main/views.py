from flask import Blueprint, render_template, request
from .helpers import hex_to_hue, make_prediction

views = Blueprint('views', __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        weight = int(request.form.get("weight"))
        peel_color_hex = request.form.get("peel color")
        flesh_color_hex = request.form.get("flesh color")
        texture = int(request.form.get("texture"))
        size = int(request.form.get("size"))

        peel_color = hex_to_hue(peel_color_hex)
        flesh_color = hex_to_hue(flesh_color_hex)

        prediction_array, prediction = make_prediction(weight, peel_color, flesh_color, texture, size)
        print(prediction)
        prediction_image = prediction + ".png"
        print(prediction_array)
        return render_template("home.html", data={'prediction':prediction, 'prediction_array':prediction_array, 'prediction_image':prediction_image})

    return render_template("home.html", data={})