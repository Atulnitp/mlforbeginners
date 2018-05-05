import torch as ch
import logging
from activation import Activation
import numpy as np

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class NeuralNetwork(object):

        def __init__(self, train_x, train_y, hidden_layer=1, hidden_neurons=3):
            self.train_x = train_x
            self.train_y = train_y
            self.hidden_layer = hidden_layer
            self.hidden_neurons = hidden_neurons
            self.input_nodes = train_x.size()[0]
            self.output_nodes = train_y.size()[0]

            self.loop_counter = self.hidden_layer + 1
            self.W_in = np.random.normal(0.0, 0.1, (self.input_nodes, self.hidden_neurons))
            self.W_out = np.random.normal(0.0, 0.1, (self.hidden_neurons, self.output_nodes))
            self.Weight_Mat = list()
            self.Weight_Mat.append(self.W_in)
            self.Weight_Mat.append(self.W_out)
            if self.loop_counter > 2:
                for i in range(1, len(self.loop_counter)-1):
                    self.Wh_i = np.random.normal(0.0, 0.1, (self.hidden_neurons, self.hidden_neurons))
                    self.Weight_Mat.append(self.Wh_i)

        def feed_forward(self, weight, bias=0):
            self.weight = self.Weight_Mat
            self.bias = bias
            for i in range(len(self.weight)):
                X_i = ch.mm(self.weight[i], self.train_x)
                A_i = Activation.sigmoid(X_i)
                self.train_x = A_i
            self.E_total = 0
            for i in range(len(A_i)):
                E = Activation.L2_loss(A_i[i], self.train_y[i])
                self.E_total += E

        def backprop(self, lr=0.001):
            self.lr = lr