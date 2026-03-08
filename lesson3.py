import matplotlib.pyplot as plt
import numpy as np


#DIFFERENT TYPES OF GRAPHS

#BAR CHARTS, PIE CHART, LINEAR, STACK PLOT, SCATTER 

# shop_name = ["KFC", "Mcdonalds", "Burger King", "Subway"]
# rating = ["1", "2", "3", "4"]


# plt.plot(shop_name, rating, marker= "x", linewidth= 2, color= "red")
# plt.title("Comparison")
# plt.xlabel("Restaurant Name")
# plt.ylabel("Rating")



# plt.show()


#BAR GRAPH


shop_name = ["KFC", "Mcdonalds", "Burger King", "Subway"]
rating = [1, 2, 3, 4]

plt.bar(shop_name, rating)
plt.ylim(0, 5)
plt.show()


#PIE CHART

daily_activities = ["walking", "working", "sleeping", "eating", "resting"]
time = [15, 20, 40, 12, 30]

plt.pie(time, labels= daily_activities, shadow= True, autopct= "%1.1f%%")
plt.show()

int1 = np.random.randint(1, 50, 50)

bins = [10, 20, 30, 40, 50]

plt.hist(int1, bins)
plt.show()



#HISTOGRAM

random_numbers = np.random.randint(1, 50, 100)

intervals = [0, 10, 20, 30, 40, 50]

plt.hist(random_numbers, bins= intervals)
plt.show()


#SCATTER PLOT

number_sold = np.random.randint(1, 20, 6)
temperature = [0, 1, 2, 3, 4, 5]


plt.scatter(number_sold, temperature)

plt.show()


#STACK

activities = ["football", "running", "basketball", "cricket"]
monday_hours = [2, 1, 2, 3]
tuesday_hours = [3, 2, 4, 3]
wednesday_hours = [1, 1, 2, 1]
thursday_hours = [4, 3, 1, 2]

plt.stackplot(activities, monday_hours, tuesday_hours, wednesday_hours, thursday_hours, labels= ["Monday", "Tuesday", "Wednesday", "Thursday"])

plt.legend()

plt.xlabel("Activities")
plt.ylabel("Hours Spent")


plt.show()


#SUB PLOT

plt.figure()

plt.subplot(121)

plt.stackplot(activities, monday_hours, tuesday_hours, wednesday_hours, thursday_hours, labels= ["Monday", "Tuesday", "Wednesday", "Thursday"])


plt.subplot(122)

plt.scatter(number_sold, temperature)
plt.show()