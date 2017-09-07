# coding=utf-8
import tensorflow as tf
import numpy as np

# create data
#用断点调试
x_data=np.random.rand(100).astype(np.float32)
y_data=x_data * 0.1 + 0.3

#Variable
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))
init = tf.initialize_all_variables()

#gradient descent
y = Weights * x_data + biases
loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# session
sess = tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    #打印
    if step%20 == 0 :
        print step,sess.run(Weights),sess.run(biases)
sess.close()