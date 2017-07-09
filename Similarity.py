from math import *
import numpy as np

def similarity(layeroutput, input):
    similar = sqrt(sum(pow(a - b, 2) for a, b in zip(layeroutput, input)))
    return similar

def noised(input):
    pure = input
    noise = np.random.normal(0, 1, 100)
    signal_noise = pure + noise
    return (signal_noise)
