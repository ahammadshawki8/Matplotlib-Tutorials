from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("ggplot")

data=pd.read_csv("data1.csv")
ages=data["Age"]
dev_salaries=data["All_Devs"]
py_salaries=data["Python"]

overall_median=57287

plt.plot(ages,dev_salaries,linestyle="--",color="k",label="All_devs")
plt.plot(ages,py_salaries,color="b",label="Python Devs")

plt.fill_between(ages,py_salaries,y2=dev_salaries,alpha=0.25,where=(py_salaries>=dev_salaries),interpolate=True,label="Above Avg")
plt.fill_between(ages,py_salaries,y2=dev_salaries,alpha=0.25,where=(py_salaries<dev_salaries),color="red",interpolate=True,label="Above Avg")

plt.title("Median Salary By Age")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.legend()
plt.tight_layout()
plt.show()