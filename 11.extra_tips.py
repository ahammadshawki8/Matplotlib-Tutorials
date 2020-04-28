# Extra tips

# note that, here all of the codes are correct. 
# but since we are creating multiple plots they might be conflict with each other.
# so practising those in differnt module is recommanded.

# tip 1
# Categorical variables

# we can create custom figure with figure() method too.
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9,3))
# this figsize arguements indicate the figsize of our figure. now, its lenth is 9 and breadth in 3

# It is also possible to create a plot using categorical variables. 
# Matplotlib allows you to pass categorical variables directly to many plotting functions.

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.subplot(131)
plt.bar(names,values)
# subplot variable create subplots in the figure.
# call signature:
#       subplot(nrows, ncols, index, **kwargs)
#       subplot(pos, **kwargs)
#       subplot(ax)
# Parameters of subplots:
    # *args
    #     Either a 3-digit integer or three separate integers
    #     describing the position of the subplot. If the three
    #     integers are *nrows*, *ncols*, and *index* in order, the
    #     subplot will take the *index* position on a grid with *nrows*
    #     rows and *ncols* columns. *index* starts at 1 in the upper left
    #     corner and increases to the right.

    #     *pos* is a three digit integer, where the first digit is the
    #     number of rows, the second the number of columns, and the third
    #     the index of the subplot. i.e. fig.add_subplot(235) is the same as
    #     fig.add_subplot(2, 3, 5). Note that all integers must be less than
    #     10 for this form to work.

plt.subplot(1,3,2)
plt.scatter(names,values)

plt.subplot(133)
plt.plot(names,values)

plt.title("Categorical variables")
#plt.show()

# tip2

# sub-tip 1
# working with text

# we can work with text by text() function.
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')

# here the first and second arguement is coordinate.
# after that we use a mathematical expression.

# we can also change the fontsize, alpha, color and other props when setting perticular text.
plt.xlabel("Randoms",color="green",fontsize=10,alpha=0.75)
#plt.show() 


# sub-tip 2
# mathematical expressions in text

# matplotlib accepts TeX equation expressions in any text expression.
# For example to write the expression in the title, we can write a TeX expression surrounded by dollar signs
plt.title(r'$\sigma_i=15$')
# The r preceding the title string is important.
# it signifies that the string is a raw string and not to treat backslashes as python escapes.
# matplotlib has a built-in TeX expression parser and layout engine,
# and ships its own math fonts. for details, we can see :
"doc:/tutorials/text/mathtext."
#plt.show()

# sub-tip 3
# Annotating text

# The uses of the basic text() command above place text at an arbitrary position on the Axes.
# A common use for text is to annotate some feature of the plot,
# and the annotate() method provides helper functionality to make annotations easy. 
# In an annotation, there are two points to consider:
# the location being annotated represented by the argument xy and the location of the text xytext.
# Both of these arguments are (x, y) tuples.

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

# here arrowprops arguement which is a dictionary indicates that our annotating will be an arrow 
# and its facecolor will be black, the arrow will be start at xytext and end at xy.
# but it will be 0.05 away from xy this is what shrink does.

plt.ylim(-2, 2)
plt.show()

# tip 3
# non linear axes.
# we have seen linear and logarithmic axes earlier.

# we have some more non linear axes in matplotlib rater than logarithmic axes.
# they are symmatric log and logit scale.

# we can set those scales in the axes with yscale() and xscale() method. 

from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the open interval (0, 1)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()

# it is also possible to add our own scale.

# tip 4
# sample_plots
# matplot is a powerful tool to working and creating different types of simple and complex plots.
# some plots are

# 1. line plots
    # we can use plt.plot() to create line plots.

# 2. multiple subplots in one figure
    # we can use plt.subplot() or plt.subplots()

# 3. images
    # plt.imshow()

# 4. Contouring and pseudocolor
    # The plt.pcolormesh() function can make a colored representation of a two-dimensional array,
    # even if the horizontal dimensions are unevenly spaced.
    # The plt.contour() function is another way to represent the same data

