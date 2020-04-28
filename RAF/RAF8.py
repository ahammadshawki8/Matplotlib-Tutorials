from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("ggplot")

data=pd.read_csv("data2.csv")
ages=data["Age"]

plt.hist(ages,bins=[0,10,20,30,40,50,60,70,80,90],edgecolor="black",log=True)

median_age=29
plt.axvline(median_age,linewidth=2,color="green",label="Median Age")

plt.title("Respondants by Age")
plt.xlabel("Age")
plt.ylabel("Respondants")

plt.legend()
plt.tight_layout()
plt.show()