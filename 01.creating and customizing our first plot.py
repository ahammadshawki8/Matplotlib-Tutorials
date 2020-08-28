# lesson 1
# creating and customizing our first plot

from matplotlib import pyplot as plt 
# here we are importing pyplot from matplotlib module as plt which is a convention.

plt.style.use("dark_background")# adding different styles.
#plt.xkcd() # this will make our graph cartoonish. it is basically used for comics.

# now we are going to input our own data to pyplot.
# we will make a simple line graph on "median salary of developers based on age" survey.
ages_x =[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
#dev_x =[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# this list reprents developers ages in the x axis.
dev_y=[38496, 41000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
# this list represents the median salary in the y axis.

# now we need to plot this data. we can do that by plot function.
#plt.plot(ages_x, dev_y, linestyle= "--", color="#444444", marker=".", label="All developer")
# but now we cant see our graph if we run our code.
# to see our graph we can use show functon.
#plt.show()
# now we get a basic line plot.
# here we have pan, zoom, undo, redo, reset, configeration, save menu.

# now we should add more information in our plot.
# we dont know what that data represent after watching the plot as heir is no labels and title.

# we can give our entire plot a title. we can do that by title method.
plt.title("MEDIAN SALARY($) BY AGE")
# now we can label x an y axis by xlabel and ylabel method.
plt.xlabel("AGES")
plt.ylabel("MEDIAN SALARY($)")

#plt.show()
# now we can add more plots in our plot. suppose we want to add "median salary of python davelopers".
#py_x= [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_y= [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83670]
# but here we are using same x axis as first time. so we can- 
plt.plot(ages_x,py_y, "o-b", linewidth=3, label="Python")

#plt.show()
# now we are getting two lines for two different information. but we dont know which line represent which data.
# so we need to add legends. we can do that in 2 methods.
# first method,
#plt.legend(["All Developers","Python"])
# here we need to enter a list as an arguement.
# since we have ploted all developers data first. so first legend is all developers and so on.
#plt.show()

# second method:
# the first method is good but not great because we have to always remember the order tha twe have ploted our data.
# instead of doing that, w can add an extra label arguement when we are ploting our data.
"""please see there where we ploted data"""
# after doing that we will run the legend method.
#plt.legend()
# but now we are leaving it empty.
#plt.show()

# now we want to format our plot.
# what if we want different colors and lines and markers for different lines?
# there is a way to pass all fo these information in all at once by passing formatstring after the y-axis value when we are ploting.
# a format string consist of a part for color, marker, line.
# fmt="[marker][line][color]"
# other fmt such as [color][marker][line] are also supported. But note that, their parsing may be ambiguous.

# markers
# "."       point marker
# ","       pixel marker
# "o"       circle marker
# "v"       tringle down marker
# "^"       triangle up marker
# "<"       triangle left marker
# ">"       triangle right marker
# "1"       tringle down marker
# "2"       triangle up marker
# "3"       triangle left marker
# "4"       triangle right marker
# "h"       hexagon1 marker
# "H"       hexagon2 marker
# "a"       square marker
# "p"       pentagon marker
# "*"       star marker
# "+"       plus marker
# "x"       cross marker
# "D"       diamond marker
# "d"       thin diamond marker
# "|"       vertical line marker
# "_"       horizontal line marker

# line styles
# "-"        solid line style
# "--"       dashed line style
# "-."       dash-dot line style
# ":"        dotted line style

# color
# "b"       blue
# "g"       green
# "r"       red
# "c"       cyan
# "m"       magenta
# "y"       yellow
# "k"       black
# "w"       white

# now we are going to add this and show our plot.
#plt.show()
# but format string is not readable to human.
# we can specify color and linestyle and marker by adding extra arguements instead of format sting as it is readable.
#plt.show()

# we can also use hex color values for our lines as well.
# how hex values work?
# we first write # and then 3 pair of number. the first pair represents red, second pair blue ans the last pair green.
# we can find hex color palletes online.

# lets add some javascript data in our plot.
js_y=[37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x,js_y,color="#adad3b",linestyle="-",marker="o", linewidth=3, label="JavaScript")
#plt.show()

#suppose we want to mmake the lines of our plt more widthful.
# to do that we need to add another arguement in our plot method which is linewidth.
#plt.show()

# but here we can see our all dev line has been covered by javascript line as we enter js data late. 
# so we can cut all dev data and paste it after js data.
plt.plot(ages_x, dev_y, linestyle= "--", color="r", marker=".", label="All developer")
plt.legend()
# sometimes we can get little patting issues and our stuffs getting cut of in our plot.
# but we can take take of that by tight_layout() function.
plt.tight_layout()
#plt.show()

# but it is hard to tell when we cross certain salary.
# so if we add gridlines to our plot it would be lot easier to do that.
# we can do that by grid() method.
plt.grid(True)# here we must use a arguement which is True.
#plt.show()

# we can also change the styles of our plots to look it bit more nicer.
# we have some built_in styles in our matlotlib library.
# we can see the available style by style.available attribute.
print(plt.style.available)
# this is not a method, this is a attribute.
# we can add styles by using styles.use() method.
# we have to do that in the top of our code.
"""please look at the top"""
#plt.show()
# all built_in styles have default color and styles and grid.
# if we add our own color,lineswidth or style it will execute that, otherwise it will execute the default one.

# we can also make our plot comic style by xkcd() method.
# we have to do that in the top of our code.
"""please look at the top"""
# we should not use that when we are using another style in our plot.

# we can also save our plot in the plot menu and also by doing coding.
# first lets see what are the file types available for us to save our plot.
print(fig.canvas.get_supported_filetypes())

# we can use savefig function.
plt.savefig("plot1.png")
# it will be save to our current directory.
# but we can save that in another location too by adding the location as first arguement of our savefig function.
# we can also use some useful arguements in savefig() function. they are-

# transparent=True makes the background of the saved figure transparent if the format supports it.
# dpi=80 controls the resolution (dots per square inch) of the output.
# bbox_inches="tight" fits the bounds of the figure to our plot.

plt.show()
