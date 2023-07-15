import tensorflow as tf
from tensorflow import keras
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
(train_features, train_labels), (test_features, test_labels) = keras.datasets.boston_housing.load_data()


normalizer = tf.keras.layers.Normalization(axis = 1)
normalizer.adapt(train_features)
train_features = normalizer(train_features)
test_features = normalizer(test_features)

print(train_features)


model = keras.Sequential([
    tf.keras.layers.Dense(128, input_shape=(13, ), activation='relu', name='dense_1'),
    tf.keras.layers.Dense(64, activation='relu', name='dense_2'),
    tf.keras.layers.Dense(1, activation='linear', name='dense_output'),
])

model.compile(
                loss = "mse",
                optimizer='adam',
                metrics=['mae'],
            )
model.fit(x=train_features,y=train_labels, epochs=100, validation_split=0.05)

predictions = model.predict(test_features)
print(predictions)

m = tf.keras.metrics.MeanAbsoluteError()
m.update_state(test_labels, predictions)
score = m.result().numpy()

print(score)
