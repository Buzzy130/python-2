import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas.plotting
import warnings

warnings.filterwarnings('ignore')

dataFile = open("iris.data")
column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
# print(dataFile.readlines())
for stroke in dataFile.readlines():
    splited = stroke.split(',')
    if (len(splited)<3):
        continue
    column1.append(float(splited[0]))
    column2.append(float(splited[1]))
    column3.append(float(splited[2]))
    column4.append(float(splited[3]))
    column5.append(splited[4][:len(splited[4])-1:])
data = {"sepal length": column1,"sepal width": column2,"petal length": column3,"petal width": column4,"class": column5}
dataFrame = pd.DataFrame(data)
classes = ["Iris-setosa", "Iris-versicolor","Iris-virginica"]
arguments = ["sepal length","sepal width","petal length","petal width"]
dataFile.close()

def paramCorrelations():
    for i in range(0,4):
        correlation = dataFrame.groupby(arguments[i], group_keys=True).apply(lambda x: x)
        for j in range(i+1, 4):
            correlation.plot.scatter(0, y=arguments[j], s=12, grid=True)
            plt.xlabel(arguments[i]+", cm")
            plt.ylabel(arguments[j]+", cm")
            plt.show()

paramCorrelations()

def paramsClassCorelations():
    for i in range(0,4):
        fig, axes = plt.subplots(nrows=1, ncols=1)
        correlation = dataFrame.groupby("class").get_group(classes[0])
        correlation.plot.scatter(x=arguments[i], y="class", ax=axes, c='g', s=12, grid=True)
        correlation = dataFrame.groupby("class").get_group(classes[1])
        correlation.plot.scatter(x=arguments[i], y="class",  ax=axes,  c='b', s=12, grid=True)
        correlation = dataFrame.groupby("class").get_group(classes[2])
        correlation.plot.scatter(x=arguments[i], y="class",  ax=axes,  c='r', s=12, grid=True)
        plt.xlabel(arguments[i]+", cm")
        plt.ylabel("Class")
        plt.show()

paramsClassCorelations()

def twoParamsClassCorelations():
    for i in range(0,4):
        for j in range(i+1, 4):
            fig, axes = plt.subplots(nrows=1, ncols=1)
            correlation = dataFrame.groupby("class").get_group(classes[0])
            correlation.plot.scatter(x=arguments[i], y=arguments[j], ax=axes, c='g', s=12, grid=True)
            correlation = dataFrame.groupby("class").get_group(classes[1])
            correlation.plot.scatter(x=arguments[i], y=arguments[j], ax=axes,  c='b', s=12, grid=True)
            correlation = dataFrame.groupby("class").get_group(classes[2])
            correlation.plot.scatter(x=arguments[i], y=arguments[j], ax=axes,  c='r', s=12, grid=True)
            plt.xlabel(arguments[i]+", cm")
            plt.ylabel(arguments[j]+", cm")
            plt.show()

twoParamsClassCorelations()
















dataFile = open("agaricus-lepiota.data")
arguments = ["edibility", "cap-shape", "cap-surface", "cap-color", "bruises", "odor" ,"gill-attachment" ,
             "gill-spacing" ,"gill-size" ,"gill-color" ,"stalk-shape" ,"stalk-root" ,"stalk-surface-above-ring" ,
             "stalk-surface-below-ring" ,"stalk-color-above-ring" ,"stalk-color-below-ring" ,"veil-type" ,"veil-color" ,
             "ring-number" ,"ring-type" ,"spore-print-color" ,"population" ,"habitat"]
columns = [[] for i in range(len(arguments))]
for stroke in dataFile.readlines():
    splited = stroke.split(',')
    if (len(splited)<23):
        continue
    splited[22]=(splited[22])[:1:]
    for i in range(0, len(splited)):
        columns[i].append(splited[i])
dataFrame2 = pd.DataFrame({})
dataFile.close()
for i in range(len(arguments)):
    dataFrame2[arguments[i]] = columns[i]
# print(dataFrame2)

def paramsDistributionByClasses():
    for i in range(1, len(arguments)):
        dataFrame2.groupby(arguments[0])[arguments[i]].value_counts().unstack().plot.bar()
        plt.show()

paramsDistributionByClasses()























