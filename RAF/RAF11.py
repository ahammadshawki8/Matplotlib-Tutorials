import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import timedelta, datetime

plt.style.use("ggplot")

dates=[
    datetime(2019,5,25), 
    datetime(2019,5,26),
    datetime(2019,5,27),
    datetime(2019,5,28),
    datetime(2019,5,29),
    datetime(2019,5,30),
    datetime(2019,5,31)
    ]
y=[6,3,0,2,4,5,1]

plt.plot_date(dates,y,linestyle="solid",marker=None)

current_fig=plt.gcf()
current_fig.autofmt_xdate()

date_format=mpl_dates.DateFormatter("%b-%d-%Y")
current_axis=plt.gca()
current_axis.xaxis.set_major_formatter(date_format)

plt.title("Bitcoin Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")

plt.tight_layout()
plt.show()