import imp
import math
import numpy as np
import os
from keras.models import load_model
from . import model

# print(os.getcwd())

# model = load_model('./fruits_classifier.h5')

def hex_to_hue(hex):
    r = int(hex[1:3], 16)
    g = int(hex[3:5], 16)
    b = int(hex[5:7], 16)
    high = max(r, g, b)
    low = min(r, g, b)
    h, s, v = high, high, high

    d = high - low
    s = 0 if high == 0 else d/high

    if high == low:
        h = 0.0
    else:
        h = {
            r: (g - b) / d + (6 if g < b else 0),
            g: (b - r) / d + 2,
            b: (r - g) / d + 4,
        }[high]
        h /= 6

    return h * 360


def make_prediction(weight, peel_color, flesh_color, texture, size):
    pred_arr = model.predict([[weight, peel_color, flesh_color, texture, size]])
    prediction_array = map(lambda x: str(round(x * 100, 2)), pred_arr[0])

    prediction = np.argmax(pred_arr, axis = 1)
    fruits = {0:"apple", 1:"mango", 2:"orange", 3:"pineapple", 4:"unknown"} 
    prediction_array = list(prediction_array)
    print(prediction_array)
    return prediction_array, fruits.get(prediction[0])
