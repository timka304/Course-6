import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go



data = pd.read_csv(r"Machine Learning\WHO-COVID-19-global-data.csv")

print(data.info())


data["DateReported"] = pd.to_datetime(data["DateReported"])

print(data.info())

april = data["DateReported"].dt.month == "4"

print(len(april))


us = data["Country"] == "United States of America"

us_april = data[(data["Country"] == "United States of America") & (data["DateReported"].dt.month == 4) & (data["DateReported"].dt.year == 2021)] 

print(us_april)


deaths = data["New_deaths"]

year = data["DateReported"].dt.year == 2021


data2 = data[data["DateReported"].dt.date == pd.to_datetime("2021-04-01")]


# print(data2)

data3 = data.groupby("DateReported")["New_cases"].sum()

print(data3)

data4 = data.groupby("DateReported")["Cumulative_cases"].sum()

print(data4)

data5 = data.groupby("DateReported")["New_deaths"].sum()

print(data5)

data6 = data.groupby("DateReported")["Cumulative_deaths"].sum()

print(data6)

figure1 = go.Figure()

data7 = data.groupby("DateReported").sum()

figure1.add_trace(go.Scatter(x= data7.index, y= data7["Cumulative_deaths"], fill= "tonexty", line_color= "blue"))

figure1.update_layout(title= "COVID Cumulative Deaths")

figure1.write_html("coviddeaths.html", auto_open= True)



figure2 = go.Figure()
data8 = data.groupby("DateReported").sum()

figure2.add_trace(go.Scatter(x= data8.index, y= data8["Cumulative_cases"], fill= "tonexty", line_color= "red"))

figure2.update_layout(title= "COVID Cumulative Cases")

figure2.write_html("covidcases.html", auto_open= True)
