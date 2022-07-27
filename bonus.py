import numpy as np
import math
import matplotlib.pyplot as plt

data = np.random.normal(size=(100,))

'''
fxn should ahve no side effect on data structure
'''
def median(oriData):
    data = sorted(oriData)
    if (len(data) % 2 == 0):
        return (data[math.floor(len(data)/2)] + data[math.floor(len(data)/2)-1])/2
    else:
        return data[math.floor(len(data)/2)]

def mean(data):
    total = 0
    for value in data:
        total += value
    return total/len(data)

def min(oriData):
    data = sorted(oriData)
    return data[0]

def max(oriData):
    data = sorted(oriData)
    return data[-1]

def std(data):
    m = mean(data)
    totalDev = 0
    for value in data:
        totalDev += (value - m)**2
    return math.sqrt((totalDev)/len(data))

def testing():
    assert median([1,2,3]) == 2
    assert median([100.0, 5.0, 4.0, 7.0]) == 6.0
    assert mean([8, 100, 100, 50, 20]) == 55.6
    assert max([2, 4, 5, 10903, 3, -1003]) == 10903
    assert min([2, 4, 5, 10903, 3, -1003]) == -1003
    assert std([10, 12, 23, 23, 16, 23, 21, 16]) == 4.898979485566356

testing()

dataLine = plt.plot(data, label='data')

rollingMeans = []
rollingStd = []
for i in range(len(data)-1):
    curData = data[:i+1]
    rollingMeans.append(mean(curData))
    rollingStd.append(std(curData))

plt.plot(rollingMeans, label='mean')
plt.plot(rollingStd, label='std')

plt.ylabel('numbers')
plt.legend()

#plt.legend([dataLine], ['data'])

#plt.show()
