import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random

def Gaussian_noise(x):
    """ Apply gaussian noise to data input , 
    
    : param X : array data , input data
    
    : return : transformed data , data input noised
    """
    pure = x
    noise = np.random.normal(0, 1, 3000)
    data_noise = pure + noise
    return (data_noise)

def Standar_noised():
    """ Apply standar nised for signal ECG to data input, 
    
    : param X : array data, input data
    
    :return : transformed data, data input noised
    """

    Fs = 800
    f = 5
    sample = 800
    x = np.arange(sample)
    noise = 0.0008 * np.asarray(random.sample(range(0, 1000), sample))

    y = np.sin(2 * np.pi * f * x / Fs) + noise


    plt.plot(x, y)
    plt.xlabel('voltage(V)')
    plt.ylabel('sample(n)')
    plt.show()

    return (y)

def Masking_noise(x):
    """Apply noised with choose random value change wtih zero
    
    : param x : array data, input data
    
    :return : transformed data, data input noised
    """
    y = x
    for i in range(len(y/3)):
        xi = np.random.randint(0,len(y))
        y[xi] = 0

    return (y)


def act_function ():
    """ Apply gaussian noise to data input , 

    : param X : array data , input data

    : return : transformed data , data input noised
    """
    return ()