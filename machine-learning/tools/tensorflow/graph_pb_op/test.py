#!/usr/bin/env python
# coding: utf-8

import tensorflow as tf

a = tf.Variable(1, name='xx')
b = tf.Variable(1, name='xx')
c = a + b

graph = tf.get_default_graph()
g = graph.as_graph_def()

print dir(graph)
print dir(g)

g_s = g.SerializeToString()

with open('graph.pb', 'w') as fd:
    fd.write(g_s)


