#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tf.mnist.input_data  as input_data
import tensorflow as tf


if __name__ == '__main__':
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
