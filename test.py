import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Load some data
from datasets import Dataset
dataset = Dataset.from_dict({
    "feature1": [1,0,1,0,1],
    "feature2": ['blue', 'red', 'blue', 'red', 'blue'],
    "target": [1, 2, 1, 2, 1]
    }).with_format("tf")
print()

numerical = tf.reshape(dataset["feature1"], (len(dataset["feature1"]), -1))
input_shape = numerical.shape[1:]
# Create a Normalization layer and set its internal state using the training data
numerical = keras.Input(shape=(1,), name="feature1")

# Use StringLookup to build an index of the feature values and encode output.
lookup = keras.layers.StringLookup(output_mode="int", vocabulary=['blue', 'red'])
categorical = keras.Input(shape=(1,), name="feature2", dtype=tf.string)
x2 = lookup(categorical)

x = keras.layers.concatenate([numerical, tf.cast(x2, dtype=tf.float32)])
process_1 = keras.layers.Activation('relu')(numerical)
y = keras.layers.Dense(1, name="target")(process_1)


model = keras.Model(
    inputs=[numerical, categorical], outputs=[y]
)

model.compile(
    loss=keras.losses.BinaryCrossentropy(),
    metrics=[keras.metrics.CategoricalAccuracy()],
)

train_dataset = tf.data.Dataset.from_tensor_slices(
    (
        {"feature1": dataset['feature1'], "feature2": dataset['feature2']},
        {"target": dataset['target']},
    )
)
train_dataset = train_dataset.batch(5)
model.fit(train_dataset, epochs=5)
values = model.predict(
        {"feature1": dataset['feature1'], "feature2": dataset['feature2']}
    )
print(values)
