# this file contains the functions shared between python script and jupyter notebook

# import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt


# read file
def read_file(file):
    return pd.read_csv(file)


# find maximum
def findMin(data):
    min_ind = 0
    for i in range(len(data)):
        if data[i] < data[min_ind]:
            min_ind = i
    return data[min_ind]


# find minimum
def findMax(data):
    max_ind = 0
    for i in range(len(data)):
        if data[i] > data[max_ind]:
            max_ind = i
    return data[max_ind]


# find mean
def calcMean(data):
    total = 0
    for ele in data:
        total += ele
    return round(total / len(data), 3)


def visulize_figure(data_frame):
    plt.scatter(data_frame["wt"], data_frame["mpg"])
    plt.xlabel("Weight, lbs")
    plt.ylabel("Miles per Gallon, miles")
    plt.title("Miles per gallon changes with automible weight")
    plt.show()
