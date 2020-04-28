import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import timedelta,datetime

plt.style.use("fivethirtyeight")

data=pd.read_csv("data4.csv")
data["Date"]=pd.to_datetime(data["Date"])
data.sort_values("Date",inplace=True)

close=data["Close"]
date=data["Date"]

# new_Pdate=[]
# for dates in date:
#     new_date=datetime.strptime(dates,"%b-%d-%Y")
#     new_Pdate.append(new_date)


plt.plot_date(date,close,linestyle="solid")

current_fig=plt.gcf()
current_fig.autofmt_xdate()

date_fmt=mpl_dates.DateFormatter("%b-%d-%Y")
current_axis=plt.gca()
current_axis.xaxis.set_major_formatter(date_fmt)

plt.title("Bitcoin Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")

plt.tight_layout()
plt.show()