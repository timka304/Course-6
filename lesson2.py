import pandas as pd


r = {"name": ["tim", "john", "mark"], "age":["14", "15", "16"], "grade":["A", "B", "C"], "class": ["1", "2", "3"]}

print(r["name"][0])
print(r["age"][2])
print(r["grade"][0])
print(r["class"][0])

data = pd.DataFrame(r)

print(data)

print(data.columns)

print(data.shape)

print(data["name"])

print(data.head())
print(data.tail())


titanic_data = pd.read_csv(r"Data Science\titanic.csv")


print(titanic_data)

print(titanic_data.head())
print(titanic_data.tail())
print(titanic_data.shape)
print(titanic_data.columns)

print(titanic_data["Name"])

print(titanic_data[["Name", "Age"]])

#MIN(), MAX(), MEAN(), COUNT() FUNCITIONS

print(titanic_data["Age"].max())
print(titanic_data.info())

print(titanic_data.describe())

print(titanic_data["Pclass"].value_counts())

#FILTERING DATA

print(titanic_data[titanic_data["Age"] > 30])

print(titanic_data["Name"][titanic_data["Age"] > 30])

print(titanic_data[(titanic_data["Age"] > 19) & (titanic_data["Age"] < 31)])