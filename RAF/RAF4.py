from matplotlib import pyplot  as plt

plt.style.use("dark_background")

slices=[65,35]
label=["Male","Female"]
color=["Blue","Pink"]

plt.pie(slices,labels=label,wedgeprops={"edgecolor":"black"},colors=color)

plt.title("Developers Ratio")
plt.tight_layout()
plt.show()