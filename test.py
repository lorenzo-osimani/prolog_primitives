import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras
from sklearn.model_selection import KFold
import time

start_time = time.time()
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
                'Acceleration', 'Model Year', 'Origin']

dataset = pd.read_csv(url, names=column_names,
                          na_values='?', comment='\t',
                          sep=' ', skipinitialspace=True).copy().dropna()

X = dataset.drop('MPG', axis = 1)
y = dataset.pop('MPG')

normalizer = tf.keras.layers.Normalization(axis = 1)
normalizer.adapt(X)
X = normalizer(X)

def createModel():
    model = keras.Sequential([
        tf.keras.layers.Dense(128, input_shape=(7, ), activation='relu', name='dense_1'),
        tf.keras.layers.Dense(64, activation='relu', name='dense_2'),
        tf.keras.layers.Dense(1, activation='linear', name='dense_output'),
    ])
    model.compile(
                    loss = "mse",
                    optimizer='adam',
                    metrics=['mae'],
                )
    return model

kfold = KFold(n_splits=5, shuffle=True, random_state=42)

scores = []
for train_index, test_index in kfold.split(X):
    X_train, X_test = np.take(X, train_index, axis = 0), np.take(X, test_index, axis = 0)
    y_train, y_test = np.take(y, train_index, axis = 0), np.take(y, test_index, axis = 0)
    
    model = createModel()
    model.fit(x=X_train,y=y_train, epochs=100, validation_split=0.05)

    predictions = model.predict(X_test)

    m = tf.keras.metrics.MeanAbsoluteError()
    m.update_state(y_test, predictions)
    scores.append(m.result().numpy())
print(f'Accuracies: {scores}')

print("--- %s seconds ---" % (time.time() - start_time))