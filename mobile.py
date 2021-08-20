import plotly.figure_factory as pf
import pandas as pd
import csv
df=pd.read_csv("data.csv")
mobile=[]
mobile=df["Avg Rating"].tolist()
graph=pf.create_distplot([mobile],["reasult"],show_hist=False)
graph.show()