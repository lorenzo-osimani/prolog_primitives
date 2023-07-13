import tensorflow as tf
from tensorflow import keras
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
(train_features, train_labels), (test_features, test_labels) = keras.datasets.boston_housing.load_data()

'''input = tf.keras.Input(shape=(13,), name="input")
a = tf.keras.layers.Dense(128, activation="relu")(input)
b = tf.keras.layers.Dense(64, activation="relu")(a)
c = tf.keras.layers.Dense(32, activation="relu")(b)
d = tf.keras.layers.Dense(16, activation="relu")(c)
e = tf.keras.layers.Dense(1)(d)

model = keras.Sequential([
    tf.keras.Input(shape=(13,), name="input"),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(1, activation="relu")
])

model.compile(
                loss = "mae",
                optimizer=tf.keras.optimizers.Adam(),
                metrics=['mae', 'mse'],
            )
model.fit(x=train_features,y=train_labels, epochs=100)

predictions = model.predict(test_features)
print(test_labels)
print(predictions)

score = tf.keras.metrics.mean_absolute_error(test_labels, predictions)

totalscore = tf.get_static_value(sum(score)/len(score))

print(totalscore)'''

value = np.reshape([[0, 0], [1, 1], [2, 2], [3, 3]], (2, 4))
print(len(value))

