# module 9
# plotting live data in real time

# in this module we are going to plot some data that is continuosly generated in real time.
# so this real time plots would be great for plotting data that is changing frequently that we want to monitor.
# here we are actually monitering a csv file.
# if we are pulling some data from a real time api or a sensor of some kind
# then it is preety common to write those data in a csv file.
# so we monitor that for changes and make updates to our plots when there are new data available.

import random
from itertools import count
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")

x_vals=[]
y_vals=[]
 
index=count() # count function basically counts up one number at a time and each time we get the next value.

def animate(i):
    x_vals.append(next(index))# x values is going to append a value which going to count up by one. so its just going to be sequential.
    y_vals.append(random.randint(0,5))# y value is appending a random number here from 0 to 5.
    plt.cla()
    plt.plot(x_vals,y_vals,linewidth=0.5)
# lets say we want to run this function every second and plot this values appended to our list.
# how can we do that?
# we can use FuncAnimation class from the animation module in matplotlib.
# now lets tell matplotlib that we wnat to run that function on a specific interval so we can plot this new data.
# we can do this by-
ani=FuncAnimation(plt.gcf(),animate,interval=1000)
# first we need to add figure as the first arguement.
# then we need to add the function that we want for our animation.
# then we want to add that interval of how many secons after we run our function.
# the unit of the interval is on miliseconds.
# now matplotlib will run this function after 1 sec.
# but we need to plot the data in animate function.
# but here we are getting different colors each time.
# our plot method is actually plotting a brand new line every time but its not clearing out the old lines .
# so there are actually multiple lines getting stacked on top of each other there.
# but they are just being covered up so we can just really tell.
# so one way will can solve this is simply clear out our axis.
# if we do that every time it will plot new line from scratch and it will always have the same color.
# so to declare the axis we can simply run the cla() method which stands for clear axis. 
# so we need to add the color arguement in our plot() function.

plt.tight_layout()
plt.show()
