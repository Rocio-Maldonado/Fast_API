from cgitb import text
from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/myapi")
def hello(name: str = None):
    if name is None:
        text = "hello world"

    else:
        text = "hello " + name

    return text


@app.get("/get-iris")
def get_iris():
    url = 'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)
    return iris


@app.get("/plot-iris")
def plot_iris():
    import matplotlib.pyplot as plt

    url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
    iris = pd.read_csv(url)
