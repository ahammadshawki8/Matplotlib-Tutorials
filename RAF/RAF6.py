from matplotlib import pyplot as plt

plt.style.use("dark_background")

minutes=[1,2,3,4,5,6,7,8,9]
player1=[1,2,3,3,4,4,4,4,5]
player2=[1,1,1,1,3,2,2,3,4]
player3=[1,1,1,2,2,2,3,3,3]

labels=["player1","player2","player3"]
colors=["yellow","orange","red"]

plt.stackplot(minutes,player1,player2,player3,labels=labels,colors=colors)

plt.title("Players Contribution Graph")
plt.xlabel("minutes")
plt.ylabel("points")

plt.legend(loc="upper left")
plt.tight_layout()
plt.show()