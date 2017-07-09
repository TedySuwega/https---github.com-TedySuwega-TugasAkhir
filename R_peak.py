import Load_Data
import sys
from matplotlib import pyplot as plt
from numpy import NaN, Inf, arange, isscalar, asarray, array
import numpy as np
q= Load_Data.input

def peakdet_org(v, delta, x=None):
# """
# Converted from MATLAB script at http://billauer.co.il/peakdet.html
#
# Returns two arrays
#
# function [maxtab, mintab]=peakdet(v, delta, x)
# %PEAKDET Detect peaks in a vector
# %        [MAXTAB, MINTAB] = PEAKDET(V, DELTA) finds the local
# %        maxima and minima ("peaks") in the vector V.
# %        MAXTAB and MINTAB consists of two columns. Column 1
# %        contains indices in V, and column 2 the found values.
# %
# %        With [MAXTAB, MINTAB] = PEAKDET(V, DELTA, X) the indices
# %        in MAXTAB and MINTAB are replaced with the corresponding
# %        X-values.
# %
# %        A point is considered a maximum peak if it has the maximal
# %        value, and was preceded (to the left) by a value lower by
# %        DELTA.
#
# % Eli Billauer, 3.4.05 (Explicitly not copyrighted).
# % This function is released to the public domain; Any use is allowed.
#
# """
    maxtab = []
    mintab = []

    if x is None:
        x = arange(len(v))

    v = asarray(v)

    if len(v) != len(x):
        sys.exit('Input vectors v and x must have same length')

    if not isscalar(delta):
        sys.exit('Input argument delta must be a scalar')

    if delta <= 0:
        sys.exit('Input argument delta must be positive')

    mn, mx = Inf, -Inf
    mnpos, mxpos = NaN, NaN

    lookformax = True

    for i in arange(len(v)):
        this = float(v[i])
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]

        if lookformax:
            if this < mx - delta:
                maxtab.append((mxpos, mx))
                mn = this
                mnpos = x[i]
                lookformax = False
        else:
            if this > mn + delta:
                mintab.append((mnpos, mn))
                mx = this
                mxpos = x[i]
                lookformax = True

    return array(maxtab), array(mintab)

# series = q
# maxtab, mintab = peakdet_org(series,0.3)
# # print(mintab)
#
# # plt.figure()
# # plt.plot(maxtab,mintab)
# # plt.show()
#
# plt(series)
# plt.scatter(array(maxtab)[:, 0], array(maxtab)[:, 1], color='blue')
# plt.scatter(array(mintab)[:, 0], array(mintab)[:, 1], color='red')
# plt.show()

yg = np.array([  1.57438571e+01,   7.61257196e+00,   1.52430926e-01,
     1.36516560e-01,   5.15979768e+00,   1.64124707e+01,
     1.89515520e+01,   1.42487909e+01,   3.54018477e+00,
     1.14062707e+01,   1.02388242e+01,   1.87826244e+01,
     1.95441484e+01,   2.24071140e+01,   2.02983868e+01,
     1.82032003e+01,   1.73453618e+01,   1.47026081e+01,
     1.78448059e+01,   2.58816032e+01,   6.56713725e+01,
     1.25462491e+02,   1.87772026e+02,   2.59049063e+02,
     3.51947933e+02,   4.53792943e+02,   5.19410345e+02,
     5.52208254e+02,   5.70822845e+02,   5.80361497e+02,
     5.89003135e+02,   6.06347208e+02,   6.43622339e+02,
     6.62009186e+02,   6.42148423e+02,   5.92902622e+02,
     5.20002943e+02,   4.41806277e+02,   3.48097035e+02,
     2.63343718e+02,   1.78357030e+02,   1.34485314e+02,
     1.17501271e+02,   1.09649638e+02,   8.43415105e+01,
     7.13899534e+01,   5.18412945e+01,   3.35901390e+01,
     2.08088661e+01,   3.07336351e+01,   4.79581429e+01])

series = q
maxtab, mintab = peakdet_org(series, .3)
plt.plot(series)
plt.scatter(array(maxtab)[:, 0], array(maxtab)[:, 1], color='blue')
plt.scatter(array(mintab)[:, 0], array(mintab)[:, 1], color='red')
plt.show()
print(maxtab)
print('maxtab : ',maxtab[0][0])
print('load data : ',Load_Data.input[int(maxtab[2][0])])
print('len maxtab : ',len(maxtab))

for i in range(len(maxtab)):
    # ce.append(Load_Data.input[maxtab[i][0]])
    print(Load_Data.input[int(maxtab[i][0])])


