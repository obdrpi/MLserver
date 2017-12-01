from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib

import numpy as np
import tensorflow as tf

#Define the training inputs
def get_train_inputs():
  x = tf.constant(training_set.data)
  y = tf.constant(training_set.target)

  return x, y


# Define the test inputs
def get_test_inputs():
  x = tf.constant(test_set.data)
  y = tf.constant(test_set.target)

  return x, y

NETWORK_TRAFFIC="network-training.csv" 

NETWORK_TEST="network-test.csv"

training_set = tf.contrib.learn.datasets.base.load_csv_without_header(filename=NETWORK_TRAFFIC, target_dtype=np.int, features_dtype=np.int)

test_set = tf.contrib.learn.datasets.base.load_csv_without_header(filename=NETWORK_TEST, target_dtype=np.int, features_dtype=np.int)

feature_columns = [tf.contrib.layers.real_valued_column("", dimension=8)]

classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                            hidden_units=[10, 20, 10],
                                            n_classes=2,
                                            model_dir="/tmp/attack_model")

# Fit model.
classifier.fit(input_fn=get_train_inputs, steps=2000)

# Evaluate accuracy.
accuracy_score = classifier.evaluate(input_fn=get_test_inputs,
                                     steps=1)["accuracy"]

print("\nTest Accuracy: {0:f}\n".format(accuracy_score))


