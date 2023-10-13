import numpy as np
import csv
import sklearn
from math import sqrt
from dtaidistance import dtw
reddit = []
uwyo = []
iteration_counter = 0
is_reddit = True


with open('/Users/mattyjpru/Desktop/PowerBox_29536_-8585049994528028928.csv') as data_set:
    reader = csv.reader(data_set)
    time=0
    dicts_temp= {}
    for row in reader:
        if(time==60000):
            time=0.0
            if(is_reddit):
                reddit.append(dicts_temp)
            else:
                uwyo.append(dicts_temp)
            dicts_temp= {}
            is_reddit = not is_reddit
        if(time>=120000):
  #          print(iteration_counter)
            iteration_counter = iteration_counter+1
            is_reddit=not is_reddit
            time=0
            if(is_reddit):
                reddit.append(dicts_temp)
            else:
                uwyo.append(dicts_temp)
            dicts_temp= {}
        if(iteration_counter>100):
            break
            ##print(float(row[0])-1)
        if(is_reddit):
            #float(row[0])-1
            dicts_temp[time] = row[1]
        else:
            #float(row[0])-1
            dicts_temp[time] = row[1]
        time=time+2

#for value in reddit[0].items():
#   print(value)


####################### KNN ##########################


# Finding the optimal k value
