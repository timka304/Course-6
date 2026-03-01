import pandas as pd
import random
import numpy as np



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

# print(titanic_data["Age"].max())
# print(titanic_data.info())

# print(titanic_data.describe())

# print(titanic_data["Pclass"].value_counts())

# #FILTERING DATA

# print(titanic_data[titanic_data["Age"] > 30])

# print(titanic_data["Name"][titanic_data["Age"] > 30])

# print(titanic_data[(titanic_data["Age"] > 19) & (titanic_data["Age"] < 31)])

print(titanic_data[(titanic_data["Pclass"] == 1) | (titanic_data["Pclass"] == 2)])


print(titanic_data.loc[titanic_data["Survived"] == 1, ["Name", "Age"]])

print(titanic_data.iloc[100:150, 2:5:2])

titanic_data.iloc[0:10, 2] = "Tim"

print(titanic_data[0:10])


titanic_data.to_csv("new_titanic.csv")


titanic_data["Discount"] = titanic_data["Fare"]*0.1

print(titanic_data)

hair_colours = ["Black","Blonde", "Brunette"]

random_hair = random.choice(hair_colours)

titanic_data["Hair Colour"] = np.random.choice(hair_colours, len(titanic_data))


print(titanic_data)



td = titanic_data.rename(columns={"Name":"First Name"})



print(td)


#AGGREGATE FUNCTIONS

#MEDIAN() SUM()


print(titanic_data[["Age", "Fare"]].mean())


#GROUPING DATA CATEGORICALLY

td1 = titanic_data.groupby("Pclass")["Fare"].mean()

print(td1)


td2 = titanic_data.groupby(["Pclass", "Sex"])["Fare"].mean()

print(td2)


#SORTING DATA

td_sort = titanic_data.sort_values(by="Pclass", ascending=True)

print(td_sort)


titanic_data["Pname"] = titanic_data["Name"].str.lower()

titanic_data["name length"] = titanic_data["Pname"].str.len()

print(titanic_data)