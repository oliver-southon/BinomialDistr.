import math
import statistics as st
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def meanStd(sample):
    mean = st.mean(sample)
    std = st.stdev(sample)
    return [mean,std]

def plot(mean, std):
    x = np.linspace(mean - 3*std, mean + 3*std, 100)
    plt.plot(x, stats.norm.pdf(x, mean, std))

def sampleToStats(sample):
    stats = meanStd(sample)
    mean = stats[0]
    std = stats[1]
    print("Mean: ", mean)
    print("Std: ", std)
    plot(mean, std)


sample = input("Enter the sample data: ")
sample = sample.split(" ")

sampleToStats(sample)