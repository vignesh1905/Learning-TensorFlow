# Trying tensor flow
import tensorflow as tf

#Initialize the variables

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)


addition = tf.add(a, b)

#Intitialize variables
init = tf.global_variables_initializer()

#Create session and run the graph
with tf.Session() as sess:
    sess.run(init)
    print "Addition: %i" % sess.run(addition, feed_dict={a:2, b:3})

sess.close
