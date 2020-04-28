import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn")

data=pd.read_csv("data5.csv")
ages=data["Age"]
dev_salaries=data["All_Devs"]
py_salaries=data["Python"]
js_salaries=data["JavaScript"]

fig1,ax1 =plt.subplots()
fig2,ax2 =plt.subplots()

ax1.plot(ages,dev_salaries,label="All Developers",color="k",linestyle="--")
ax2.plot(ages,py_salaries,label="Python")
ax2.plot(ages,js_salaries,label="JavaScript")

ax1.set_title("Median Salary By Age")
ax1.set_xlabel("Age")
ax1.set_ylabel("Salary")
ax1.legend()

ax2.set_title("Median Salary By Age")
ax2.set_xlabel("Age")
ax2.set_ylabel("Salary")
ax2.legend()

plt.tight_layout()
plt.show()