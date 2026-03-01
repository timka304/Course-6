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
