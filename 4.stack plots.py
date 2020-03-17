# module 4
# stack plots

# stack plot are also called area plot.
# they are pretty simmilar to pie charts because they show us how the propotions of different values contribute to the whole.
# but instead of doing this just one time, stack plot shows us over time.
# stack plots are really good for data when we want to track a total and also track down a total by a specific catagory.

# lets say we are playing video game and we have teams and we want to keep track the total points for the whole team 
# and also how many points each individual player contributed.

from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")

minutes=[1,2,3,4,5,6,7,8,9]# this is the minutes list of the game
player1=[1,2,3,3,4,4,4,4,5]# this players list indicates how many points they have scored in entire game up to that point.
player2=[1,1,1,1,3,2,2,3,4]
player3=[1,1,1,2,2,2,3,3,3]

# we can use pie plots to see players contribution after each minutes.
#plt.pie([1,1,1],labels=["player1","player2","player3"])
# now lets use a stack plot to look at the distributation over an entire series of minutes.
# we can do that by stackplot method.
plt.stackplot(minutes,player1,player2,player3,labels=["player1","player2","player3"],colors=["#6d904f","#fc4f30","#008fd5"])
# first we need to pass in the x axis value that represents the prograssion which is minutes.
# now we can pass in our player list one by one as additional arguement. This can also be a multidimentional array if our dta is arranged that way.
# but ours are currently individual one-by list.
# we can also add labels in our list by lables arguement and legend() method. it will make our labels activated.
# but this legends are not in the exact place where we need. so we are going to change its location.
# we can do that by adding extra arguement in our legend method which is loc.
# we can also specific the exact location of legends by passing coordinates.
# we can find it by searching in google matplolib legends to know more information about it.
# we can also customize the color by adding extra color arguement.

plt.legend(loc="upper left")
# we can also specify the location using coordinates by adding tuple instead of string.
#plt.legend(loc=(0.07,0.05))
plt.title("My awesome stack plot")
plt.tight_layout()
#plt.savefig("plot6.png")
plt.show()
# another common usecase for stack plots is to visualize something that maintains a total.
# for example, lets say that we have a project and our team is allowed to work in that project 8 hours at a day.
# we could use a stack plot to show who is working with that project most of the time.
# stack plots is used in different alalyticts such as youtube analyticts use this for video views and traffic sources.


# Blue  -   #008fd5
# Red   -   #fc4f30
# Yellow-   #e5ae37
# Green -   #6d904f
