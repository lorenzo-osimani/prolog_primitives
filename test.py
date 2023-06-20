import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

'''
from tensorflow.keras.layers.experimental import preprocessing

def preprocess_schema(schema):
    # Create a dictionary to store the preprocessed features
    preprocessed_features = {}
    
    # Iterate over each feature in the schema
    for feature_name, feature_info in schema.items():
        feature_type = feature_info['type']
        # Perform preprocessing based on the feature type
        if feature_type == 'numerical':
            # Convert the numerical data to a TensorFlow constant tensor
            feature_data = tf.constant([feature_info['data']], dtype=tf.float32)
            # Reshape the data to have a known shape
            # Create a Normalization layer and adapt it to the data
            normalization_layer = preprocessing.Normalization()
            normalization_layer.adapt(feature_data)
            preprocessed_features[feature_name] = normalization_layer
        elif feature_type == 'categorical':
            # Create an IntegerLookup layer and adapt it to the data
            integer_lookup_layer = preprocessing.StringLookup(max_tokens=5, output_mode='binary', vocabulary = ['cat', 'dog', 'bird'])
            preprocessed_features[feature_name] = integer_lookup_layer
    
    return preprocessed_features

schema = {
    'feature1': {
        'type': 'numerical',
        'data': [1, 2, 3, 4, 5]
    },
    'feature2': {
        'type': 'categorical',
        'data': ['cat', 'dog', 'bird', 'dog', 'bird']
    }
}

preprocessed_features = preprocess_schema(schema)
# Inspect the attributes and types of the resulting schema
resulting_schema = {}

for feature_name, preprocessing_layer in preprocessed_features.items():
    resulting_schema[feature_name] = {
        'type': tf.dtypes.as_dtype(preprocessing_layer.get_config()['dtype'])
    }
    try:
        resulting_schema[feature_name]["vocab"] = preprocessing_layer.get_vocabulary(include_special_tokens=True)
    except:
        None
    
print(resulting_schema)   

'''
# Load some data
from datasets import Dataset
dataset = Dataset.from_dict({
    "feature1": [1,2,3,4,5],
    "feature2": ['blue', 'red', 'blue', 'red', 'blue'],
    "target": [1, 2, 1, 2, 1]
    }).with_format("tf")
print()

numerical = tf.reshape(dataset["feature1"], (len(dataset["feature1"]), -1))
input_shape = numerical.shape[1:]
# Create a Normalization layer and set its internal state using the training data
normalizer: keras.layers.Normalization = layers.Normalization()
print(normalizer.dtype)
normalizer.adapt(numerical)
print(normalizer.is_adapted)
print(normalizer(numerical))
numerical = keras.Input(shape=(1,), name="feature1")
x1 = normalizer(numerical)

# Use StringLookup to build an index of the feature values and encode output.
lookup = layers.StringLookup(output_mode="int", vocabulary=['blue', 'red'])
categorical = keras.Input(shape=(1,), name="feature2", dtype=tf.string)
x2 = lookup(categorical)

x = keras.layers.concatenate([x1, tf.cast(x2, dtype=tf.float32)])
process_1 = layers.Activation('relu')(x2)
y = layers.Dense(1, name="target")(process_1)


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
