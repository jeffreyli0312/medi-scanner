import tensorflow as tf
import numpy as np
import os
import PIL
import PIL.Image
import pathlib

import matplotlib.pyplot as plt
import cv2
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

base_dir = os.path.dirname("C:\medi-scanner\dataset")
base_dir = os.path.join(base_dir , "dataset")

base_dir = pathlib.Path(base_dir)
image_count = len(list(base_dir.glob("*/*.png")))
print(image_count)

batch_size = 75
img_height , img_width = 180 , 180

# def plotImages(images_arr):
#     fig, axes = plt.subplots(1, 5, figsize=(20,20))
#     axes = axes.flatten()
#     for img, ax in zip(images_arr, axes):
#         ax.imshow(img)
#     plt.tight_layout()
#     plt.show()

# image_gen_train = tf.keras.preprocessing.image.ImageDataGenerator(
#     validation_split = 0.2,
#     rescale = 1./255,
#     rotation_range = 40,
#     width_shift_range = 0.2,
#     height_shift_range = 0.2,
#     shear_range = 0.2,
#     zoom_range = 0.5,
#     horizontal_flip = True,
#     fill_mode = 'nearest'
# )
# train_data_gen = image_gen_train.flow_from_directory(
#     batch_size = batch_size,
#     directory = base_dir, 
#     shuffle = True,
#     target_size = (img_height , img_width),
#     subset = 'training',
#     class_mode = 'sparse'
# )
# image_gen_val = tf.keras.preprocessing.image.ImageDataGenerator(
#     rescale = 1./255
# )
# val_data_gen = image_gen_val.flow_from_directory(
#     batch_size = batch_size,
#     directory = base_dir,
#     shuffle = True,
#     target_size = (img_height , img_width),
#     subset = 'validation',
#     class_mode = 'sparse'
# )
train_ds = tf.keras.utils.image_dataset_from_directory(
    base_dir,
    validation_split = 0.3,
    subset = "training",
    seed = 123,
    image_size = (img_height , img_width),
    batch_size = batch_size
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    base_dir,
    validation_split = 0.2,
    subset = "validation",
    seed = 123,
    image_size = (img_height , img_width),
    batch_size = batch_size
)

class_names = train_ds.class_names
print(class_names)

train_ds = train_ds.cache()
val_ds = val_ds.cache()

# plt.figure(figsize=(10, 10))
# for images, labels in train_ds.take(1):
#   for i in range(9):
#     ax = plt.subplot(3, 3, i + 1)
#     plt.imshow(images[i].numpy().astype("uint8"))
#     plt.title(class_names[labels[i]])
#     plt.axis("off")
# plt.show()

num_classes = 4
model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255),
    tf.keras.layers.Conv2D(32 , 3 , activation='relu'),
    tf.keras.layers.MaxPooling2D(2 , 2),

    tf.keras.layers.Conv2D(64 , 3 , activation='relu'),
    tf.keras.layers.MaxPooling2D(2 , 2),

    tf.keras.layers.Conv2D(64 , 3 , activation='relu'),
    tf.keras.layers.MaxPooling2D(2 , 2),

    tf.keras.layers.Conv2D(128 , 3 , activation='relu'),
    tf.keras.layers.MaxPooling2D(2 , 2),
    
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256 , activation='relu'),
    tf.keras.layers.Dense(num_classes)
])

model.compile(
    optimizer = 'adam',
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
    metrics = (['accuracy'])
)
epochs = 18
history = model.fit(
    train_ds,
    validation_data = val_ds,
    epochs = epochs
)

model.save("/medi-scanner/keras_save/burns")