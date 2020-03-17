# module 7
# scatter plots

# scatter plots are great when we want to show the relationship between two sets of values
# and see if they are co-related.
# they are really nice for seeing different trends and outliers or things like that

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("seaborn")

x=[5,7,8,5,6,7,9,2,3,4,4,4,2,6,3,6,8,6,4,1]
y=[7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]
colors=[7,5,9,7,5,7,2,5,3,7,1,2,8,1,9,2,5,6,7,5]
sizes=[209,486,381,266,191,315,185,228,174,558,239,394,399,153,273,293,436,501,397,539]

# to create a scatter plot we need to use scatter() method.
#plt.scatter(x,y,s=300,c="green",marker="*",edgecolor="black",linewidth=1,alpha=0.75)

# we can change the sizes of the dots by adding "s" arguement.
# we can also change the color of the dots by adding "c" arguement.
# we can also change the marker style of the dots by adding "marker" arguement.
# we can also add the edges of the dots by adding "edgecolor" arguement.
# we can also change the linewidth of the edges by adding "linewidth" arguement.
# we can also set the transpirency of the dots by adding "alpha" arguement.

# the color and sizes can actually be on a per mark basis rather them applying them to all of the marks.
# why should we want multiple colors and sizes?
# =because having the ability of adding multiple color and sizes allows us to add additional datasets in our plot.
# for example,
# lets say we have current plot that we just looked at but we want to add some additional information.
# lets pretend our current plot is some kind of survey data about a bunch of people.
# and we wanted to break down the data further into something more specific.
# lets say we have these people rate any product from 1 to 10 and we wanted to plot their rating.
# to do that we could simply assign some numbers to these different possibilities
# and those will then give us different colors on our scatter plots as long as we pass that into a method.
# here we have color variable which is actually a list which indicates the rating of the people from 1 to 10.
# so each of the value in the list will correspond to a data point in our x and y variables.
# we can pass these into out scatter method as the "c" arguement.
plt.scatter(x,y,s=sizes,c=colors,cmap="Greens",marker="*",edgecolor="black",linewidth=1,alpha=0.75)
# we can see that we got different color dots so what this is.
# so what these is doing here is whenever we plot this x and y values it also access the color values.
# but these colors are not too good. these areb the shades of grey.
# we can actually change this by using a color map.
# there are ton of buit_in color maps that we can use:
"https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html"
# to add the color maps in our plot we can just add a new arguement which is "cmap"
# but people will dont know what this colors are doing here.
# so we can add labels so that people could know what this colors represent.
# so yo do that we can add a color bar legend.
cbar=plt.colorbar() # that is a method
cbar.set_label("Ratings")
# we can also change the sizes of our each individual data points.
# these can add in another way explaining our data like populations or things like that.
# here we also have a sizes variable which is a list.
# so each of the value in the sizes list will correspond to a data point in our x and y variables.
# we can pass these into out scatter method as the "s" arguement.


plt.title("Sample data")
#plt.xlabel("view count")
#plt.ylabel("total like")

plt.legend()
plt.tight_layout()
#plt.savefig("plot9.png")
plt.show()
