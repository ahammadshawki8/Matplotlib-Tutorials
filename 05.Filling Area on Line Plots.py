# module 5
# Filling area on line plots

# this time we will revisit line plots.
# but this time we will add to them by adding an fill.
# fills are great because they not only make our plots nice progessionals but also they can give us useful insights depending on how we use them.
# for example, we can use conditional fills that will show us what areas of our line plots fall above or below a certain trash hole.

import pandas as pd
from matplotlib import pyplot as plt

# here we have bringing up some data from csv file. 
data=pd.read_csv("data1.csv") 
ages=data["Age"]
dev_salaries=data["All_Devs"]
py_salaries=data["Python"]
js_salaries=data["JavaScript"]  

overall_median=57287

# plotting our data
plt.plot(ages,dev_salaries,color="#444444",linestyle="--",label="All Devs")
plt.plot(ages,py_salaries,label="Python Devs")

# lets say we want to fill the entire area underneath the python plotted data. we can do this  by fill_between method.
plt.fill_between(ages,py_salaries,alpha=0.25,y2=dev_salaries,where=(py_salaries>=dev_salaries),interpolate=True,label="Above AVG")
plt.fill_between(ages,py_salaries,alpha=0.25,y2=dev_salaries,color="red",where=(py_salaries<=dev_salaries),interpolate=True,label="Below AVG")
# here we can use an additional arguement y2 which indicates where to our filling will stop. 
# But if we dont add that arguement it will defaultly set to 0 and fill the whole area underneath the line.
# but we can see that it also interfaring little bit because we can hardly see the other lines behind the filling.
# to cope with this problem we can add alpha arguement which sets the transpirancy so that we can see through this better.
# if we use this with "conditional pressholes", then it can also give us some important information and some feedback as well.
# lets use this.
# lets add our y2 value to the overall median salary instead of using 0.
# now we can see exactly where our python line is crossing the median salary.
# when python is below the overall median, if fills up.
# when the line is over the overall median if fills down.that actually give us some nice feedbacks.
# we can also add some addtional conditionals here so that if only fills when the condition is True.
# lets say we want to set the color red when the line is under the median salary. we can do that by adding another arguement which is where. 
# we are going to set another arguement True which is interpolate.
# that will just make sure that certain x intersections dont get clipped and all of the regions are actually filled correctly.
# we can also fill in the area of two different line plots also.
# so instead of using overall median we can change y2 as dev_salaries.
# it really helps when we are trying to empasize them  in our line plots.
# we can also lebel this fill sections by adding label arguement.


plt.legend()
plt.tight_layout()
plt.title("Median Salary($) based on Age")
plt.xlabel("Age")
plt.ylabel("Median Salary($)")

#plt.savefig("plot7.png")
plt.show()