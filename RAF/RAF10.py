from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("seaborn")

data=pd.read_csv("data3.csv")
view_count=data["view_count"]
likes=data["likes"]
ratio=data["ratio"]

plt.scatter(view_count,likes,marker="o",edgecolor="k",linewidth=1.25,c=ratio,cmap="summer")

plt.xscale("log")
plt.yscale("log")

cbar=plt.colorbar()
cbar.set_label("likes percentage")

plt.title("Youtube Trending Video")
plt.xlabel("Views")
plt.ylabel("Likes")

plt.legend()
plt.tight_layout()
plt.show()