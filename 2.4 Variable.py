# coding=utf-8
import tensorflow as tf

counter = tf.Variable(0,name = 'counter')
print counter.name

one = tf.constant(1)

# 以下三行将函数作为一个对象？在sess.run时才触发？输出的是函数的返回值？？？
init = tf.initialize_all_variables()
newValue = tf.add(counter,one)
newCounter = tf.assign(counter,newValue)


with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(newValue)
        print sess.run(newCounter)
