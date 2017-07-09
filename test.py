import numpy as np
import csv
from matplotlib import pyplot as plt
import Similarity


def loadData():
    listData = []
    tempdata = []
    data = []
    num = 101
    ndata = 3000

    # inisiasi data awal
    inf = csv.reader(open('D:/[TELKOM UNIVERSITY]/Semester 7/TA 1/Dataset ECG/100.csv'))
    for col in inf:
        tempdata.append(col[1])
    for i in range(ndata):
        data.append(float(tempdata[i + 2]))
    listData.append(data)

    for i in range(1, 48):
        tempdata = []
        data = []
        #    print('tempdata', tempdata)
        temp = '.csv'
        tmp = str(num) + temp
        #    print('tmp : ',tmp)
        temp2 = 'D:/[TELKOM UNIVERSITY]/Semester 7/TA 1/Dataset ECG/'
        print(temp,'//',tmp,'//',temp2)
        res = temp2 + tmp
        # print(res)
        inf = csv.reader(open(res))
        for col in inf:
            tempdata.append(col[1])
        for i in range(ndata):
            data.append(float(tempdata[i + 2]))
        # print(data)
        listData = np.vstack((listData, data))
        num = num + 1

        # print('num : ', num)

        #     data = []

        # listData = np.asarray(listData)
        # print(listData)
        # print('data ke 1 : ',listData[1])
        # print('data ke 2 : ',listData[0])
        # print(listData.shape)

        # nois = Similarity.noised(listData[1])
        #     # print(nois)
        # sim = Similarity.similarity(listData[1],listData[0])
        #     #
        # print(sim)
    return (listData)

a = loadData()
# data = np.save()
# print (a)
# # visual data cutting
# fig = plt.figure()
# plt.plot(a[2])
# plt.title("Data ECG 'cuting'")
# plt.show()