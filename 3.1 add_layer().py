# coding=utf-8
import tensorflow as tf
import numpy as np


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

'''
3.2 建造神经网络
'''
x_data = np.linspace(-1,1,300)[:,np.newaxis]#新增一个维度
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 +noise

xs = tf.placeholder([None,1])
ys = tf.placeholder([None,1])

l1 = add_layer(x_data, 1, 10, activation_function = tf.nn.relu())
prediction = add_layer(l1, 10, activation_function=None)

loss = tf.reduce_sum(tf.square(y_data - prediction),
                     reduction_indices=[1])
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)
#for i in range(1,100)



