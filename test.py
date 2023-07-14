import tensorflow as tf
from tensorflow import keras
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
(train_features, train_labels), (test_features, test_labels) = keras.datasets.boston_housing.load_data()


model = keras.Sequential([
    tf.keras.Input(shape=(13,), name="input"),
    tf.keras.layers.Dense(100, activation="relu"),
    tf.keras.layers.Dense(50, activation="relu"),
    tf.keras.layers.Dense(1, activation="relu")
])

model.compile(
                loss = "mse",
                optimizer=tf.keras.optimizers.Adam(),
                metrics=['mae', 'mse'],
            )
model.fit(x=train_features,y=train_labels, epochs=10)

predictions = model.predict(test_features)

m = tf.keras.metrics.MeanAbsoluteError()
m.update_state(test_labels, predictions)
score = m.result().numpy()

print(score)

print(np.shape([[1,2,3]]))
