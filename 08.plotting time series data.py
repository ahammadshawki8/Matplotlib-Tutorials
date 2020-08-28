# module 8
# plotting time series data.

# time series data are used to plotting dates in matplotlib.

import pandas as pd
from matplotlib import pyplot as plt
from datetime import timedelta, datetime
from matplotlib import dates as mpl_dates

plt.style.use("seaborn")

dates=[
    datetime(2019,5,25), 
    datetime(2019,5,26),
    datetime(2019,5,27),
    datetime(2019,5,28),
    datetime(2019,5,29),
    datetime(2019,5,30),
    datetime(2019,5,31)
    ]
# here we are using datetime module to create the dates.

y=[6,3,0,2,4,5,1]

# to plot this dates we can simply use plot_date() method.
plt.plot_date(dates,y,linestyle="solid")
# by default, this plot have markers instead of the dots connected by line.
# we can fix this by changing linestyle arguement to "solid".
# we can also remove this marker by changing the marker arguement to None. 
# we can also format our plot in different ways..
# we can run auto format x date method on our figure.
# this will rotate our date so that they fit bit nicer and change their allignment and things like that. 
# we will learn about figure and axis in the subplot video.
# but basically this is going to be a method on our figure and not on this pyplot(plt) object.
# to get the current figure from our pyplot we can use gcf() method.
# and now to run autofmt_xdate() method is on the current figure.
current_figure=plt.gcf()
current_figure.autofmt_xdate()
# now this dates are rotated and they have different allignment which makes the plot easier to read.
# we can also format our dates.
# to do that we have to import dates from matplotlib.
# from that imported module we are going to use the "DateFormatter" class.
# and we are going to passing in any format sting that we could also pass in the strftime method from the datetime class.
date_format=mpl_dates.DateFormatter("%b-%d-%Y")
# now we need to set these as the format of our x axis.
# so just like we grabbed the figure , we need to grab the axis to run this format method by gca() method.
current_axis=plt.gca()
# now we can change  the format of our x axis saying xaxis.set_major_formatter.
current_axis.xaxis.set_major_formatter(date_format)


plt.title("Bitcoin prices")
plt.xlabel("date")
plt.ylabel("closing price")
plt.tight_layout()
#plt.savefig("plot11.png")
plt.show()