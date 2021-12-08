import csv
import pandas as pd 
import plotly.express as px

read = pd.read_csv("data.csv")
graph = px.scatter(read,x="date",y="cases",color="country")
graph.show()