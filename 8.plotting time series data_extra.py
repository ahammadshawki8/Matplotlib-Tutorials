# module 8
# extra 
# plotting real world time series data.

import pandas as pd
from matplotlib import pyplot as plt
from datetime import timedelta, datetime
from matplotlib import dates as mpl_dates

plt.style.use("seaborn")

data=pd.read_csv("data4.csv")

# converting string into date with panda
data["Date"]=pd.to_datetime(data["Date"])
# here we are just converting that date coloumn to a datetime using the to_datetime method.
# and then we are replacing those values with converted datetimes.
# now we need to sort that. we can use sort_values() method. and we are going to sort the data by date.
data.sort_values("Date",inplace=True)
# we want to sort those data in place by changing the value True.
# in place just basically means that it goes head and
# modifies that date instead of us needing to say like data=data.sort()

price_date=data["Date"]
price_close=data["Close"]

# converting string into date with strptime.
#new_price_date=[]
#for dates in price_date:
    #new_date=datetime.strptime(dates,"%Y-%m-%d")
    #new_price_date.append(new_date)

plt.plot_date(price_date,price_close,linestyle="solid")
# right now this might look okay. but it's not actually plotting out our x axis as dates.
# its actually plotting this out as string.
# so we can solve this problem by strptime() method.
"Please look UP"
# we can also do that with panda.
"Please look UP"

current_figure=plt.gcf()
current_figure.autofmt_xdate()

plt.title("Bitcoin prices")
plt.xlabel("date")
plt.ylabel("closing price")
plt.tight_layout()
#plt.savefig("plot12.png")
plt.show()