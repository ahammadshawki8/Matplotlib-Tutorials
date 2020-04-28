from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

languages=['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
popularity=[27175, 25532, 21932, 16836, 16407]
colors=["orange","grey","green","blue","red"]
explode=[0,0,0,0.2,0]

plt.pie(popularity,labels=languages,colors=colors,wedgeprops={"edgecolor":"White"},
        startangle=80,explode=explode,shadow=True,autopct="%1.3f%%")

plt.title("Most Popular Programming Languages")
plt.show()