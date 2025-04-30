import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt
from constants import *

# Load and preprocess tf_flowers dataset
def load_data(img_size=(180, 180), batch_size=32):
	(train_ds, test_ds), ds_info = tfds.load(
		'tf_flowers',
		split=['train[:80%]', 'train[80%:]'],
		as_supervised=True,
		with_info=True
	)

	def preprocess(image, label):
		image = tf.image.resize(image, img_size)
		image = tf.cast(image, tf.float32) / 255.0 # normalize pixel values to be between [0, 1]
		return image, label

	# batch - group of images and labels
	# prefetch - load data in advance
	train_ds = train_ds.map(preprocess).batch(batch_size).prefetch(tf.data.AUTOTUNE)
	test_ds = test_ds.map(preprocess).batch(batch_size).prefetch(tf.data.AUTOTUNE)

	return train_ds, test_ds, ds_info

# Create CNN model
def create_model(input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3), num_classes=NUM_CLASSES):
	model = tf.keras.Sequential([
		tf.keras.layers.InputLayer(input_shape=input_shape),	# input layer
		tf.keras.layers.Conv2D(32, 3, activation='relu'), 		# 32 filters, 3x3 kernel, relu activation
		tf.keras.layers.MaxPooling2D(), 						# reduce dimensionality 
		tf.keras.layers.Conv2D(64, 3, activation='relu'), 		# 64 filters, 3x3 kernel, relu activation
		tf.keras.layers.MaxPooling2D(), 						# reduce dimensionality
		tf.keras.layers.Flatten(), 								# flatten the output - 1D array
		tf.keras.layers.Dense(128, activation='relu'), 			# 128 neurons, relu activation
		tf.keras.layers.Dense(num_classes) 						# output layer
	])

	# compile the model
	model.compile(
		optimizer='adam',
		loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
		metrics=['accuracy']
	)
	return model

# Show sample image
def show_sample(image, label, class_names):
	plt.imshow(image)
	plt.title(f"Label: {class_names[label]}")
	plt.axis('off')
	plt.show()

# Main routine
def main():
	train_ds, test_ds, ds_info = load_data()
	class_names = ds_info.features['label'].names

	# Show a sample image from the dataset
	for image, label in train_ds.take(3):
		show_sample(image[0].numpy(), label[0].numpy(), class_names)

	model = create_model()
	model.fit(train_ds, epochs=EPOCHS)
	model.evaluate(test_ds)

	# Optional: predict on one sample from test set
	for i in range(10):
		for image_batch, label_batch in test_ds.take(10):
			logits = model(image_batch, training=False)
			probs = tf.nn.softmax(logits)
			pred = tf.argmax(probs[i]).numpy()
			true_label = label_batch[i].numpy()
			
			# Get probabilities for all classes
			probabilities = probs[i].numpy()

			# Sort indices by probability in descending order
			sorted_indices = np.argsort(probabilities)[::-1]
			
			print(f"\nPrediction for image {i+1}:")
			print("True label:", GREEN + f"{class_names[true_label]}" + RESET) # use green color
			print("Top predictions:")
			for idx in sorted_indices:
				print(f"{class_names[idx]}: {probabilities[idx]*100:.2f}%")
			print("-" * 50)

			show_sample(image_batch[i].numpy(), true_label, class_names)
			break

if __name__ == "__main__":
	main()
