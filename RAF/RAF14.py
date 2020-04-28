import random
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("seaborn")

def animate(i):
    data=pd.read_csv("data6.csv")
    x=data["x_value"]
    t1=data["total_1"]
    t2=data["total_2"]

    plt.cla()

    plt.plot(x,t1,color="r",label="Channel 1")
    plt.plot(x,t2,color="b",label="Channel 2")

    plt.legend(loc="upper left")
    plt.tight_layout()


ani=FuncAnimation(plt.gcf(),animate,interval=1000)

plt.title("Live Data")
plt.tight_layout()
plt.show()