# extra practice
from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")

languages=['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']#[, 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
popularity=[27175, 25532, 21932, 16836, 16407]#[, 14812, 12450, 10470, 9448, 8577, 8315, 3652, 3434, 3303, 2676]
colors=["orange","grey","green","blue","red"]
explode=[0,0,0,0.1,0]# this value will represent how much we emphasis the slice.
# 0 keep the slice how it is. any number beside 0 will represent the fraction of the radious that we like to explode the values.


plt.pie(popularity,labels=languages,wedgeprops={"edgecolor":"black"},colors=colors,
        explode=explode,shadow=True,startangle=55,autopct="%1.1f%%")
        # autopct is a format string here which is "%1.1f%%"
        # autopct refers to auto percentage. It will show the parcentage of area of each slices in the pie.

plt.title("Popular Programming Languages")
plt.tight_layout()
#plt.savefig("plot5.png")
plt.show()

# but when there are lots of information we should use bar charts.
# we should not use pie charts because it seems little crowded and it is too difficult to compare between two slices.
# we should use pie charts if we have less than 5 items.

# lot of the time we see pie charts that have emphasis on one piece of the chart.
# lets say we want to emphasis on python piece. 
# we can do this by passing an explode arguement and this will be a list of values that will offset the slice.
"""Please see up"""

# there are few more things we can do with pie charts.
# we can add a shadow in our chart by adding an arguement shadow = True.

# another arguement we can pass in is the starting angle. It will rotate our chart.

# if we want to display the parcentage that our each slices, we can add in an arguement for that as well.
# this is called autopct. pct means percent.