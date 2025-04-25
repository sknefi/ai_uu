import tensorflow as tf
import numpy as np

# Print TensorFlow version
print(f"TensorFlow version: {tf.__version__}")

# Create a simple TensorFlow model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Generate some random data
x_train = np.random.random((100, 784))
y_train = np.random.randint(0, 10, (100, 1))

# Train the model
model.fit(x_train, y_train, epochs=3, batch_size=32)

print("TensorFlow is working correctly!") 