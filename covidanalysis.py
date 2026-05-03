import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go




data = pd.read_csv(r"Machine Learning\covid_data.csv")

print(data)

newdata = data.info()

print(newdata)


datac = data[["Province_State", "Country_Region", "Confirmed", "Recovered", "Active"]]
print(datac)

newdata2 = data.groupby("Country_Region")["Confirmed"].sum()

print(newdata2)

newdata3 = data.groupby("Country_Region")["Deaths"].sum()
print(newdata3)


print("Top 10 Deaths from COVID")
print(newdata3.nlargest(10).sort_values(ascending=True))
topten = newdata3.nlargest(10).sort_values(ascending=True)



chart1 = px.bar(topten, y= "Deaths", x= topten.index, color= "Deaths", color_continuous_scale=["red", "blue"], title= "COVID Deaths by Country")

chart1.write_html("chart1.html", auto_open= True)


newdata4 = data.groupby("Country_Region")["Recovered"].sum()
print(newdata4)


print("Top 10 counrties with the most recovered cases")
top10_2 = newdata4.nlargest(10).sort_values(ascending=True)

print(top10_2)

scatter1 = px.scatter(top10_2, y="Recovered", x= top10_2.index, title="Countries with the most recovered COVID cases", size= "Recovered", size_max=50, color=top10_2.index)
scatter1.write_html("scatter1.html", auto_open=True)


newdata5 = data.groupby("Country_Region")["Confirmed"].sum()
top10 = newdata5.nlargest(10).sort_values(ascending=True)

print(top10)

scatter2 = px.scatter(top10, y="Confirmed", x= top10.index, title="Countries with the most confirmed COVID cases", size= "Confirmed", size_max=50, color=top10.index)
scatter2.write_html("scatter2.html", auto_open= True)



#Countrywise Analysis

data2 = data.groupby("Country_Region").get_group("US")
print(data2)


top_ten = data2.nlargest(10,"Deaths").sort_values(by= "Deaths", ascending=True)
print(top_ten)

scatter3 = px.scatter(top_ten, y= "Deaths", x= "Province_State", title= "States with the most confirmed COVID Deaths", size= "Deaths", size_max= 50)
scatter3.write_html("scatter3.html", auto_open=True)



#Graph Plotting

figure1 = go.Figure(data= [
    go.Bar(name= "Death Cases", x= top_ten["Deaths"], y= top_ten["Province_State"], orientation= "h"), 
    go.Bar(name= "Confirmed Cases", x= top_ten["Confirmed"], y= top_ten["Province_State"], orientation="h")
])

figure1.write_html("figure1.html", auto_open=True)



figure2 = go.Figure(data= [
    go.Bar(name= "Death Cases", x= top_ten["Province_State"], y= top_ten["Deaths"]), 
    go.Bar(name= "Confirmed Cases", x= top_ten["Province_State"], y= top_ten["Confirmed"])
])

figure2.write_html("figure2.html", auto_open=True)


#ANOThER COUNTRY

data3 = data.groupby("Country_Region").get_group("United Kingdom")
print(data3)


top_ten = data3.nlargest(10,"Deaths").sort_values(by= "Deaths", ascending=True)
print(top_ten)

scatter4 = px.scatter(top_ten, y= "Deaths", x= "Province_State", title= "Cities with the most confirmed COVID Deaths", size= "Deaths", size_max= 50)
scatter4.write_html("scatter4.html", auto_open=True)
