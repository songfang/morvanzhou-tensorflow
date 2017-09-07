# coding= utf-8

import tensorflow as tf
matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                      [2]])
product = tf.matmul(matrix1,matrix2)

# # method 1
# sess = tf.Session()
# result = sess.run(product)
# print result
# sess.close()

# method 2
with tf.Session() as sess:
    res = sess.run(product)
    print res
#自动sess.close()