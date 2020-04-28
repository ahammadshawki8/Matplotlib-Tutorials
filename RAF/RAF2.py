from matplotlib import pyplot as plt
import numpy as np

plt.style.use("ggplot")

ages_x =[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y  =[38496, 41000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
py_y= [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83670]
js_y=[37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

x_indexes=np.arange(len(ages_x))# it is like a list of 0 to 10 =. but it is not an ordinary list. it is a numpy array.
print(x_indexes)

width=0.25

plt.bar(x_indexes-width,dev_y,color="r",width=width,label="All dev")
plt.bar(x_indexes,py_y,color="b",width=width,label="Python dev")
plt.bar(x_indexes+width,js_y,color="orange",width=width,label="JavaScript dev")

plt.xticks(ticks=x_indexes,labels=ages_x)

plt.title("Median Salary By Age")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.legend()
plt.tight_layout()
plt.show()