# module 10 extra
# subplots

# here we have created two different figures.
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("data5.csv")
ages=data["Age"]
dev_salaries=data["All_Devs"]
py_salaries=data["Python"]
js_salaries=data["JavaScript"]

# clear all the arguements
fig1, ax1=plt.subplots()
fig2, ax2=plt.subplots()
# making 2 axes in 2 figure

ax1.plot(ages,dev_salaries,label="All_Devs",linestyle="--")
ax2.plot(ages,py_salaries,label="Python")
ax2.plot(ages,js_salaries,label="JavaScript")

ax1.legend()
ax2.legend()

ax1.set_title("Median Salary by Age")
ax1.set_xlabel("Ages")
ax1.set_ylabel("Median Salary")

ax2.set_title("Median Salary by Age")
ax2.set_xlabel("Ages")
ax2.set_ylabel("Median Salary")

plt.tight_layout()
# to save this figures we are going to use fig object instead of plt object.
fig1.savefig("fig1.png")
fig2.savefig("fig2.png")
plt.show()

# its nice being able to generate multiple figures and axes at a time like this and save them.
# so this would be great for automatic data analysis where we are plotting data in a background script.
