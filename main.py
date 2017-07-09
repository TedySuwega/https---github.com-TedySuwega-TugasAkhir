# import SDAE
# import DAE
# import Load_Data
import test
import utilities
from matplotlib import pyplot as plt


if __name__ == '__main__':
    a = test.loadData()
    print(a)
    # visual data cutting
    fig = plt.figure()
    plt.plot(a[2])
    plt.title("Data ECG 'cuting'")
    plt.show()



#         a = utilities.Standar_noised()
#
# print (a)