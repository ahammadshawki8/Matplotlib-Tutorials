import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use("ggplot")

data= np.random.randn(2,250)
data2= np.random.randn(30,30)
data3= np.random.randn(30,30)
eq=np.linspace(0,501,30)
vq=np.linspace(0,2001,30)
print(data[0])
print(data[1])


fig,ax=plt.subplots(nrows=2,ncols=2,sharex=True)
((ax1,ax2),(ax3,ax4))=ax

ax1.hist2d(data[0],data[1])
ax2.plot(data[0],data[1])
ax3.streamplot(eq,vq,data2,data3)

ax1.set_title("Complex 2D Figure")
ax2.set_title("Complex Linear Figure")
ax3.set_title("Complex Histogram Figure")
ax4.set_title("Complex Scatter")

#plt.table(data[0],data[1])
plt.show()