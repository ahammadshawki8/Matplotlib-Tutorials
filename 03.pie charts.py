# lesson 3 
# pie charts

# pie charts are pretty simple and straight forward.

from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")

slices=[60,40]

#plt.pie(slices,labels=labels)# we need to use pie method to plot a pie chart.

# lets also add labels to our slices so that we can know whats what when we look at our chart.
# to do this we can add labels as a arguement in a list.
labels=["Male","Female"]
#plt.pie(slices,labels=labels)

# we can also use some separators in our pie chart. so to do this we can pass in some wedge properties.
# we can do that by adding an extra arguement which is called wedgeprops.
#plt.pie(slices,labels=labels,wedgeprops={"edgecolor":"white"})# it is a dictionary. here we are going to change the edgecolor.

# what if we want to change the color of the slices in the pie charts?
# we can do it by adding another arguement which is color. It is a list.
colors=["green","red"]
plt.pie(slices,labels=labels,wedgeprops={"edgecolor":"white"},colors=colors)
# here we can also use hex color values without color name because the default colors are too bright.
# some hex color values are-
# Blue  -   #008fd5
# Red   -   #fc4f30
# Yellow-   #e5ae37
# Green -   #6d904f
# we can find more hex color pelettes online.

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.savefig("plot4.png")
plt.show()

# now we have known how to make pie charts. Lets create a pie chart about popular programming languages.
# we are going to do that in our extra_practice module.
