from matplotlib import pyplot as plt

print(plt.style.available)
plt.style.use("fivethirtyeight")

ages_x =[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y  =[38496, 41000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
py_y= [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83670]
js_y=[37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x,dev_y,color="r",linewidth=.75,linestyle="--",marker=".",label="All devs")
plt.plot(ages_x,py_y,color="b",linewidth=.75,label="Python devs")
plt.plot(ages_x,js_y,color="orange",linewidth=.75,label="JavaScript devs")

plt.title("Median Salary By Age")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
