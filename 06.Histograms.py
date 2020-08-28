# module 6
# histograms
# histograms are great for visualizing the data falls within certain boundary.
# its a lot like a bar graph.
# but a histogram groups the data up into certain range instead of plotting each individual value.

# lets pretend we took a survey and we track the ages with all the people who responded.
# now it might be useful to plot those ages to get an idea of which age groups are in our sample size.
# how can we do this?
# we can think that we could use bar chart. but that would be a bad idea as we possible have up to hundred different ages.
# and if we plot that out we may have hundred of different coloumns which definately isn't useful.
# on the other side histograms allows as to create a bins for our data and plot how many values fall into that bins.
# we can create a histogram with hist() method. 

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("seaborn")
 
data= pd.read_csv("data2.csv")
ages=data["Age"]
#ids=data["Responder_id"]

#plt.hist(ages)
# if we ran this now it would give us a plot. but really we dont know what plot it would be using.
# so we should pass those bins manually and explicitly so that people know what those bins are.
# so when we specified bins we can either pass an integer or a list of values.
# if we passed in an integer then it will just make that number of bins and divide our data automatically.
# but when we pass a list of values those values would be bins.
# if we want to plot our values into 10 year differnces.we could-
bins=[0,10,20,30,40,50,60,70,80,90]
# we should use our own list bins for this kind of data because
# if we do that we does't have to where the colomns has broken up and its easier to read too.
# we can even exclude some data if we dont want to add those ranges to our bins.
# for example, if we dont want to include 10 to 20 in our plot we can just start the bins list with 20.
plt.hist(ages,bins=bins,edgecolor="black"),#log=True)
# when we feel difficult to read the columns in our plot we can use edgecolor arguement.
# again sometimes when we are working with large data we can have some values which are so so small than other values
# so that we cant see in our plot. so to solve this problem, we can plot the histogram in a logarithmic scale.
# to do this we can add a arguement log equals to True.
# now we have the data visible.
# sometimes we need to add some additional information to our code to make it more useful.
# lets say we want to plot a vertical line where the median age of all the respondants is.
# to do that we should use axvline() method which stands for axis vertical line.
median_age=29
plt.axvline(median_age,color="green",label="Median age",linewidth=2)
# we can add here color and label also.
# we can also change the line width by adding linewidth arguement.

plt.legend()
plt.title("Ages of respondants")
plt.xlabel("Ages")
plt.ylabel("Total respondants")
plt.tight_layout()
#plt.savefig("plot8.png")
plt.show()