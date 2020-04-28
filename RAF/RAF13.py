import random
from itertools import count
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")

x_vals=[]
y_vals=[]

index=count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))
    plt.cla()
    plt.plot(x_vals,y_vals,linewidth=0.5)
    plt.title("Real Time Data")

ani=FuncAnimation(plt.gcf(),animate,interval=1000)

plt.tight_layout()
plt.show()