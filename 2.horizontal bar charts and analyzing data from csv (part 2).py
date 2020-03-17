# lesson 2
# part 2
# horizontal bar charts and analyzing data from csv

# in previous lesson we learned how to create vertical bar charts.
# in these lesson, we will look at how to create horizontal bar chart.
# horizontal bar charts are used to created when there are a lot of data which looks too crowded in a vertical bar.
# now the data we are going to load in, it is belongs to a csv file.
# most of the time we need to use data from external sources like a csv file.
# sometimes we need to work little bit so the data is ready to be graphed.

# we want to create a bar chart of "most popular programming language"
# here we have a data.csv file in our current directory. we are going to build the graph based on this csv file.
import csv
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use("ggplot")
# first lets grab the data from the csv file.
# now there are multiple way to do that.
# we could use the read_csv method from pandas(faster way)
# we also could use the loadtxt() method from numpy.
# we could use csv module from standerd library and we are going to do that.(because it is popular)
with open("data.csv","r") as csv_file:
    csv_read=csv.DictReader(csv_file)
    # here we should add an arguement which is the csv file.
    # here we are going to use the DictReader() method from csv module to read the data in csv file.
    # the dictionary reader actually make a dictionary when we can access the values by key instead of index and that is pretty helpful.
    # here csv_read is a iterator that we can loop over. but we dont have to loop over every line because there are 40 thousands row in this data.
    # instead of that let us print the first row to see what they look like.
    # we can grab this row by next func.
    row=next(csv_read)# next method will grab the first row of this iterator.
    print(row)
    # we can also do that by:
    #print(list(csv_read)[0])
    # it will give us an OrderedDict. the keys are the headers of the csv file and their values are the responses for thst perticular person.
    print(row["LanguagesWorkedWith"])
    # the languages are deliminated with semicolons.
    # so we can make it list with split function.
    print(row["LanguagesWorkedWith"].split(";"))
    # here we get the list of the languages.
    # we want to make a plot based on the most popular languages from that survey.
    # so we need to keep a count of languages that each responed that they worked at.
    # there are lot of different ways that we can do that. But this is so common and python has a built_in class for this kind of things which is called Counter.
    # and its definately the best way and extreamly helpful to do something like this with Counters.
    # so we need to import Counter class from collections library.
    language_counter=Counter()# here we set it to empty counter. now we need to grad exact same list for every responder in data.csv.
    # we can do that by
    for row in csv_read:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))
print(language_counter)
# here we have the counter which is a dictionary with so many languages which are the keys. but we dont have to print all of this.
# lets plot 15 most common prog. language from this language_counter. we can do this by most_common method.
print(language_counter.most_common(15)) 
# this method returns a list here. And this list contains tuples. And each tuple contains two item.
# the first one is the languages and the second one is their apperences.

# now lets try to plot this data.
# we need to split the languages into their own list and corresponding counts into their own list for the x and y axis.
# there are couple more ways to do this.
languages=[]
popularity=[]
for tuples in language_counter.most_common(15):
    languages.append(tuples[0])
    popularity.append(tuples[1])
print(languages)
print(popularity)
reversed_languages=list(reversed(languages))
reversed_popularity=list(reversed(popularity))
# now we have two list for our x and y axis data.
# now lets make a vertical bar chart.
# plt.bar(languages,popularity) 
# here we can see that our chart is too messy. 
# so when we have a lot of items then it might be readble if we use horizontal barchart instead.
# we can do that by barh method
plt.barh(reversed_languages,reversed_popularity) 

plt.title("Most Popular Languages")
plt.xlabel("Number of People Who Use")
#plt.ylabel("Programming Languages")

plt.legend()
plt.tight_layout()
#plt.savefig("plot3.png")
plt.show()
# here we can see that the most popular language is showing in the bottom.
# maybe we want to see it in the top. to do that we need to reverse the x and y axis list.
"""Please look in line 67""" 