# 5. histograms
    # plt.hist()
    # plt.hist2d()

# 6. paths
    # we can add arbitrary paths in Matplotlib using the matplotlib.path module

# 7. Three dimentional plotting
    # The mplot3d toolkit (see toolkit_mplot3d-tutorial and mplot3d-examples-index) has support 
    # for simple 3d graphs including surface, wireframe, scatter, and bar charts.

# 8. Stream plot
    # The plt.streamplot() function plots the streamlines of a vector field.
    # In addition to simply plotting the streamlines, it allows us to map the colors 
    # and/or line widths of streamlines to a separate parameter, 
    # such as the speed or local intensity of the vector field.
    # This feature complements the plt.quiver() function for plotting vector fields.

# 9. Ellipses
    # In support of the Phoenix <http://www.jpl.nasa.gov/news/phoenix/main.php>_ mission to Mars
    # (which used Matplotlib to display ground tracking of spacecraft),
    # Michael Droettboom built on work by Charlie Moad to provide an extremely accurate 
    # 8-spline approximation to elliptical arcs (see :class:~matplotlib.patches.Arc),
    # which are insensitive to zoom level

# 10. bar charts
    # vertical bar - plt.bar()
    # horizontal bar- plt.barh()
    # stacked bar - plt.stacked_bar()

# 11. pie charts
    # The plt.pie() function allows you to create pie charts.
    # Optional features include auto-labeling the percentage of area,
    # exploding one or more wedges from the center of the pie, and a shadow effect

# 12. tables
    # The plt.table() function adds a text table to an axes.

# 13. scatter plots
    # The plt.scatter() function makes a scatter plot with (optional) size and color arguments.
    # Here, the alpha attribute is used to make semitransparent circle markers.

# 14. gui widgets
    # Matplotlib has basic GUI widgets that are independent of the graphical user interface we are using,
    # allowing us to write cross GUI figures and widgets. See :mod:matplotlib.widgets 
    # and the widget examples <../../gallery/index.html>_.

# 15. filled curves
    # The plt.fill() function lets you plot filled curves and polygons

# 16. Date handling
    # You can plot timeseries data with major and minor ticks and custom tick formatters for both.

# 17. log plots
    # The plt.semilogx(), plt.semilogy() and plt.loglog() functions simplify the creation of logarithmic plots.

# 18. polar plots
    # plt.polar()

# 19. legends
    # The plt.legend() function automatically generates figure legends,
    # with MATLAB-compatible legend-placement functions. 

# 20. text notation on text objects
    # Below is a sampling of the many TeX expressions now supported by Matplotlib's internal mathtext engine.
    # The mathtext module provides TeX style mathematical expressions using FreeType <https://www.freetype.org/>_ 
    # and the DejaVu, BaKoMa computer modern, or STIX <http://www.stixfonts.org>_ fonts. 
    # See the :mod:matplotlib.mathtext module for additional details.

    # Matplotlib's mathtext infrastructure is an independent implementation and
    # does not require TeX or any external packages installed on your computer.
    # See the tutorial at :doc:/tutorials/text/mathtext.

# 21. Native text rendering
    # Although Matplotlib's internal math rendering engine is quite powerful,
    # sometimes we need TeX. Matplotlib supports external TeX rendering of strings with the usetex option.

# 22. EEG gui
    # We can embed Matplotlib into pygtk, wx, Tk, or Qt applications.
    # see more in: <https://github.com/nipy/pbrain>__.
    # The lower axes uses plt.specgram() to plot the spectrogram of one of the EEG channels.

# 23. xkcd text plots
    # Just for fun, Matplotlib supports plotting in the style of xkcd
    # more more: https://www.xkcd.com/

# 24. live plots
    # we can also plot live plots using animation module of matplotlib.

# sometimes we can create really complex plots by using some of our common functions.
