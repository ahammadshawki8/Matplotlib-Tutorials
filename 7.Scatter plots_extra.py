# module 7 extra
# Scatter plots
# plotting real world data

# we have a data3. csv file of top trending youtube videos.
# and we do a scatter plot of their total views and total likes.
# here we also have the ratio of likes and dislikes as well.

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("seaborn")

# lets pull in the data from the csv file
data=pd.read_csv("data3.csv")
view_count=data["view_count"]
likes=data["likes"]
ratio=data["ratio"]

# now we can plot this plot
plt.scatter(view_count,likes,c=ratio,cmap="summer",edgecolor="black",linewidth=1,alpha=0.75)
# but there is too many data messing up in a single place.
# so we can use log scales for both of our x and y scales by doing that-
plt.xscale("log")
plt.yscale("log")
# let use the ratio as color of dots in plot.
# and lets use the color bar so that we can know what it represents.
cbar=plt.colorbar()
cbar.set_label("Likes Percentage")

plt.title("Most Trending Youtube Videos")
plt.xlabel("view count")
plt.ylabel("total like")

plt.legend()
plt.tight_layout()
#plt.savefig("plot10.png")
plt.show()

# using a scatter plot for this is a great way to represent the co-relations of the values.
# and also using color and sizes can show the difference of the values when we are adding lots of values in our plot.
# they will help us to describe the plot more easier and to represent the data clearly.