import csv
import pandas as pd
import scipy as sc
import plotly.figure_factory as ff

df = pd.read_csv("./Project/data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Average Rating"], show_hist = False)
fig.show()