import csv
import numpy as np
import pandas as pd
from pandas import DataFrame
import numpy as np
from matplotlib import pyplot as plt

#get data value only
input = []
data = []

inf = csv.reader(open('D:/[TELKOM UNIVERSITY]/Semester 7/TA 1/Dataset ECG RAW/121.csv','r'))
for col in inf:
    data.append(col[1])

# print data dan element
print("Data         : ", data[0])
print("Jenis data   : ", data[1])
# for i,elm in enumerate(data):
#     print("element : ", i)
#     print("isi data : ",data[i])


#potong data sebesar 30000 record
for i in range(3000):
    input.append(data[i+2])
    # print(input[i])

# find max input in input
maxD = max(input)
print ("max input : ", maxD)
for i, elm in enumerate(input):
    if input[i] == maxD:
        # print("isi = ", input[i])
        # print("element = ",i)
        elm_max = i


# get max R peak, and get 1500 data behind and 1500 data
fix = []
for i in range(elm_max-1500,elm_max+1500):
    fix.append(data[i])
print('panjang fix : ',len(fix))
# print(fix)


#transform from string to integer,
#karena fix terbaca sebagai string
fix2 = []
for i in range(len(fix)):
    t = float(fix[i])
    fix2.append(t)
print('=============[Data Intput]===============')
print(fix2)

# # make data to matrix
# d_matrix = np.array_split(input,1000)
# print(d_matrix)

# visual data cutting
fig = plt.figure()
plt.plot(fix)
plt.title("Data ECG 'cuting'")
plt.show()