import pickle
from pathlib import Path

from sys import path as syspath
from os import path as ospath
syspath.append(ospath.join(ospath.dirname(ospath.realpath(__file__)))) # To find out where to look, import the utils path into the script path
from preprocessing import pipe


__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/yga_survey_classification.pkl", "rb") as f:
    model = pickle.load(f)


def predict_pipeline(text):
    text = pipe(text)
    return model(text)