# lesson 2
# creating Bar charts (vertical)

from matplotlib import pyplot as plt
import numpy as np # it is also a convention.

plt.style.use("fivethirtyeight")

ages_x =[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indexes=np.arange(len(ages_x))
# it will create a varible called x_indexes and that is a list of values. 
# and those values are going to be a numbered version of our ages_x values.
# basically it is like a list counting from 0 to the last item but the speciality of it is that it is a numpy array.
width=0.25
# now we are going to substract and add the width to our x_values

dev_y=[38496, 41000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

#plt.plot(ages_x, dev_y, linestyle= "--", color="w", marker=".", label="All developer")
# if we use plot method it will create a line plot by default.
# if we want barchart we can use bar method instead of plot method.
plt.bar(x_indexes-width, dev_y, width=width , color="#444444", label="All developer")
# bar method doesn't have marker arguement.

# we can also mix_up bar plots and line plots together.
# py_y= [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83670]
# plt.plot(ages_x,py_y, "o-b", linewidth=3, label="Python") 

# js_y=[37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
# plt.plot(ages_x,js_y,color="#adad3b",linestyle="-",marker="o", linewidth=3, label="JavaScript")

# what if we want to plot py. and js. data as bars. 
py_y= [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83670]
plt.bar(x_indexes,py_y, color="b", width=width, label="Python") 

js_y=[37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes+width,js_y,color="y",width=width, label="JavaScript")
# but thats not what we are wanting.
# we cant see the data properly.
# how can we put these datas side by side?
# we can do this by off setting the x values each time we plot some data.
# to do that we have to import numpy and use that to grab a range of values to our x axis.
# after importing numpy, we are going to create a range(x_indexes) from our x values below our ages_x values.
# when we have created the x_indexes range we will use them as x_values when we ploted our data.
# but now we are using x_indexes, we can actually shift the location ofn these by adding or substracting to our values Here.
# right now, they are all stacked up into each another.lets shift our first bar to left and second bar to right.
# but how far we actually want to shift this?
# we are going to shift them by the exact width of a bar.
# so do this it would be nice if we  specify a width for our bars.
# the bars have a default width. but just be sure lets create our own width variable below the x_indexes.
# and we actually need to tell the plot that we want the width of the bar equal to our width.
# we can do that by adding another variable which is width.
# but now, when we see our x values we can find that our plot is not using ages_x, it is using x_indexes range.
# we dont want that.to fix this, we can do that by xticks method.
plt.xticks(ticks=x_indexes, labels=ages_x)
# here we need to write two arguement. one is our ticks which is equal to x_indexes and another one is labels which is equal to ages_x.
 

plt.title("MEDIAN SALARY($) BY AGE")
plt.xlabel("AGES")
plt.ylabel("MEDIAN SALARY($)")

plt.legend()
plt.tight_layout()
plt.show()

