
import xlrd
from matplotlib.pyplot import plot,show,title,legend
import numpy as np
import wfdb

sig, field = wfdb.rdsamp('100')
annsamp, anntype, nump , subtype, chan, aux , annfs  =wfdb.rdann('100','atr')
wfdb.plotwfdb(sig,field, annsamp)


file = xlrd.open_workbook('samples2.xls')
data = file.sheet_by_index(0)

x = []
y = []
z = []

for i in range(0,21600):
    x.append(data.cell(i,0).value)
    y.append(data.cell(i,1).value)
    z.append(data.cell(i,2).value)

title('EKG ')
plot(x,y, label = 'MLII')
plot(x,z, label = 'V1')
legend()
show()
