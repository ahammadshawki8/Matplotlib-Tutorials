import csv 
import random
import time

x_value=0
total_1=1000
total_2=1000

fieldnames=["x_value","total_1","total_2"] # these are going to be the headers of csv file.

# here we are opening the csv file and writing those headers.
with open("data6.csv", "w") as csv_file:
    csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
    csv_writer.writeheader()

while True:# this is a continuos loop of adding our values in csv file.
    with open("data6.csv", "a") as csv_file:# we are opening up the data in append mode.
        csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames)# creating a dictionary writer.

        # writing out this info dictionary here.
        info={"x_value":x_value,"total_1":total_1,"total_2":total_2}
        
        # writing the row in csv file.
        csv_writer.writerow(info)
        # printing out the row in the console for instant feedback.
        print(x_value,total_1,total_2)

        # updating the values
        x_value+=1
        total_1+=random.randint(-6,8)
        total_2+=random.randint(-5,6)

    # sleeping the time of our code by 1 sec.    
    time.sleep(1)