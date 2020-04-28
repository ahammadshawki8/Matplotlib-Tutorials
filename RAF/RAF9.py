from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("dark_background")

x       =   [5,7,8,5,6,7,9,2,3,4,4,4,2,6,3,6,8,6,4,1]
y       =   [7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]
colors  =   [7,5,9,7,5,7,2,5,3,7,1,2,8,1,9,2,5,6,7,5]
sizes   =   [209,486,381,266,191,315,185,228,174,558,239,394,399,153,273,293,436,501,397,539]

plt.scatter(x,y,marker="*",c=colors,cmap="Reds",s=sizes,edgecolor="white",linewidth=1.25,alpha=0.5)

cbar=plt.colorbar()
# this will create color bar in our plot
cbar.set_label("Ratings")
# this will set the label of our coloe bar.

plt.title("Sample_data")

plt.legend()
plt.tight_layout()
plt.show()
