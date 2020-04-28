import csv
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use("ggplot")

with open("data.csv","r") as myfile:
    csv_read=csv.DictReader(myfile)
    row=next(csv_read)
    print(row['LanguagesWorkedWith'].split(";"))

    language_counter=Counter()
    for row in csv_read:
        language_counter.update(row['LanguagesWorkedWith'].split(";"))
print(language_counter)
print(language_counter.most_common(10))

languages=[]
popularity=[]
for tuples in language_counter.most_common(10):
    languages.append(tuples[0])
    popularity.append(tuples[1])
print(languages)
print(popularity)

reversed_languages=list(reversed(languages))
reversed_popularity=list(reversed(popularity))

plt.barh(reversed_languages,reversed_popularity)

plt.title("Most Popular Language")
plt.xlabel("Popularity")

plt.show()