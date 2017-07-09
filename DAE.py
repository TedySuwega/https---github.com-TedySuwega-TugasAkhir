from __future__ import division, print_function,absolute_import
import numpy as np
from math import*
import Load_Data
import tensorflow as tf
import test

from AutoEncoder_tensor import display_step


class DAE (object):

    def __init__(self,
                 epoch=100,
                 n_hidden=100,
                 bias=None,
                 weight=None,
                 output = None,
                 learning_rate = 0.001,
                 n_input= 30000,
                 input = None):
        self.epoch = epoch
        self.nhidden = n_hidden
        self.output = output
        self.bias = bias
        self.weight = weight
        self.n_input = n_input
        self.learning_rate = learning_rate
        self.input = input

        if self.bias is None:
            bias= {
                'encoder_b1': tf.Variable(tf.random_normal([n_hidden])),
                'decoder_b2': tf.Variable(tf.random_normal([n_input])),
            }

        if self.weight is None:
            weight = {
                'encoder_h1': tf.Variable(tf.random_normal([n_input, n_hidden])),
                'decoder_h2': tf.Variable(tf.random_normal([n_hidden, n_input])),
            }

    def noised (self, input):
        pure = input
        noise = np.random.normal(0, 1, 100)
        signal_noise = pure + noise
        return (signal_noise)

    def encoder(self,input):
        layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(input, self.weight['encoder_h1']),self.bias['encoder_b1']))
        return (layer_1)

    def decoder(self,input):
        layeroutput= tf.nn.sigmoid(tf.add(tf.matmul(input, self.weight['decoder_h1']),self.bias['decoder_b1']))
        return (layeroutput)

    def similarity(self,layeroutput,input):
        similar = sqrt(sum(pow(a - b, 2) for a, b in zip(layeroutput, input)))
        return similar

    def train_model(self):

        # Construct model
        enc = self.encoder(input)
        dec = self.decoder(enc)

        # Prediction / find the similarity
        y_pred = dec
        # Targets (Labels) are the input data.
        y_true = input

        # Define Loss and optimizer, minimize the squared error
        cost = tf.reduce_mean(tf.pow(y_true - y_pred, 2))
        optimizer = tf.train.RMSPropOptimizer(self.learning_rate).minimize(cost)

        # Initializing the variables
        Init = tf.initialize_all_variables()

        # Launch the Graph
        # Using InteractiveSession (more convenient while using Notebooks)
        sess = tf.InteractiveSession()
        sess.run(Init)

        for i in range(self.epoch):
            # sim = DAE.similarity(DAE.decoder.layeroutput,input)
            _, c = DAE.sess.run([self.optimizer, self.cost], feed_dict={input: Load_Data.fix})
            #display per epoch
            if self.epoch % display_step == 0:
                print("Epoch:", '%04d' % (self.epoch + 1), "cost=", "{:.9f}".format(c))

        print("=====Optimization Finished!!======")

        self.encoder = enc
        self.decoder = dec




