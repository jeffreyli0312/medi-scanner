# def main():

#     # ==============================================================
#     # DISPLAY VIDEO WINDOW
#     # ==============================================================
#     cap = cv2.VideoCapture(0)
#     ptime = 0
#     ctime = 0

#     while True:
#         success , img = cap.read()
#         img_iso = np.empty(img.shape)
#         img_iso.fill(0)

#         cv2.imshow("Capture" , img)

#         if cv2.waitKey(1) &0xFF == ord('x'):
#             break # Press 'x' to close window

# if __name__ == '__main__':
#     main()

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

batch_size = 16
img_height , img_width = 180 , 180

train_ds = tf.keras.utils.image_dataset_from_directory(
    base_dir,
    validation_split = 0.2,
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

# plt.figure(figsize=(10, 10))
# for images, labels in train_ds.take(1):
#   for i in range(9):
#     ax = plt.subplot(3, 3, i + 1)
#     plt.imshow(images[i].numpy().astype("uint8"))
#     plt.title(class_names[labels[i]])
#     plt.axis("off")
# plt.show()

# num_classes = 3
# model = tf.keras.Sequential([
#     tf.keras.layers.Rescaling(1./255),
#     tf.keras.layers.Conv2D(32 , 3 , activation='relu'),
#     tf.keras.layers.MaxPooling2D(),
#     tf.keras.layers.Conv2D(32 , 3 , activation='relu'),

# ])

#;mlkjlhjlk