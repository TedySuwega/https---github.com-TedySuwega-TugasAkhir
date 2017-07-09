import Load_Data
import tensorflow as tf
import numpy as np
import math


# variable that can change
lr = 0.01
epoch = 50
n_input = len(Load_Data.fix)
n_hidden_1 = 150
n_output = len(Load_Data.fix)
loss = 0
gradient = 0
x = Load_Data.fix
totE =[]

#
w1 = np.random.rand(n_input,n_hidden_1)
# b1 = np.random.rand(1,n_hidden_1)
w2 = np.random.rand(n_hidden_1,n_output)
# b2 = np.random.rand(1,n_output)

for i in range(epoch):
    A1 = 1/(1+np.exp(-(np.dot(x,w1))))
    A2 = 1/(1+np.exp(-(np.dot(A1,w2))))
    error = x - A2
    D2 = error *(A2*(1-A2))
    D1 = D2.dot(w2.T)*(A1*(1-A2))
    w2 += A1.T.dot(D2)*lr
    w1 += x.T.dot(D1)*lr

    print(error)
    totE += error
print(totE)
mse = totE**2/n_input
print(mse)
print(D1)

# for i in range(epoch):
#     encode = tf.nn.sigmoid(tf.add(tf.matmul(x,w1,b1)))
#     decode = tf.nn.sigmoid(tf.add(tf.matmul(encode,w2,b2)))
#     print(i)

# import numpy as np
#
# data = np.array([[0,0,1,],[0,1,1],[1,0,1],[1,1,1]])
# target = np.array([[0,1,1,0]]).T

# lr = 0.01
# maxep = 60000
# nparam = len(data[0])
# nhid = 4
# noutput = 1
# totE =[]

# w1 = np.random.rand(nparam,nhid)
# w2 = np.random.rand(nhid,noutput)
# for i in range(maxep):
#     A1 = 1/(1+np.exp(-(np.dot(data,w1))))
#     A2 = 1/(1+np.exp(-(np.dot(A1,w2))))
#     error = target - A2
#     D2 = error *(A2*(1-A2))
#     D1 = D2.dot(w2.T)*(A1*(1-A2))
#     w2 += A1.T.dot(D2)*lr
#     w1 += data.T.dot(D1)*lr
#
#     print(error)
#     totE += error
# print(totE)
# mse = totE**2/nparam
# print(mse)
# print(D1)