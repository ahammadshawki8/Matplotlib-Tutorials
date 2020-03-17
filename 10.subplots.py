# module 10
# subplots

# so far in this series, we created our all the plots with pyplot object from matplotlib.
# and that works great.
# but if we want additional plots or if we want to work with plots in more object oriented manner,
# then it is best to create our plot with subplot() method.
# lot of people prefer to create their plots this way even if they are creating a single plot.

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("data5.csv")
ages=data["Age"]
dev_salaries=data["All_Devs"]
py_salaries=data["Python"]
js_salaries=data["JavaScript"]

fig, (ax1,ax2)=plt.subplots(nrows=2,ncols=1,sharex=True)# unpacking axes
# now our ax here which we can just think of as plot is only set to a single axes or a single plot at the moment.
# that is because by defaults subplots create a figure and then specify a certain number of rows and columns of axes.
# if we dont pass in our number of rows and columns then it just defaults to a one row by one column which is simply one axes.
# lets update our code to plot on this axis that we juxt created instead of using our pyplot object.

# for some cases it is as simple as using our ax here instead of plt object.
ax1.plot(ages,dev_salaries,label="All_Devs",linestyle="--")
ax2.plot(ages,py_salaries,label="Python")
ax2.plot(ages,js_salaries,label="JavaScript")
# we need to change the legend() also.
ax1.legend()
ax2.legend()

# here we not only change our plt object but also change the methods. for example set_title() instead of title(),
ax1.set_title("Median Salary by Age")
ax1.set_ylabel("Median Salary")

ax2.set_xlabel("Ages")
ax2.set_ylabel("Median Salary")
# tight_layout() and show() are methods of plt object. so this will remain same.
plt.tight_layout()
plt.savefig("fig.png")
plt.show()

# every time we are doing something with our plot we are using the plt(pyplot) object from the matplotlib library.
# we never actually created that object ourselves.
# that might be weird for some people who used to do coding in a object oriented manner.
# they might think in some point we should have do something like this.
#plt=Plot()  # create a new instance of a plot.
# we cant do something like that.
# the way that we are doing that now is called "stateful".
# and this called stateful because we are importing pyplot object and it has a current state 
# in terms of what figure we currently working with and what axes we currrently working with and things like that.
# but we havent talked about figure and axes in this series because we were using a single figure and a single axes object.
# so what are the figure and axes?
#=> the figure is the container holding our plot so we can think of that as the whole window that shows as when we run our code.
#=> the axes are the actual plots. So a figure can have multiple plots.
# in this series we have seen how to work with one plot on one figure. but we can have more than one.
# we can use gca() and gcf() method to get the current axes and figure.
print(plt.gcf())
print(plt.gca())
# we can also switch between different ones and that the stateful way of doing it.
# but many people prefer to use the more object oriented approach when working with multiple figures and axes.
# so to do that we can use the subplot() method. 

# right now lets create the same plot that we have.
# but instead of using pyplot object that we imported, we will instantiate a figure and an axes.
# to do that
"Please Look up"

# we can see that we are getting the same plot.
# so why we are learning this?
# how this is useful?
# lets say instead of all this data into a plot, we want to brake them into multiple plot.
# we wanted python and js plot in one plot and the other one in the other.
# to do that we can just add more axes.
# the first arguement of the subplot method is the number of rows and the number of columns. by default this is 1 by 1.
# we can change it and it will also change how this axis will return.

# if we print ax now- 
#print(ax)
# it will return AxesSubplot(0.113472,0.102323;0.867778x0.833434)
# we can see that the ax variable is equal to single AxesSubplot.
# but now lets say that we want 2 rows and 1 column.
# to do that we can simply add extra arguements in our subplots() method which are nrows and ncols 
# now if i run this-
#print(ax)
# it will return [<matplotlib.axes._subplots.AxesSubplot object at 0x0000027BD7432080>
#                 <matplotlib.axes._subplots.AxesSubplot object at 0x0000027BD745E9E8>]
# now we can see that our ax variable is a list of axesSubplots
# lets also see what happens if i do 2 row and 2 columns.
#print(ax)
# it wil return [[<matplotlib.axes._subplots.AxesSubplot object at 0x000001EC0C056E48>
#                 <matplotlib.axes._subplots.AxesSubplot object at 0x000001EC0C3A1828>]
#                [<matplotlib.axes._subplots.AxesSubplot object at 0x000001EC0C3DC208>
#                 <matplotlib.axes._subplots.AxesSubplot object at 0x000001EC0C408BA8>]]
# now this gets little more complicated.
# we can see we have an outer list here. and within the outer list there are two more list of AxesSubplots.
# so a total of 4 axesSubplots.
# this is pretty tricky. but we need to know how that will returned if we want to unpack them in a certain way.
# now for simplicity lets go to 2 rows and 1 columns.
# this gives us 2 axes which is what we wanted in order to break our data up.
# now this two plots will still be same figure which is the overall window
# if we wanted to them be different figures, we can do that too.
# instead of working with those 2 axes in a ax variable, let us unpack this.
"Please Look up"
# lets print them out.
print(ax1)
print(ax2)
# now we are getting those AxesSubplots individually.
# now lets change all the code of the methods.
# now if we run this we can see that we have one figure with 2 different plots.
# but there are some unnecessary information in our plot which are written twice times.
# so lets remove these.
# if we want to remove these X tick marks on the bottom plot, we can do that by passing an arguement in the subplots() method called "sharex".
# sharex will only label the bottom ticks for two rows.
# there also a sharey arguement. It will only label the leftmost ticks for two columns

# okay we have a nice figure here with two different plots.
# what if we want to this plot on two different figures.
# to do this we need to create another figure and another axis in the same method that we did before.
# lets do that in another module.

