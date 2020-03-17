# module 9
# extra

# using random data directly within our animate function doesn't really give us an idea of
# how this would help us plotting real world data that coming out from an outside source.

# to do this we are going to plot data that from a csv.
# and this csv is going to be constantly updated by a outside source.
# this source could be data that we pulled down from a online api and put into a csv file.
# it could be data that we are saving from a sensor and anything like that.
# so the source of our csv data is a simple python script that going to be continuosly adding values.
# there we just open a csv file and continuously adding new random values in it.

import random
from itertools import count
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")

def animate(i):
    data=pd.read_csv("data6.csv")
    x=data["x_value"]
    y1=data["total_1"]
    y2=data["total_2"]

    plt.cla()

    plt.plot(x,y1,label="Channel 1")
    plt.plot(x,y2,label="Channel 2")

    plt.legend(loc="upper left")
    # we have to add the legend() function in this animate function.
    # and have to choose a location else it will change the location every time when the animate function will run.
    plt.tight_layout()
    # we also need to put tight_layout method here so that the animate function consider that every time when it runs.

# now since this will run the animate function every second it will read that csv file every second.
# we can simply plot that out.
# lets give thats plot a label so we could know which one is which through the legend.

ani=FuncAnimation(plt.gcf(),animate,interval=1000)

# thats all we need to run that file but the csv file is not created it.
# so we will open our command pompt and run that python script to create our csv file.

plt.tight_layout()
plt.show()

# there's a lot more things that we can do depending on our needs.
# for example, if we need to run an initial function for our animation 
# that sets things up one time before our animation first runs.
# and to do that the FuncAnimation class has a an init func arguement that we can pass in to do that.
# or if we needed to pass in additional arguements to our animate function, 
# then our FuncAnimation class also have an F args arguement to do that.
# some of this animation can get pretty complex.
# people can use it for drawing, math simulation, gravity simulation and all kinds of neat stuff.

